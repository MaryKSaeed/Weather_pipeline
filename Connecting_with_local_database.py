import psycopg2
import os
from WeatherStack_API_requset import fetch_weather_data

password = os.getenv("POSTGRES_PASSWORD")

DB_NAME = "Weather_App"
DB_USER = "postgres"
DB_PASSWORD = 'Mariam@2001'
DB_HOST = "localhost"
DB_PORT = "5432"

def insert_weather_data(city, temp, desc, wind_speed, wind_direction, pressure, humidity, feelslike, uv_index):
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        cursor = conn.cursor()
        query = "INSERT INTO weather (city, temperature, description, wind_speed, wind_direction, pressure, humidity, feelslike, uv_index) VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (city, temp, desc, wind_speed, wind_direction, pressure, humidity, feelslike, uv_index))
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Database Error: {e}")

# Fetch data and store it in the database
weather_data = fetch_weather_data()
if weather_data:
    insert_weather_data(weather_data["location"]["name"], weather_data["current"]["temperature"],
                        weather_data["current"]["weather_descriptions"][0], weather_data["current"]["wind_speed"],
                        weather_data["current"]["wind_dir"], weather_data["current"]["pressure"],
                        weather_data["current"]["humidity"], weather_data["current"]["feelslike"],
                        weather_data["current"]["uv_index"])