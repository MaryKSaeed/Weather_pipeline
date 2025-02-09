import schedule
import time
from WeatherStack_API_requset import fetch_weather_data
from Connecting_with_local_database import insert_weather_data

def job():
    print("Fetching and storing weather data...")
    weather_data = fetch_weather_data()
    if weather_data:
        insert_weather_data(weather_data["location"]["name"], weather_data["current"]["temperature"],
                        weather_data["current"]["weather_descriptions"][0], weather_data["current"]["wind_speed"],
                        weather_data["current"]["wind_dir"], weather_data["current"]["pressure"],
                        weather_data["current"]["humidity"], weather_data["current"]["feelslike"],
                        weather_data["current"]["uv_index"])

# Run the job every hour
schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking again
