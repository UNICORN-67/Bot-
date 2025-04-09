# Redis DB connection

from redis import from_url
from bot import config

redis = from_url(config.REDIS_URI, decode_responses=True)