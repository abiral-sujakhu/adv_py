import requests
from datetime import datetime

# Replace with your actual API key from OpenWeather
API_KEY = "444b0e4e96bd4d531b186eb390aebaf4"

# City and country code
city = "New York"
country_code = "US"

# API endpoint for 5-day forecast
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&appid={API_KEY}&units=metric"

try:
    # Make the API request
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status codes
    
    data = response.json()
    
    print("=" * 60)
    print(f"📍 Weather Forecast for {city}, {country_code}")
    print("=" * 60)
    
    # Display forecast data
    print(f"\nCity: {data['city']['name']}")
    print(f"Country: {data['city']['country']}")
    print(f"Timezone: UTC{data['city']['timezone']//3600:+d}")
    print(f"\nTotal forecast entries: {data['cnt']}")
    
    print("\n" + "=" * 60)
    print("5-DAY TEMPERATURE FORECAST")
    print("=" * 60)
    
    # Group forecasts by day
    daily_temps = {}
    
    for forecast in data['list']:
        # Convert timestamp to readable date
        dt = datetime.fromtimestamp(forecast['dt'])
        date = dt.strftime('%Y-%m-%d')
        time = dt.strftime('%I:%M %p')
        
        temp = forecast['main']['temp']
        feels_like = forecast['main']['feels_like']
        description = forecast['weather'][0]['description']
        
        # Group by date
        if date not in daily_temps:
            daily_temps[date] = []
        
        daily_temps[date].append({
            'time': time,
            'temp': temp,
            'feels_like': feels_like,
            'description': description
        })
    
    # Display organized by day
    for date, forecasts in daily_temps.items():
        print(f"\n📅 {date}")
        print("-" * 60)
        
        temps = [f['temp'] for f in forecasts]
        max_temp = max(temps)
        min_temp = min(temps)
        
        print(f"   Max: {max_temp:.1f}°C | Min: {min_temp:.1f}°C")
        print()
        
        for forecast in forecasts:
            print(f"   {forecast['time']:>8} | {forecast['temp']:>5.1f}°C | {forecast['description']}")

except requests.exceptions.HTTPError as e:
    if response.status_code == 401:
        print("❌ ERROR: Invalid API Key!")
        print("Please sign up at https://openweathermap.org/api to get your API key")
        print("Then replace 'YOUR_API_KEY_HERE' in the code with your actual key")
    else:
        print(f"❌ HTTP Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"❌ Request Error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
