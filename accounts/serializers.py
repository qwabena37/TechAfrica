from rest_framework import serializers
from .models import User, ExpertProfile


class UserSerializer(serializers.ModelSerializer):
    expert_badge = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'expert_badge']


    def get_expert_badge(self, obj):
        return '✔ Expert' if obj.is_expert else None


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data.get('role', 'user')
        )
        return user