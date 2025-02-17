import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration settings for the Weather API."""
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    WEATHER_API_URL = os.getenv("WEATHER_API_URL")

    # Redis configuration
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB = int(os.getenv("REDIS_DB", 0))
    CACHE_EXPIRATION = int(os.getenv("CACHE_EXPIRATION", 12 * 60 * 60))

    # Flask Rate Limiting
    RATELIMIT_DEFAULT = "10 per minute"


config = Config()