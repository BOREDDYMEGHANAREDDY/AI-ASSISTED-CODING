import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

def get_weather_data(city_name):
    """
    Fetch weather data from OpenWeatherMap API using environment variable for API key.
    
    Args:
        city_name (str): Name of the city to get weather for
        
    Returns:
        dict: Weather data if successful, None otherwise
    """
    
    # Retrieve API key from environment variable
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    # Error handling: Check if API key is set
    if api_key is None:
        print("Error: OPENWEATHER_API_KEY environment variable not set.")
        print("Please set the API key in your .env file or system environment variables.")
        return None
    
    # API endpoint
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use Celsius
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params, timeout=5)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse and return the JSON response
        weather_data = response.json()
        return weather_data
        
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the weather API. Check your internet connection.")
        return None
        
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
        return None
        
    except requests.exceptions.HTTPError as e:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your OPENWEATHER_API_KEY.")
        elif response.status_code == 404:
            print(f"Error: City '{city_name}' not found.")
        else:
            print(f"Error: HTTP {response.status_code} - {response.reason}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        return None
        
    except ValueError:
        print("Error: Invalid JSON response from API.")
        return None


def display_weather(weather_data):
    """
    Display weather information in a readable format.
    
    Args:
        weather_data (dict): Weather data from the API
    """
    
    if weather_data is None:
        return
    
    try:
        # Extract relevant weather information
        city = weather_data.get('name')
        country = weather_data.get('sys', {}).get('country')
        temperature = weather_data.get('main', {}).get('temp')
        feels_like = weather_data.get('main', {}).get('feels_like')
        humidity = weather_data.get('main', {}).get('humidity')
        description = weather_data.get('weather', [{}])[0].get('description')
        wind_speed = weather_data.get('wind', {}).get('speed')
        pressure = weather_data.get('main', {}).get('pressure')
        
        # Display the weather information
        print("\n" + "="*50)
        print(f"Weather Information for {city}, {country}")
        print("="*50)
        print(f"Temperature: {temperature}°C (feels like {feels_like}°C)")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Conditions: {description.capitalize()}")
        print("="*50 + "\n")
        
    except KeyError as e:
        print(f"Error: Missing expected data field: {str(e)}")
    except Exception as e:
        print(f"Error: Failed to display weather data: {str(e)}")


def main():
    """Main function to run the weather application."""
    
    print("Weather Data Fetcher Application")
    print("-" * 50)
    
    # Get city name from user input
    city_name = input("Enter city name: ").strip()
    
    # Validate user input
    if not city_name:
        print("Error: City name cannot be empty.")
        return
    
    print(f"\nFetching weather data for {city_name}...")
    
    # Fetch weather data
    weather_data = get_weather_data(city_name)
    
    # Display the weather information
    if weather_data:
        display_weather(weather_data)
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    main()
