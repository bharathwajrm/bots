import requests
import pyttsx4
import datetime
# Initialize the text-to-speech engine
engine = pyttsx4.init()

print("The time and date is:", datetime.datetime.now())
engine.say("The time and date is: " + str(datetime.datetime.now()))
engine.runAndWait()

print("\t\tWelcome to the Weather Forecaster!\n")
print("Getting weather report for Coimbatore.\n")

city_name = "Coimbatore"
api_key = "77bf453c318a62e1cc7cc5031277b785"  # Replace this with your API key

# Function to Get Weather Report
def get_weather_report(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        weather_summary = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]

        report = f"Weather in {city_name}: {weather_summary}. Temperature: {temperature} °C. Wind Speed: {wind_speed} km/h. Humidity: {humidity}%."

    except Exception as e:
        print("Error occurred while fetching the weather data:", e)
        report = "Error Occurred"

    return report


# Get the weather report for Coimbatore
weather_report = get_weather_report(city_name)
print(weather_report)
engine.say(weather_report)
engine.runAndWait()

