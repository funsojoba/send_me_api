from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from api.serializers.register_serializer import RegisterSerializer


class ResgisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        password = data.get('password', '')

        if serializer.is_valid():
            user = get_user_model().objects.create(email=email, password=password,
                                                   first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return Response({"data": serializer.data, "message": "success"}, status=status.HTTP_201_CREATED)

        return Response({"data": serializer.errors, "message": "failure"}, status=status.HTTP_400_BAD_REQUEST)
