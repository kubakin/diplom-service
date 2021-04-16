
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service.settings')

app = Celery('service')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'some-task' : {
        'task': 'app.tasks.printer',
        'schedule': 1.0
    },
    'one-more-tast' : {
        'task': 'app.tasks.getStat',
        'schedule' : 60.0
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')