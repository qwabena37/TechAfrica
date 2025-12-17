from rest_framework import generics, permissions
from .models import Issue
from .serializers import IssueSerializer


class IssueListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all().order_by('-created_at')
    serializer_class = IssueSerializer
    permission_classes = [permissions.IsAuthenticated]


def perform_create(self, serializer):
    serializer.save(user=self.request.user)