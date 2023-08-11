from core.redis_client.sentinel_client import RedisSentinelClient
import asyncio
async def set_up_redis(): 
    RedisClass = RedisSentinelClient
    redis_cache = RedisClass()
    await redis_cache.connect(
        [('172.30.227.176',26379)],
        "test",
        0,
        "nguyennt63",
        True
    )
    
if __name__ == "__main__":
    asyncio.run(set_up_redis())