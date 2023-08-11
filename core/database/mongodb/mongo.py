# -*- coding: utf-8 -*-
import asyncio
from umongo.frameworks import MotorAsyncIOInstance
from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings

# print(env.APP_DB_MONGO_URI)
url = f'mongodb://{settings.MONGO_DB_USERNAME}:{settings.MONGO_DB_PASSWORD}@{settings.MONGO_DB_HOST}:{settings.MONGO_DB_PORT}/?authMechanism=DEFAULT'
client = AsyncIOMotorClient(url)[settings.MONGO_DB_NAME_DB]
# fix mongo connection attached to a different loop
client.get_io_loop = asyncio.get_running_loop
umongo_cnx = MotorAsyncIOInstance(client)