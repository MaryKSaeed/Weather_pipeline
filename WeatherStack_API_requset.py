import requests
import os

API_KEY = os.getenv("WEATHERSTACK_API_KEY")  # Get the API key from the environment
URL = f"https://api.weatherstack.com/current?access_key={API_KEY}" # Historical weather data API endpoint
querystring = {"query":"Cairo"} # Query parameters

# Function to fetch weather data from the API
def fetch_weather_data():
    try:
        response = requests.get(URL, params=querystring) # Send a GET request to the API
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json() # Parse the JSON data into a Python dictionary
        return data
    except requests.exceptions.RequestException as e: # Catch any request exception errors
        print(f"API Request Failed: {e}") # Print the error
        return None

weather_data = fetch_weather_data()
print(weather_data)