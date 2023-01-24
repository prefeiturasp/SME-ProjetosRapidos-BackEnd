from django.conf import settings
from django.core.mail import send_mail


def send_email_support(subject, message, from_email='noreply@sme.prefeitura.sp.gov.br', recipient_list=[]):
    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
    except Exception as e:
        print("error send_email_support", str(e))
