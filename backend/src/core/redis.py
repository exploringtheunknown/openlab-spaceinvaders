from functools import lru_cache
import aioredis
from aioredis import Redis
from pydantic import BaseModel


class Redis(BaseModel):
    redis: Redis

    async def __init__(self):
        self.redis = aioredis.from_url("redis://localhost")

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value: str):
        await self.redis.set(key, value)


@lru_cache
def get_cache():
    return Redis()


redis = get_cache()
