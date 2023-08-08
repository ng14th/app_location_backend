
from celery import Celery
from settings.config import settings

def make_celery(app):
    celery = Celery(app.name, 
                backend='rpc://', 
                broker=f"amqp://{settings.RABBIT_MQ_USERNAME}:{settings.RABBIT_MQ_PASSWORD}@{settings.RABBIT_MQ_URL}/{settings.RABBIT_MQ_VH}")

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery