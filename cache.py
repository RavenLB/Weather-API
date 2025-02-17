import redis
from config import config

REDIS_HOST = config.REDIS_HOST
REDIS_PORT = config.REDIS_PORT
REDIS_DB = config.REDIS_DB
CACHE_EXPIRATION = config.CACHE_EXPIRATION

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

def get_cached_weather(key: str):
    """Retrieve weather data from Redis cache."""
    try:
        return redis_client.get(key)
    except redis.RedisError as e:
        print(f"Redis error: {e}")  # Debug logging
        return None

def set_cached_weather(key: str, data: str):
    """Store weather data in Redis cache."""
    try:
        redis_client.setex(key, CACHE_EXPIRATION, data)
    except redis.RedisError as e:
        print(f"Redis error: {e}")  # Debug logging