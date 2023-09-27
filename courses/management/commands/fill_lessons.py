from django.core.management import BaseCommand
from courses.models import Cours, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        courses = Cours.objects.all()
        for cours in courses:
            Lesson.objects.create(title='Lesson 1', description='Your first lesson in cours', cours=cours)
            Lesson.objects.create(title='Lesson 2', description='Your second lesson in cours', cours=cours)
            Lesson.objects.create(title='Lesson 3', description='Your third lesson in cours', cours=cours)
            Lesson.objects.create(title='Lesson 4', description='Your final lesson in cours', cours=cours)
