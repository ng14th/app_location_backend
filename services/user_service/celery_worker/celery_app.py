from celery import Celery
from settings.config import settings

celery = Celery('Celery-User-Service', 
                backend='rpc://', 
                broker=f"amqp://{settings.RABBIT_MQ_USERNAME}:{settings.RABBIT_MQ_PASSWORD}@{settings.RABBIT_MQ_URL}/{settings.RABBIT_MQ_VH}")

celery.backend.cleanup()
# Disable task result save in redis
celery.conf.task_ignore_result = True
celery.conf.task_store_errors_even_if_ignored = True
celery.conf.timezone = 'UTC'

celery.conf.result_backend_transport_options = {
    'retry_policy': {
       'timeout': 5.0
    }
}

celery.autodiscover_tasks(['celery_worker.tasks'])

celery.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
    task_acks_late=True,                                       #True : when task is processing worker down -> worker up task will be process again
    broker_transport_options={'visibility_timeout': 7200},     #Task will restore in queue when get error in processing -> will be process again by another worker
    task_reject_on_worker_lost=False,                          #Task will send to retry queue to another worker process when worker lost
    task_reject_on_connection_lost=True,                       #Task will send to retry queue to another worker process when connection lost
    worker_pool_restarts=True,                                 #Auto restart worker when it got error
    task_acks_on_failure_or_timeout=False,                     #Never ack task when it failure or timeout -> retry queue to another worker process when worker lost
    worker_concurrency=8,                                      #Number of worker
    # worker_autoscaler='celery.worker.autoscale:None',        #Scale worker   
    # task_ignore_result=True,
    # task_store_errors_even_if_ignored=True,
    # result_persistent=False,
    # task_default_queue='default'
)
