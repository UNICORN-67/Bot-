# Feature toggles

from .redisdb import redis

async def enable_feature(chat_id: int, feature: str):
    return await redis.set(f"{feature}:{chat_id}", "on")

async def disable_feature(chat_id: int, feature: str):
    return await redis.delete(f"{feature}:{chat_id}")

async def is_enabled(chat_id: int, feature: str) -> bool:
    return await redis.get(f"{feature}:{chat_id}") == "on"