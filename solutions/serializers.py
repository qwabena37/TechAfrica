from rest_framework import serializers
from .models import Solution

class SolutionSerializer(serializers.ModelSerializer):
    expert = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Solution
        fields = '__all__'
        read_only_fields = ['expert', 'created_at']
