from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from courses.models import Cours


@shared_task
def sendmail(product_id):
    cours = Cours.objects.get(pk=product_id)
    sublist = []
    for sub in cours.subscription_set.all():
        sublist.append(sub.owner.email)

    send_mail("Your subscription on site.",
              f"Update information about your subscription.",
              settings.EMAIL_HOST_USER,
              sublist,
              fail_silently=False)
