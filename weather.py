import requests
from dotenv import load_dotenv
import os

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL= os.getenv("WEATHER_API_URL")


def get_weather(city: str, start_date: str = "today", end_date: str = None):
    """
    Fetches weather data for a given city from the Visual Crossing API.
    """
    if not WEATHER_API_KEY:
        return {"error": "Weather API key is missing."}

    if end_date:
        url = f"{WEATHER_API_URL}/{city}/{start_date}/{end_date}"
    else:
        url = f"{WEATHER_API_URL}/{city}/{start_date}"

    params = {
        "key": WEATHER_API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}