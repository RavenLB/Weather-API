import json
import requests
from cache import get_cached_weather, set_cached_weather
from config import config


api_key = config.WEATHER_API_KEY
weather_url = config.WEATHER_API_URL


def get_weather(city: str, start_date: str = "today", end_date: str = None):
    """
    Fetches weather data for a given city from the Visual Crossing API.
    """
    if not api_key:
        return {"error": "Weather API key is missing."}

    if not city:
        return {"error": "City name is required."}

    # Create a unique cache key that includes the date parameters
    cache_key = f"{city}:{start_date}:{end_date}"
    
    cached_data = get_cached_weather(cache_key)
    if cached_data:
        return json.loads(cached_data)

    # Remove any leading/trailing slashes and spaces from the city name
    city = city.strip().strip('/')
    
    # Construct the URL properly
    if end_date:
        url = f"{weather_url.rstrip('/')}/{city}/{start_date}/{end_date}"
    else:
        url = f"{weather_url.rstrip('/')}/{city}/{start_date}"

    print(f"Requesting URL: {url}")  # Debug line
    
    params = {
        "key": api_key,
        "unitGroup": "metric",
        "include": "days"  # Explicitly request daily data
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        weather_data = response.json()
        set_cached_weather(cache_key, json.dumps(weather_data))
        return weather_data

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch weather data: {str(e)}"}