from rest_framework import serializers

from bank_accounts.models import BankAccount, Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name', 'avatar']
        read_only_fields = ['name', 'avatar']


class BankAccountSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta:
        model = BankAccount
        fields = ['account_number', 'balance', 'created_at', 'last_transaction_date', 'bank', 'user']
        read_only_fields = ['created_at', 'user']
