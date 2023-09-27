from django.core.management import BaseCommand
from courses.models import Cours


class Command(BaseCommand):

    def handle(self, *args, **options):
        Cours.objects.create(title='First step in Django', description='Cours for beginners.')
        Cours.objects.create(title='Second step in Django', description='Cours for advanced.')
        Cours.objects.create(title='Final step in Django', description='Cours for professionals.')
