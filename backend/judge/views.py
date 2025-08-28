import time

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from judge.models import Problem, Submission, ProgrammingLanguage
from .tasks import evaluate_submission


@csrf_exempt
def run_judge(request, problem_id):
    """
    گرفتن problem_id از URL،
    ساختن یه Submission جدید،
    فرستادن به Celery برای داوری
    """

    try:
        problem = Problem.objects.get(id=problem_id)
    except Problem.DoesNotExist:
        return JsonResponse({"error": "Problem not found"}, status=404)

    # گرفتن language_id و source_code از request.POST (یا request.GET برای تست ساده)
    language_id = request.POST.get("language_id")
    source_code = request.POST.get("source_code")

    if not language_id or not source_code:
        return JsonResponse({"error": "language_id and source_code are required"}, status=400)

    try:
        language = ProgrammingLanguage.objects.get(id=language_id)
    except ProgrammingLanguage.DoesNotExist:
        return JsonResponse({"error": "Language not found"}, status=404)

    # ساخت Submission جدید
    submission = Submission.objects.create(
        user=request.user,
        problem=problem,
        language=language,
        source_code=source_code,
        status=Submission.StatusChoices.queued,
        verdict=Submission._meta.get_field("verdict").choices[0][0],  # پیشفرض (مثلا Accepted)
    )

    # فرستادن به celery
    task = evaluate_submission.delay(submission.id)
    while not task.ready():
        print(task.state)
        time.sleep(1)
    print(task.get())

    return JsonResponse({
        "message": "Submission created and sent to judge",
        "submission_id": submission.id,
        "status": submission.status,
    })
