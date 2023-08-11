# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from redis.asyncio import Redis

class AbsClient(ABC):
    @property
    @abstractmethod
    def client(self) -> Redis:
        raise NotImplementedError
    
    @property
    @abstractmethod
    def slave_client(self) -> Redis:
        raise NotImplementedError
    
class AbsRedisMixin(AbsClient):
    @abstractmethod
    async def publish(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def subcribe(self, *args, **kwargs):
        raise NotImplementedError
    
class AbsRedisClient(AbsClient):
    @abstractmethod
    async def connect(self, *args, **kwargs):
        raise NotImplementedError