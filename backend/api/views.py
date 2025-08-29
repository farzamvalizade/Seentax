from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from judge.models import Problem
from account.models import User

from .serializers import ProfileSerializers

# Create your views here.


class ProblemCountAPIView(APIView):
    def get(self, request):
        count = Problem.objects.count()
        return Response({"count": count}, status=status.HTTP_200_OK)


class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
