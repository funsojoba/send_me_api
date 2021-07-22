from django.urls import path
from .views.auth.register import ResgisterView
from .views.auth.login import LoginView
from .views.transact.send import SendMoneyView

urlpatterns = [
    path('auth/register/', ResgisterView.as_view(), name="register"),
    path('auth/login/', LoginView.as_view(), name="login"),
    path('transact/send/', SendMoneyView.as_view(), name="login"),

]
