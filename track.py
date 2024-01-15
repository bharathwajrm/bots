import requests
import pyttsx3

API_KEY = "59c3fa3f397a119873a0ab1efc9a3431"

def track_phone_location(phone_number):
    # API endpoint URL
    endpoint = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={phone_number}&country_code=&format=1"

    try:
        # Send the API request
        response = requests.get(endpoint)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()

            # Check if the number is valid
            if data["valid"]:
                # Get the location information
                country = data["country_name"]
                location = data["location"]
                carrier = data["carrier"]

                # Print the tracked information
                print("Phone number:", phone_number)
                print("Location:", location)
                print("Country:", country)
                print("Carrier:", carrier)

                # Initialize the text-to-speech engine
                engine = pyttsx3.init()
                engine.say("Phone number: " + phone_number)
                engine.say("Location: " + location)
                engine.say("Country: " + country)
                engine.say("Carrier: " + carrier)
                engine.runAndWait()

            else:
                print("Invalid phone number!")

        else:
            print("Error occurred while making the API request.")

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

# Get user input for the phone number
phone_number = input("Enter the phone number to track (including country code): ")

# Call the function with user input
track_phone_location(phone_number)
