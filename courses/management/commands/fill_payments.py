from django.core.management import BaseCommand
from courses.models import Payment, Cours, Lesson


class Command(BaseCommand):

    def handle(self, *args, **options):
        courses = Cours.objects.all()
        summ = 200
        for cours in courses:
            Payment.objects.create(summ=summ, cours=cours)
            summ += 20

        lessons = Lesson.objects.all()
        summ = 15
        method = 'cash'
        for lesson in lessons:
            Payment.objects.create(summ=summ, lesson=lesson, payment_method=method, date='2023-09-20')
            if method == 'cash':
                method = 'non-cash'
            else:
                method = 'cash'
