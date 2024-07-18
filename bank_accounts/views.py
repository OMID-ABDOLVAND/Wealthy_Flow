from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from bank_accounts.models import BankAccount
from bank_accounts.serializers import BankAccountSerializer
from config.permissions import IsOwnerOrAdmin


class BankAccountViewSet(ModelViewSet):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        # Return only the bank accounts owned by the authenticated user
        return BankAccount.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the bank account with the authenticated user
        serializer.save(user=self.request.user)

