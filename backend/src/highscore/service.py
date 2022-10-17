from ..core.redis import redis
import json


async def example(key: str, value: dict) -> dict:
    await redis.set(key, json.dumps(value))
    return json.loads(await redis.get(key))
