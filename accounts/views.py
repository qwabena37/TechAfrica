from rest_framework import generics, permissions
from .models import ExpertProfile
from .serializers import UserSerializer
from .serializers import RegisterSerializer
from .models import User


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


    def get_object(self):
        return self.request.user


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]