# Redis DB connection

import redis
from bot.config import REDIS_URL

# Initialize Redis connection
redis = redis.Redis.from_url(REDIS_URL, decode_responses=True)

# Toggle management
def get_toggle(group_id: int, toggle_name: str) -> bool:
    value = redis.get(f"toggle:{toggle_name}:{group_id}")
    return value == "true"

def set_toggle(group_id: int, toggle_name: str, value: bool):
    redis.set(f"toggle:{toggle_name}:{group_id}", str(value).lower())

def delete_toggle(group_id: int, toggle_name: str):
    redis.delete(f"toggle:{toggle_name}:{group_id}")
