from django.contrib.auth import authenticate
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token

from api.serializers.login_serializer import LoginSerializer
from rest_framework.response import Response


class LoginView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        if email is None or password is None:
            return Response(errors={'invalid_credentials': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=email, password=password)

        if not user:
            return Response({'invalid_credentials': 'Ensure both email and password are correct and you have verify you account'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(user)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
