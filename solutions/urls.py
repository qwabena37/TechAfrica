from django.urls import path
from .views import SolutionCreateView

urlpatterns = [
    path('', SolutionCreateView.as_view(), name='solutions'),
]
