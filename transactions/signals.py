from django.db.models.signals import post_save
from django.dispatch import receiver
from transactions.models import Transaction

""" use signals to handle buissines logic of withdraw and deposite """
@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, created, **kwargs):
    if instance.transaction_status == Transaction.Status.SAVE:
        bank_account = instance.bank_account
        if instance.transaction_type == Transaction.TransactionType.DEPOSIT:
            bank_account.deposit(instance.amount)
        elif instance.transaction_type == Transaction.TransactionType.WITHDRAWAL:
            bank_account.withdraw(instance.amount)