import os
import time

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_in_docker.settings')

app = Celery('django_in_docker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender: Celery, **kwargs):
    sender.add_periodic_task(5.0, test_task(), name='run every 5')


def test_task():
    for i in range(100):
        print(f'=========== {i}')
        time.sleep(2)
