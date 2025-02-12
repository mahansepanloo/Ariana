import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testt.settings')

app = Celery('testt')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()