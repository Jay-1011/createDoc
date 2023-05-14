from rest_framework import serializers
from .models import Document
from users.serializers import UserSerializer


class MyModelSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Mark "user" field as read-only

    class Meta:
        model = Document
        fields = '__all__'