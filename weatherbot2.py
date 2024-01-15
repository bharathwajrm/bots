import requests
import pyttsx3


def get_weather(api_key, location):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": location
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "current" in data:
        weather = data["current"]
        temperature = weather["temperature"]
        weather_description = weather["weather_descriptions"][0]
        humidity = weather["humidity"]

        result = f"Weather in {location}:\n"
        result += f"Temperature: {temperature}°C\n"
        result += f"Description: {weather_description}\n"
        result += f"Humidity: {humidity}%\n"
        return result
    else:
        return "Weather data not available."


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    api_key = "070a15dfe707d0a698cad4df5909553d"
    location = input("Enter a location: ")

    weather_info = get_weather(api_key, location)
    print(weather_info)

    speak("Here is the weather information.")
    speak(weather_info)
