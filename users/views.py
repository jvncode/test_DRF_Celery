from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers
from .models import UserRegister
from rest_framework import status
from .forms import UserForm
from users import tasks
import logging
import os
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


class User_APIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            form = UserForm()
            success_message = ''
            context = {
                'form': form,
                'success_message': success_message,
            }
            logging.debug("USER APIVIEW GET - SUCCESS")
        except Exception as e:
            logging.error("USER APIVIEW GET : {}".format(e))
        finally:
            return render(request, 'index.html', context)

    def post(self, request):
        try:
            serializer = UserSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logging.debug("USER APIVIEW POST - SUCCESS")
                if os.environ.get('APP_ENV', default='') == 'PROD':
                    tasks.send_mail.delay(request.data['email'])
                    tasks.send_sms.delay(request.data['phone'])
                    logging.debug("USER APIVIEW PROD POST TASKS - SUCCESS")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logging.error("USER APIVIEW POST : {}".format(e))
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Profile_APIView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            profile = UserRegister.objects.get(id=kwargs['pk'])
            serializer = UserSerializers(profile)
            context = {'verified_email': True,
                    'verified_phone': False}
            logging.debug("PROFILE APIVIEW GET - Profile: {}".format(profile))
        except Exception as e:
            logging.error("PROFILE APIVIEW GET : {}".format(e))
        finally:
            return Response({**serializer.data, **context})
