from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import os

app = Flask(__name__)

API_KEY = '00207f9a16cbfbbf8f3bf05a01e74cf8'  # Better to use environment variables for API keys


# API_KEY = os.environ.get('OPENWEATHER_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        current_weather_data = get_current_weather(city)
        forecast_data = get_forecast(city)
        return render_template('index.html', current_weather_data=current_weather_data, forecast_data=forecast_data)
    return render_template('index.html', current_weather_data=None, forecast_data=None)


def get_current_weather(city):
    """Get current weather data for a city."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_forecast(city):
    """Get 5-day forecast for a city with improved data processing."""
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the forecast data to get daily summaries
        daily_forecast = {}
        for entry in data['list']:
            date_time = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
            date = date_time.strftime('%Y-%m-%d')
            formatted_date = date_time.strftime('%a, %b %d')  # Format: Mon, Jan 01

            # For each date, track icon, description, max and min temps
            if date not in daily_forecast:
                daily_forecast[date] = {
                    'temp_min': entry['main']['temp_min'],
                    'temp_max': entry['main']['temp_max'],
                    'description': entry['weather'][0]['description'],
                    'icon': entry['weather'][0]['icon'],
                    'formatted_date': formatted_date,
                    'humidity': entry['main']['humidity'],
                    'wind_speed': entry['wind']['speed']
                }
            else:
                daily_forecast[date]['temp_min'] = min(daily_forecast[date]['temp_min'], entry['main']['temp_min'])
                daily_forecast[date]['temp_max'] = max(daily_forecast[date]['temp_max'], entry['main']['temp_max'])

                # Use noon data for the icon and description if available (more representative)
                if '12:00:00' in entry['dt_txt']:
                    daily_forecast[date]['description'] = entry['weather'][0]['description']
                    daily_forecast[date]['icon'] = entry['weather'][0]['icon']

        # Sort by date and limit to 5 days
        sorted_forecast = {}
        for i, (date, data) in enumerate(sorted(daily_forecast.items())):
            if i >= 5:  # Limit to 5 days
                break
            sorted_forecast[data['formatted_date']] = {
                'temp_min': data['temp_min'],
                'temp_max': data['temp_max'],
                'description': data['description'],
                'icon': data['icon'],
                'humidity': data['humidity'],
                'wind_speed': data['wind_speed']
            }

        return sorted_forecast
    return None


# Add a route for AJAX requests if you want to make the site more interactive
@app.route('/api/weather', methods=['GET'])
def api_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    current_weather = get_current_weather(city)
    forecast = get_forecast(city)

    if current_weather is None:
        return jsonify({'error': 'City not found'}), 404

    return jsonify({
        'current_weather': current_weather,
        'forecast': forecast
    })


if __name__ == '__main__':
    app.run(debug=True)
