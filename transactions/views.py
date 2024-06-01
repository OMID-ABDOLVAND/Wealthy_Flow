from django.shortcuts import render
from djongo.models import Q
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from transactions.models import Category, Transaction
from transactions.serializaers import CategorySerializer, TransactionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(Q(user=user) | Q(default=True))


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(transactions_bank=user)