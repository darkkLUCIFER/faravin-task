from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.api.serializers import RegisterSerializer


class RegisterCreatorView(APIView):
    """
        post:
            register creator

            body: [username, password]
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            user_exists: bool = get_user_model().objects.filter(username=username).exists()

            if user_exists:
                return Response(
                    {
                        'errors': 'user exists'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                get_user_model().objects.create(
                    username=username,
                    password=make_password(password),
                    is_creator=True
                )
                return Response(
                    {
                        'data': 'user created'
                    },
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                serializer.errors
            )


class RegisterViewerView(APIView):
    """
        post:
            register viewer

            body: [username, password]
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            user_exists: bool = get_user_model().objects.filter(username=username).exists()

            if user_exists:
                return Response(
                    {
                        'errors': 'user exists'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            else:
                get_user_model().objects.create(
                    username=username,
                    password=make_password(password),
                    is_viewer=True
                )
                return Response(
                    {
                        'data': 'user created'
                    },
                    status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                serializer.errors
            )


class LoginView(APIView):
    """
        post:
            verify user and return access and refresh token

            body: [username, password]
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            user = get_user_model().objects.get(username=username)

            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)

                token = str(refresh.access_token)
                refresh_token = str(refresh)

                return Response(
                    {
                        'access': token,
                        'refresh': refresh_token
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'errors': 'invalid credentials'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
