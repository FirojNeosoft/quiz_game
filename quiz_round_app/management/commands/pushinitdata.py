from django.contrib.auth.models import User
from django.core.management import BaseCommand, call_command

class Command(BaseCommand):
    help = "sets the user passwords"

    def handle(self, *args, **options):
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()