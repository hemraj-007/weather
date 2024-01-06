import requests
import json

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        data = response.json()
        if data:
            main = data.get('main', {})
            weather = data.get('weather', [{}])[0]
            wind = data.get('wind', {})

            temperature = main.get('temp')
            weather_description = weather.get('description')
            wind_speed = wind.get('speed')

            print(f"Weather in {city.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {weather_description}")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("No data available for this location.")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Main program
if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "96843249949b893169b77a486efe9585" 
    get_weather(city, api_key)
