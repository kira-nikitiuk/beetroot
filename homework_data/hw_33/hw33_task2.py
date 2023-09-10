# Task 3
# The Weather app
# Write a console application which takes as an input a city name and returns current weather 
# in the format of your choice. For the current task, you can choose any weather API or website 
# or use openweathermap.org 

import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"  
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        try:
            data = response.json()
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            return f"Weather in {city_name}: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        except requests.exceptions.RequestException as e:
            return f"Error decoding response: {e}"
    else:
        return f"Error fetching weather data. Status code: {response.status_code}"

def main():
    api_key = "e37180871cff1c1ac61f4b5b2bea6ad0"  
    city_name = input("Enter city name: ")
    weather_info = get_weather(city_name, api_key)
    print(weather_info)

if __name__ == "__main__":
    main()
