from rest_framework import serializers
from api.models.user import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True, style={
                                     "input_type": "password"})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
