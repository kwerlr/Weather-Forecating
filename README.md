# Weather Forecast Website

A beautiful and interactive weather forecasting web application built with Flask and the OpenWeatherMap API. This application allows users to search for weather information by city name and displays current weather conditions along with a 5-day forecast.

![Weather Forecast Website](https://via.placeholder.com/800x400)

## Features

- **Beautiful UI**: Modern, clean interface with smooth animations and transitions
- **Dark/Light Mode**: Toggle between light and dark themes with automatic preference saving
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Current Weather Display**: Shows temperature, "feels like" temperature, weather description, and icon
- **Detailed Weather Information**: Displays humidity, wind speed, pressure, and visibility
- **5-Day Forecast**: Provides a 5-day weather forecast with high/low temperatures and weather conditions
- **Interactive Elements**: Cards with hover effects and smooth transitions for better user experience
- **Loading Animation**: Visual feedback while weather data is being fetched

## Technologies Used

- **Backend**: Python with Flask framework
- **Frontend**: HTML, CSS, JavaScript
- **API**: OpenWeatherMap API for weather data
- **Icons**: Font Awesome for UI icons
- **Weather Icons**: OpenWeatherMap icon set

## Installation

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/kwerlr/weather-forecast-website.git
   cd weather-forecast-website
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install flask requests
   ```

4. Set up your OpenWeatherMap API key:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get a free API key
   - Replace the API_KEY value in app.py with your API key or set it as an environment variable:
     ```python
     # Direct assignment (less secure)
     API_KEY = 'your_api_key_here'
     
     # Environment variable (recommended)
     # API_KEY = os.environ.get('OPENWEATHER_API_KEY')
     ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
weather-forecast-website/
│
├── app.py                  # Flask application with backend logic
├── templates/              # HTML templates
│   └── index.html          # Main page template with HTML, CSS, and JavaScript
├── static/                 # Static files (optional, for additional assets)
│   ├── css/                # CSS files (if separated from HTML)
│   ├── js/                 # JavaScript files (if separated from HTML)
│   └── img/                # Image files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Usage

1. Enter a city name in the search box
2. Click the "Get Weather" button or press Enter
3. View the current weather conditions and 5-day forecast
4. Toggle between light and dark modes using the moon/sun icon in the top-right corner

## Customization

### Changing Colors

You can customize the color scheme by modifying the CSS variables in the `:root` selector:

```css
:root {
    --primary-color: #1e3a8a;
    --secondary-color: #3b82f6;
    --accent-color: #93c5fd;
    --text-light: #f8fafc;
    --text-dark: #1e293b;
    --bg-gradient: linear-gradient(135deg, #dbeafe, #bfdbfe);
    --card-bg: rgba(255, 255, 255, 0.85);
    --shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}
```

### Adding New Features

Some ideas for extending the application:

- Add geolocation support to automatically detect the user's city
- Implement hourly forecast
- Add weather maps
- Include air quality information
- Add multiple city saving/favorites feature
- Implement weather alerts
- Add historical weather data

## API Reference

This application uses the OpenWeatherMap API:

- Current Weather Data: `api.openweathermap.org/data/2.5/weather`
- 5-Day Forecast: `api.openweathermap.org/data/2.5/forecast`

For more information, visit the [OpenWeatherMap API documentation](https://openweathermap.org/api).

## Error Handling

The application includes basic error handling:

- If a city is not found, the user will receive appropriate feedback
- API errors are caught and handled gracefully
- Loading indicators provide feedback during data fetching

## Browser Compatibility

The application works on all modern browsers:

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgements

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API
- [Font Awesome](https://fontawesome.com/) for the icons
- [Flask](https://flask.palletsprojects.com/) for the web framework

---

## Author
Vagisha Sharma
