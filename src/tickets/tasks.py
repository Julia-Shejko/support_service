from time import sleep

from config.celery import celery_app


@celery_app.task()
def hello_task(name: str):
    sleep(3)
    print(f"Hello, {name}! This is CELERY 🙂.")
