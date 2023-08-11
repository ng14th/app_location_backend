# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from pydantic import ValidationError
from core.exceptions.reponse_exception import ErrorResponeException
from core.schema.api_respone import custom_respone
from src.user.sso import route as route_sso
from src.user.db_login import route as route_app
from core.exceptions.handler_exception import *
from .celery_app import make_celery


app = Flask(__name__)
app.register_blueprint(route_sso)
app.register_blueprint(route_app)
celery = make_celery(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    # default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

#add CORS
CORS(app, methods=["POST", "GET"])
CORS(app, origins=["*"])
CORS(app, expose_headers=['*'])

# add handler Exception
@app.errorhandler(ErrorResponeException)
def handler_exception(exception: ErrorResponeException):
    return error_response_exception(exception)
@app.errorhandler(429)
def handler_exception_429(exception):
    return handle_rate_limit_exceeded(exception)
@app.errorhandler(ValidationError)
def handler_exception_validation_error(exception):
    return handle_request_validator_error(exception)


# @app.before_request
# def authenticate():
#     test_raise(request)
    
# def test_raise(request):
#     if request.headers.get('X-User') != 123:
#         raise ErrorResponeException(**get_error_code(1000))
#     return 


@app.get('/')
@limiter.limit("10/minute", key_func=lambda: f"{request.headers.get('X-user')}_root")
def root():
    celery.send_task('test_connect')
    return custom_respone({"data" : ["Hello"]})

@app.get('/connector_celery')
def connector():
    print('Still alive')
    return custom_respone({"data" : ['OK']})

from core.redis_client.sentinel_client import RedisSentinelClient
import asyncio
async def set_up_redis(): 
    RedisClass = RedisSentinelClient
    redis_cache = RedisClass()
    await redis_cache.connect(
        [('172.27.230.14',26379)],
        "mymaster",
        0,
        "nguyennt63",
        True
    )
    return redis_cache
    
async def test():
    redis_cache = await set_up_redis()
    print('1', await redis_cache.client.client_id())
    print('2', await redis_cache.slave_client.client_id())

    set_result = await redis_cache.client.set("test7","abc")
    
    
    

asyncio.run(test())    
if __name__ == "__main__":
    pass
    







