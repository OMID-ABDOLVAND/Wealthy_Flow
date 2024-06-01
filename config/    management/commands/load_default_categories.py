from django.core.management.base import BaseCommand
from transactions.models import Category


class Command(BaseCommand):
    help = 'Load default categories'

    def handle(self, *args, **kwargs):
        default_categories = [
            'Groceries', 'Dining Out', 'Utilities', 'Rent/Mortgage', 'Transportation',
            'Entertainment', 'Health', 'Insurance', 'Education', 'Clothing',
            'Personal Care', 'Travel', 'Gifts/Donations', 'Subscriptions',
            'Household', 'Childcare', 'Pets', 'Miscellaneous'
        ]
        for category_name in default_categories:
            Category.objects.get_or_create(name=category_name, defaults={'default': True})
        self.stdout.write(self.style.SUCCESS('Successfully loaded default categories'))
