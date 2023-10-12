from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sendmail():
    send_mail("Your subscription on site.",
              "Update information about your subscription.",
              settings.EMAIL_HOST_USER,
              ["shlegel.s@me.com"],
              fail_silently=False)
