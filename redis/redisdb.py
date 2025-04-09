# Redis DB connection

from redis import from_url
from bot import config

redis = from_url(config.REDIS_URI, decode_responses=True)

async def get_toggle(toggle_type: str, chat_id: int) -> bool:
    return r.get(f"{toggle_type}_{chat_id}") == "true"

async def set_toggle(toggle_type: str, chat_id: int, value: bool):
    r.set(f"{toggle_type}_{chat_id}", str(value).lower())
