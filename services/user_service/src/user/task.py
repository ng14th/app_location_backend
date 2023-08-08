from celery import shared_task

@shared_task(name="test")
def toll():
    print(123)