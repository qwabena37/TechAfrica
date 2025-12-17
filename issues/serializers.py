from rest_framework import serializers
from .models import Issue


class IssueSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()


class Meta:
    model = Issue
    fields = '__all__'