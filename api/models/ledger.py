import uuid

from django.db import models
from api.models.user import User


class Ledger(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    ledger_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user_id.first_name} {self.user_id.last_name}\'s ledger'
