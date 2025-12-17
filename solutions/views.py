from rest_framework import generics
from .models import Solution
from .serializers import SolutionSerializer
from .permissions import IsExpert


class SolutionCreateView(generics.CreateAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [IsExpert]


    def perform_create(self, serializer):
        serializer.save(expert=self.request.user)