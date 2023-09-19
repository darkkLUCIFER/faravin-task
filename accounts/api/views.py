from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

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
                    }
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
                    }
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
                    }
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
                    }
                )
        else:
            return Response(
                serializer.errors
            )
