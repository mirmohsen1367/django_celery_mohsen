from celery import shared_task
from time import sleep

@shared_task(bind=True)
def \
        gotosleeo(self, x, y):
    return sleep(x+y)

