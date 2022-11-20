from __future__ import absolute_import
from django.conf import settings
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_app.settings')

app = Celery('test_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.autodiscover_tasks()
