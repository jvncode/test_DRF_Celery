import instasent
import os
import logging

from celery import shared_task
from redmail import EmailSender
from dotenv import load_dotenv

load_dotenv()

# Logs Config
APP_ENV = os.environ.get('APP_ENV', default='')


def ConfigEnv():
    if APP_ENV == 'DEV':
        return logging.DEBUG
    elif APP_ENV == 'PROD':
        return logging.WARNING


logging.basicConfig(filename='logs/app.log',
                    format='%(levelname)s %(asctime)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    level=ConfigEnv())


@shared_task(name="send_email")
def send_mail(email):
    mail = EmailSender(
        host='smtp.gmail.com',
        port=465,
        username=os.environ.get('EMAIL_SENDER', default=''),
        password=os.environ.get('PASS_EMAIL_SENDER', default=''),
    )
    try:
        mail.send(
            subject='Correo de verificación',
            receivers=email,
            text='Este es un correo de verificación\
                    para confirmar su registro en nuestra plataforma',
            attachments={}
        )
        logging.debug(f'Correo de verificación enviado\
                        correctamente a la dirección {email}')
    except Exception as e:
        logging.error(f'Error en el envío del correo de\
                        verificación a la dirección {email}: {e}')
    finally:
        return mail


@shared_task(name="send_sms")
def send_sms(number):
    try:
        client = instasent.Client(
            os.environ.get('TOKEN_SEND_SMS', default=''))
        response = client.send_sms(
            'Instasent', number, 'Este es un correo de verificación\
                para confirmar su registro en nuestra plataforma.')
        logging.debug(f'Mensaje SMS de verificación\
                        enviado correctamente al número {number}')
    except Exception as e:
        logging.error(f'Error en el envío del mensaje SMS\
                        de verificación al número {number}: {e}')
    finally:
        return response
