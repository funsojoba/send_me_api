from rest_framework import serializers


class SendMoneySerializer(serializers.Serializer):
    amount = serializers.IntegerField()