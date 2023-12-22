from django.core.mail import send_mail
from random import randint
from django.conf import settings
from django.template.loader import render_to_string
from UGDbackend.config import config
from django.utils.html import strip_tags


def send_query_creation_email(sender, instance, **kwargs):
    subject = "New Student Created"
    html_message = render_to_string(
        "email_templates/new_query.html", {"student": instance}
    )
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to_email = config["reciever_mail"]

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message,fail_silently=False)
