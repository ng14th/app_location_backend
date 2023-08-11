# -*- coding: utf-8 -*-
import asyncio
from functools import wraps
from typing import List, Tuple , Optional
from core.abstractions.redis_abs import AbsRedisClient
from redis.asyncio import Redis, Sentinel




class RedisSentinelClient(AbsRedisClient):
    def __init__(self, **kwargs) -> None:
        self._sentinel_client: Sentinel = None
        self._sentinel_name: Optional[str] = None
        self._master_client: Redis = None
        self._slave_client: Redis = None
        self._is_connected: bool = False
        self._is_have_master: bool = True
        self._master_ip: Optional[str] = None
    
    @property
    def is_connected(self):
        return self._is_connected
    
    @property
    def client(self) -> Redis:
        if self._is_have_master:
            print("vào à")
            return self._master_client
        return self._slave_client
    
    @property
    def slave_client(self) -> Redis:
        return self._slave_client
    
    async def change(self):
        master = self._master_ip
        return await self._slave_client.execute_command("REPLICAOF", master[0], master[1])
    
    async def get_clients(self):
        master = None
        try:
            master = await self._sentinel_client.discover_master(self._sentinel_name)
        except Exception as e:
            self._is_have_master = False
            print(e)
            
        slaves = await self._sentinel_client.discover_slaves(self._sentinel_name)
        self._master_client = self._sentinel_client.master_for(self._sentinel_name)
        if not slaves:
            self._slave_client = self._master_client
        else:
            self._slave_client = self._sentinel_client.slave_for(self._sentinel_name)
        
        print(f'redis clients | master {master} | slaves {slaves}')

    
    async def connect(
        self, 
        sentinel_servers: List[Tuple[str, int]],
        sentinel_name : str,
        redis_db : int = 0,
        redis_password: str = None,
        decode_respone: bool = True,
        **kwargs
        ):
        try:
            if isinstance(self._sentinel_client, Sentinel):
                return

            self._sentinel_client = Sentinel(
                sentinel_servers,
                db=redis_db,
                password=redis_password,
                decode_responses=decode_respone
            )

            self._sentinel_name = sentinel_name
            await self.get_clients()
            
            self._name = f'Sentinel-Client-{sentinel_servers}'
            self._is_connected = True
            print(f'RedisSentinelClient {self._name} | connected {self._is_connected}')
        except Exception as e:
            print(str(e))

