from django.contrib.auth import get_user_model
from rest_framework import serializers


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=15)
    # class Meta:
    #     model = get_user_model()
    #     fields = ['username', 'password']
