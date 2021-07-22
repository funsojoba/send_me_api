from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from api.models.user import User
from api.serializers.send_money_serializer import SendMoneySerializer

class SendMoneyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SendMoneySerializer

    def put(self, request):
        data = request.data
        user_id = request.user.id
        serializer = self.serializer_class(data=data)

        user = User.objects.get(id=user_id)

        serializer.is_valid(raise_exception=True)

        db_amount = user.account_balance
        request_amount = data.get('amount')

        if db_amount < request_amount:
            print(type(user.account_balance), type(data.get('amount')))
            return Response({"error":"insufficient amount"})
        
        db_amount -= request_amount

        return Response({"id": user_id, "balance":db_amount })
