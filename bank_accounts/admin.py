from django.contrib import admin
from bank_accounts.models import Bank, BankAccount
# Register your models here.
admin.site.register(Bank)
admin.site.register(BankAccount)