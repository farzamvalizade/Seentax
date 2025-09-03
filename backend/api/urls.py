from django.urls import path

from .views import (
    ProfileAPIView,
    ProblemCountAPIView,
    LeaderboardView,
    UserRankView,
)

urlpatterns = [
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("problem/count/", ProblemCountAPIView.as_view(), name="problem-count"),
    path("leaderboard/", LeaderboardView.as_view(), name="leaderboard"),
    path(
        "leaderboard/user-rank/",
        UserRankView.as_view(),
        name="leaderboard-user-rank",
    ),
]
