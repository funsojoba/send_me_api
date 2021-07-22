from rest_framework.views import APIView
from rest_framework import permissions, status

from api.models.user import User


class RecieveMoneyView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        amount = request.GET.get('amount')
        key = request.GET.get('get')

        