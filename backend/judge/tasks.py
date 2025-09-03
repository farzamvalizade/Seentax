from django.contrib.auth import get_user_model
from django.db import transaction

from celery import shared_task
from django.db.models import F

from judge.models import Submission, TestCase, TestCaseResult, Problem, ScoreAward
from judge.core.docker_pool import DockerPool
from judge.core.executor import CodeExecutor

User = get_user_model()

language_pools = {}


def get_pool(language):
    if language.name not in language_pools:
        language_pools[language.name] = DockerPool(
            image=f"judge-{language.name.lower().replace(" ", "_")}", pool_size=2
        )
    return language_pools[language.name]


def get_points_for_problem(problem: Problem) -> int:
    if problem.difficulty == Problem.DifficultyChoices.easy:
        return 10
    elif problem.difficulty == Problem.DifficultyChoices.normal:
        return 20
    elif problem.difficulty == Problem.DifficultyChoices.hard:
        return 30
    return 0


@shared_task
def evaluate_submission(submission_id):
    submission = Submission.objects.get(id=submission_id)
    submission.status = "Running"
    submission.save()

    problem = submission.problem
    language = submission.language
    print(1)
    pool = get_pool(language)
    print(2)
    container = pool.acquire()
    executor = CodeExecutor(
        container,
        {
            "run_command": language.run_command,
            "compile_command": language.compile_command,
            "need_compile": language.need_compile,
        },
        time_limit=problem.time_limit_ms,
        memory_limit=problem.memory_limit_kb,
    )

    executor.copy_code(submission.source_code, f"Main.{language.extension}")
    compile_result = executor.compile()

    if not compile_result["success"]:
        submission.verdict = "CE"
        submission.status = "Done"
        submission.save()
        pool.release(container)
        return

    all_results = []
    final_verdict = "AC"
    print(3)
    for test_case in TestCase.objects.filter(problem=problem):
        result = executor.run_test(test_case.input, test_case.expected_output)
        print(result["verdict"])

        TestCaseResult.objects.create(
            submission=submission,
            test_case=test_case,
            verdict=result["verdict"],
            stdout=result["stdout"],
            stderr=result["stderr"],
            time_ms=result["time_ms"],
            memory_kb=result["memory_kb"],
            exit_code=result["exit_code"],
        )

        all_results.append(result["verdict"])
        if result["verdict"] != "AC":
            final_verdict = result["verdict"]
        print(final_verdict)
    print(4)
    submission.verdict = final_verdict
    submission.status = "Done"
    submission.save()

    pool.release(container)

    if final_verdict == "AC":
        points = get_points_for_problem(problem)
        user = submission.user

        with transaction.atomic():
            award, created = ScoreAward.objects.get_or_create(
                user=user,
                problem=problem,
                defaults={"points": points},
            )
            if created:
                User.objects.filter(id=user.id).update(point=F("point") + points)
