from django.urls import path, include
from rest_framework.routers import DefaultRouter
from bank_accounts.views import BankAccountViewSet

router = DefaultRouter()
router.register(r'bank-accounts', BankAccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
]