from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from api.models.user import User
from api.models.ledger import Ledger
from api.serializers.amount import AmountSerializer

class SendMoneyView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AmountSerializer

    def put(self, request):
        data = request.data
        user_id = request.user.id
        serializer = self.serializer_class(data=data)

        user = User.objects.get(id=user_id)

        serializer.is_valid(raise_exception=True)

        db_amount = user.account_balance
        request_amount = data.get('amount')

        if int(db_amount) < int(request_amount):
            return Response({"error":"insufficient amount"})
        
        total_amount = db_amount - request_amount
        user.account_balance = total_amount
        user.save()

        # update ledger
        new_ledger = Ledger.objects.create(user_id=request.user, ledger_type="expense", amount=db_amount)
        new_ledger.save()

        return Response({"account balance":total_amount, "message":"success"}, status=status.HTTP_200_OK)
