from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_qualia_email(email, template, fields):
    fields['STATIC_URL'] = settings.STATIC_URL
    subject = render_to_string('emails/' + template + '/subject.txt', fields)
    subject = ''.join(subject.splitlines())
    message = render_to_string('emails/' + template + '/body.txt', fields)
    html_message = render_to_string('emails/' + template + '/body.html', fields)
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        email,
        fail_silently=True,
        html_message=html_message
    )
