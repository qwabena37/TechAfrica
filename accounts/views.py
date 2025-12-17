from rest_framework import generics, permissions
from .models import ExpertProfile
from .serializers import UserSerializer


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


def get_object(self):
    return self.request.user