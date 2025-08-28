import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('Seentax')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['judge'])

@app.task
def add(x, y):
    print(x + y)
    return x + y
