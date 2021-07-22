from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from api.models.user import User
from api.models.ledger import Ledger
from api.serializers.amount import AmountSerializer


class RecieveMoneyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AmountSerializer

    def put(self, request):
        data = request.data
        user_id = request.user.id

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        db_user = User.objects.get(id=user_id)
        initial_amount = db_user.account_balance
        request_amount = data.get('amount')
        total_amount = initial_amount + request_amount
        
        db_user.account_balance = total_amount
        db_user.save()

        # update ledger
        new_ledger = Ledger.objects.create(user_id=request.user, ledger_type="income", amount=total_amount)
        new_ledger.save()

        return Response(
            {"account balance":total_amount, 
            "message":"success", 
            "user":db_user.first_name,
            "initial_amount": db_user.account_balance,
            "request_amount":data.get('amount')
            }, status=status.HTTP_200_OK)





