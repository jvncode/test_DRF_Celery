from celery import shared_task

from redmail import EmailSender
import instasent
import os
from dotenv import load_dotenv

load_dotenv()

#@shared_task(name="send_email")
def send_mail(email):
    mail = EmailSender(
        host='smtp.gmail.com',
        port=465,
        username=os.environ.get('EMAIL_SENDER', default=''),
        password=os.environ.get('PASS_EMAIL_SENDER', default=''),
    )
    mail.send(
        subject='Correo de verificación',
        receivers=email,
        text='Este es un correo de verificación para confirmar su registro en nuestra plataforma',
        attachments={}
    )
    return mail

#@shared_task(name="send_sms")
def send_sms(number):
    client = instasent.Client(os.environ.get('TOKEN_SEND_SMS', default=''))
    response = client.send_sms(
        'Instasent', number, 'Este es un correo de verificación para confirmar su registro en nuestra plataforma.')
    return response
