import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_in_docker.settings')

app = Celery('django_in_docker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
