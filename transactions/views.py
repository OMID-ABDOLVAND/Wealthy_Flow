from django.shortcuts import render
from djongo.models import Q
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from config.permissions import IsOwnerOrAdmin
from transactions.models import Category, Transaction
from transactions.serializaers import CategorySerializer, TransactionSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(Q(user=user) | Q(default=True))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['destroy', 'partial_update', 'update']:
            return [IsOwnerOrAdmin()]
        return super().get_permissions()

    # todo: test and then checkout done



class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(transactions_bank=user)