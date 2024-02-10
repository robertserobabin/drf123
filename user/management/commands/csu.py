from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro',
            first_name='Dmitriy',
            last_name='Alushkin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('12345')
        user.save()