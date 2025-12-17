from rest_framework import serializers
from .models import User, ExpertProfile


class UserSerializer(serializers.ModelSerializer):
    expert_badge = serializers.SerializerMethodField()


class Meta:
    model = User
    fields = ['id', 'username', 'email', 'role', 'expert_badge']


def get_expert_badge(self, obj):
    return '✔ Expert' if obj.is_expert else None