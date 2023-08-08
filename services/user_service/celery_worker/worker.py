from .celery_app import celery


@celery.task(name="test_worker")
def test_share():
    print(50)