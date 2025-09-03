from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from judge.models import Problem, Submission, ProgrammingLanguage
from .tasks import evaluate_submission

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return

class RunJudgeAPIView(APIView):
    authentication_classes = [CsrfExemptSessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, problem_id):
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return Response({"error": "Problem not found"}, status=status.HTTP_404_NOT_FOUND)

        language_id = request.data.get("language_id")
        source_code = request.data.get("source_code")

        if not language_id or not source_code:
            return Response(
                {"error": "language_id and source_code are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            language = ProgrammingLanguage.objects.get(id=language_id)
        except ProgrammingLanguage.DoesNotExist:
            return Response({"error": "Language not found"}, status=status.HTTP_404_NOT_FOUND)

        submission = Submission.objects.create(
            user=request.user,
            problem=problem,
            language=language,
            source_code=source_code,
            status=Submission.StatusChoices.queued,
            verdict=Submission._meta.get_field("verdict").choices[0][0],
        )

        evaluate_submission.delay(submission.id)

        return Response(
            {
                "message": "Submission created and sent to judge",
                "submission_id": submission.id,
                "status": submission.status,
            },
            status=status.HTTP_201_CREATED,
        )
