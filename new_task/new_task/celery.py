import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_task.settings')

app = Celery('new_task')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()
