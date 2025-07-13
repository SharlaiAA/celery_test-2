import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celsen.settings')

app = Celery('celsen')
app.config_from_object('django.conf.settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-1-min' : {
        'task' : 'main.task.send_beat_email',
        'schedule' : crontab(minute='*/1')
    },
}