from flask import Flask, jsonify, render_template, abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from weather import get_weather
from config import config
from datetime import datetime, timedelta

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[config.RATELIMIT_DEFAULT]
)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/weather/current/<city>", methods=["GET"])
@limiter.limit("10 per minute")
def current_weather(city):
    data = get_weather(city)
    return render_template("weather.html", data=data)

@app.route("/weather/forecast/<city>/<int:days>", methods=["GET"])
@limiter.limit("10 per minute")
def forecast_weather(city, days):
    if days < 1 or days > 15:
        abort(400, "Days must be between 1 and 15")
    
    today = datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.now() + timedelta(days=days)).strftime("%Y-%m-%d")
    data = get_weather(city, today, end_date)
    
    # Add debug logging
    print(f"Forecast data received: {data}")
    
    return render_template("forecast.html", data=data)

@app.route("/weather/historical/<city>/<start>/<end>", methods=["GET"])
@limiter.limit("5 per minute")
def historical_weather(city, start, end):
    try:
        # Add date range validation
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        
        if end_date < start_date:
            abort(400, "End date must be after start date")
            
        if (end_date - start_date).days > 30:  # Visual Crossing has limitations
            abort(400, "Date range cannot exceed 30 days")
            
        data = get_weather(city, start, end)
        print(f"Historical data received: {data}")  # Debug logging
        
        return render_template("historical.html", data=data)
    except ValueError:
        abort(400, "Invalid date format. Use YYYY-MM-DD")

@app.errorhandler(400)
def bad_request(e):
    return render_template("error.html", error=str(e)), 400

if __name__ == "__main__":
    app.run(debug=True)
