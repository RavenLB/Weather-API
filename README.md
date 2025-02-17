
# Weather API Project

This project is a weather API service built using Flask that provides weather data based on city inputs. The application fetches data from the Visual Crossing API and caches it using Redis. It includes a rate limiter to avoid abuse and offers multiple endpoints for different types of weather and air quality data.

## Features
- Current weather data for any city.
- Weather data for a custom date range.
- Air quality data for any city.
- Redis caching for improved performance.
- Flask rate limiting for API requests.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/RavenLB/Weather-API.git
cd weather-API
```

### 2. Install Required Dependencies
Create a virtual environment and install the dependencies:
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scriptsctivate  # For Windows
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add your API key for Visual Crossing API and Redis configuration:
```bash
WEATHER_API_KEY=your_api_key_here
WEATHER_URL=visual_crossing_url

REDIS_HOST=localhost
REDIS_PORT=your_redis_port

```

### 4. Run the Application
Start the Flask application:
```bash
flask run
```

The app will be available at `http://127.0.0.1:5000`.

## API Endpoints

### 1. **Get Current Weather**
**URL:** `/weather/current/<city>`

**Path Parameters:**
- `city`: The name of the city (required).

Example:
```bash
http://127.0.0.1:5000/weather/current/Amsterdam
```

### 2. **Get Weather Forecast**
**URL:** `/weather/forecast/<city>/<days>`

**Path Parameters:**
- `city`: The name of the city (required).
- `days`: Number of days in the future to forecast (1-15, required).

Example:
```bash
http://127.0.0.1:5000/weather/forecast/Amsterdam/7
```

### 3. **Get Historical Weather**
**URL:** `/weather/historical/<city>/<start>/<end>`

**Path Parameters:**
- `city`: The name of the city (required).
- `start`: Start date of the range (required, format: YYYY-MM-DD).
- `end`: End date of the range (required, format: YYYY-MM-DD).

Example:
```bash
http://127.0.0.1:5000/weather/historical/Amsterdam/2023-01-01/2023-01-07
```


## Technologies Used
- Python
- Flask
- Redis
- Visual Crossing API
- Flask Limiter

## Contributing
Feel free to fork the repository, submit issues, or create pull requests.

## License
This project is licensed under the MIT License.
