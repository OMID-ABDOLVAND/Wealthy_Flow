from django.contrib.auth import get_user_model
from djongo import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'


class BankAccount(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.IntegerField()
    minimum_balance_requirement = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_transaction_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.bank.name} - {self.account_number}"

    class Meta:
        verbose_name = 'Bank Account'
        verbose_name_plural = 'Bank Accounts'

# TODO: best practice
# TODO: CASCADE OR ...

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.save()
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.save()
            return True
        return False
