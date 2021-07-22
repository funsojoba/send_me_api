from django.contrib import admin

from .models.user import User
from .models.ledger import Ledger


admin.site.register((User, Ledger))