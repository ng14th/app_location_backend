from celery import shared_task

@shared_task(name="test")
def test_share():
    print(50)