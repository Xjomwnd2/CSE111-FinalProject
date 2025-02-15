# weather_data.py
import requests
from datetime import datetime
def get_weather_data(city, api_key):
    """
    Retrieve weather data for a specified city using the OpenWeatherMap API.
    
    Parameters:
        city (str): Name of the city
        api_key (str): OpenWeatherMap API key
        
    Returns:
        dict: Weather data if successful, None if request fails
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error retrieving data: {e}")
        return None
def parse_weather_data(weather_data):
    """
    Parse the raw weather data into a more readable format.
    
    Parameters:
        weather_data (dict): Raw weather data from API
        
    Returns:
        dict: Parsed weather information
    """
    if not weather_data:
        return None
        
    try:
        return {
            "city": weather_data["name"],
            "temperature": round(weather_data["main"]["temp"], 1),
            "humidity": weather_data["main"]["humidity"],
            "description": weather_data["weather"][0]["description"],
            "wind_speed": weather_data["wind"]["speed"],
            "timestamp": datetime.fromtimestamp(weather_data["dt"]).strftime("%Y-%m-%d %H:%M:%S")
        }
    except KeyError as e:
        print(f"Error parsing data: {e}")
        return None
def format_weather_report(parsed_data):
    """
    Format the parsed weather data into a readable string.
    
    Parameters:
        parsed_data (dict): Parsed weather data
        
    Returns:
        str: Formatted weather report
    """
    if not parsed_data:
        return "Unable to generate weather report due to missing or invalid data."
        
    return f"""Weather Report for {parsed_data['city']}
Timestamp: {parsed_data['timestamp']}
Temperature: {parsed_data['temperature']}°C
Humidity: {parsed_data['humidity']}%
Conditions: {parsed_data['description'].capitalize()}
Wind Speed: {parsed_data['wind_speed']} m/s
"""
def main():
    # Replace with your actual API key from OpenWeatherMap
    API_KEY = "1a6855758b64435ee5c6fe73400920a5"
    city = input("Eldoret: ")
    
    # Get the weather data
    raw_data = get_weather_data(city, API_KEY)
    if raw_data:
        # Parse the data
        parsed_data = parse_weather_data(raw_data)
        if parsed_data:
            # Format and display the report
            print(format_weather_report(parsed_data))
        else:
            print("Error: Could not parse weather data.")
    else:
        print("Error: Could not retrieve weather data.")
if __name__ == "__main__":
    main()

