from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from transactions.models import Category

# help = 'Create a user and load default categories for that user'
# python manage.py load_default_categories <username> <email> <password>



class Command(BaseCommand):
    help = 'Create a user and load default categories for that user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username of the new user')
        parser.add_argument('email', type=str, help='The email of the new user')
        parser.add_argument('password', type=str, help='The password for the new user')

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        password = kwargs['password']
        User = get_user_model()

        user, created = User.objects.get_or_create(defaults={'email': email})
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created user "{email}"'))
        else:
            self.stdout.write(self.style.WARNING(f'User "{email}" already exists'))

        default_categories = [
            'Groceries', 'Dining Out', 'Utilities', 'Rent/Mortgage', 'Transportation',
            'Entertainment', 'Health', 'Insurance', 'Education', 'Clothing',
            'Personal Care', 'Travel', 'Gifts/Donations', 'Subscriptions',
            'Household', 'Childcare', 'Pets', 'Miscellaneous'
        ]

        for category_name in default_categories:
            Category.objects.get_or_create(name=category_name, user=user, defaults={'default': True})

        self.stdout.write(self.style.SUCCESS(f'Successfully loaded default categories for user "{email}"'))
