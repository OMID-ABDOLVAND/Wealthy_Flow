from django.contrib.auth import get_user_model
from djongo import models
from bank_accounts.models import BankAccount
import uuid


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='categories')
    default = models.BooleanField(default=False)
    avatar = models.ImageField(null=True, blank=True)

    # TODO: show category thats admin add and owner add

    def __str__(self):
        return self.name

    @staticmethod
    def get_default_categories():
        return Category.objects.filter(default=True)

    @staticmethod
    def get_user_categories(user):
        return Category.objects.filter(user=user)


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = 'Deposit', 'Deposit'
        WITHDRAWAL = 'Withdrawal', 'Withdrawal'
        TRANSFER = 'Transfer', 'Transfer'

    def generate_transaction_id():
        return str(uuid.uuid4())

    transaction_id = models.CharField(max_length=36, unique=True,
                                      default=generate_transaction_id, editable=False)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.IntegerField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name='transactions_bank')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,
                                 blank=True, related_name='transactions_category')

    def __str__(self):
        return f"{self.transaction_id} - {self.transaction_type} - {self.amount} "
