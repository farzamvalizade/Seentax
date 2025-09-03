from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions

from judge.models import Problem, ProgrammingLanguage

from .serializers import (
    ProfileSerializers,
    ProblemSerializers,
    ProgrammingLanguageSerializer,
)

User = get_user_model()


class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ProblemCountAPIView(APIView):
    def get(self, request):
        count = Problem.objects.count()
        return Response({"count": count}, status=status.HTTP_200_OK)


class UserRankView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        rank = User.objects.filter(point__gt=request.user.point).count() + 1

        return Response(
            {
                "my_rank": rank,
                "my_point": request.user.point,
            },
            status=status.HTTP_200_OK,
        )


class LeaderboardView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        top_users = User.objects.order_by("-point", "id").values(
            "id", "username", "point"
        )[:10]

        return Response(
            {
                "leaderboard": list(top_users),
            }
        )


class ProgrammingLanguageList(generics.ListAPIView):
    queryset = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguageSerializer
    permission_classes = [permissions.AllowAny]


class ProblemListView(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializers
    permission_classes = [permissions.AllowAny]
    ordering = ["-created_at"]
    filterset_fields = ["languages__name", "difficulty"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]


class ProblemDetailView(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializers
    permission_classes = [permissions.AllowAny]
    lookup_field = "id"
