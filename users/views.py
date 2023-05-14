from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            return Response({'token': token, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        error_messages = []
        for field, messages in errors.items():
            error_messages.append(f"{field}: {', '.join(messages)}")
        return Response({'errors': error_messages}, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = User.objects.filter(username=username).first()
            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                token = str(refresh.access_token)
                serializer = UserSerializer(user)
                return Response({'token': token, 'user': serializer.data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
