# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
import time
from typing import Optional
from pydantic import BaseSettings


USER_MODE = os.environ.get('USER')
class BaseSettingMixin(BaseSettings):
    
    #-------- MONGODB ------------
    MONGO_DB_HOST : Optional[str] = "" 
    MONGO_DB_PORT : int = 27016
    MONGO_DB_USERNAME : Optional[str] = ""
    MONGO_DB_PASSWORD : Optional[str] = ""
    MONGO_DB_NAME_DB : Optional[str] = ""

    #-------- POSTGRESQL ------------
    POSTGRE_DB_HOST : Optional[str] = ""
    POSTGRE_DB_PORT : int = 5445
    POSTGRE_DB_USERNAME : Optional[str] = ""
    POSTGRE_DB_PASSWORD : Optional[str] = ""
    POSTGRE_DB_NAME_DB : Optional[str] = ""

    #-------- REDIS ------------
    REDIS_HOST : Optional[str] = ""
    REDIS_PORT : int = 6379
    REDIS_NAMESPACE : Optional[str] = ""
    REDIS_PASSWORD : Optional[str] = ""
    REDIS_DB : int = 1

    #-------- RABBITMQ ------------
    RABBIT_MQ_URL : Optional[str] = ""
    RABBIT_MQ_VH : Optional[str] = ""
    RABBIT_MQ_USERNAME : Optional[str] = ""
    RABBIT_MQ_PASSWORD : Optional[str] = ""

    #-------- MINIO ------------
    MINIO_ENDPOINT : Optional[str] = ""
    MINIO_ACCESS_KEY : Optional[str] = ""
    MINIO_SECRET_KEY : Optional[str] = ""
    MINIO_SECURE : bool = False
    MINIO_LIST_BUCKET : Optional[list] = []
    MINIO_BUCKET : Optional[str] = ""
        
    def add_core_sys_path():
        current_path = Path(os.getcwd())
        sys.path.append(str(current_path.parents[1]))
        
    @classmethod
    def notify_connect_env(cls, env_path):
        print(70*"~")
        print('USER MODE : ', USER_MODE)
        print('ENV SELECTED : ', env_path)
        print(70*"~")
        
    @classmethod
    def set_up(cls, env_path):
        time_reconnect = 1
        if USER_MODE != 'root':
            for i in range(0,5):
                if '.localenv' in os.listdir(env_path):
                    cls.notify_connect_env('.localenv')
                    settings = cls(_env_file=os.path.join(env_path,'.localenv'))
                    return settings
                else:
                    print(f"##-{i}-## Try to init environment again ##-{i}-##")
                time.sleep(time_reconnect+i)
        else:
            for i in range(0,5):
                if '.env' in os.listdir(env_path):
                    cls.notify_connect_env('.env')
                    settings = cls(_env_file=os.path.join(env_path,'.env'))
                    return settings
                else:
                    print(f"##-{i}-## Try to init environment again ##-{i}-##")
                time.sleep(time_reconnect+i)
                
    class Config:
        case_sensitive = True
        validate_assignment = True
        