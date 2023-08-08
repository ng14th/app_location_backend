import requests
from celery import shared_task

@shared_task(name='test_connect')
def test_func():
    return requests.get(url='http://172.30.227.176:8888/connector_celery')