import insta
from texttospeech import pyttsx4
import track
# Get the username from the 'insta' module (assuming it provides a variable named 'usrname')
username = insta.usrname

# Ask the user to enter a username
input_username = input("Enter username: ")

# Check if the entered username matches the 'insta' username
if input_username == username:
    print("Insta completed!")
else:
    print("Invalid!")

# Get the phone number from the 'track' module (assuming it provides a variable named 'phone_number')
tracked_phone_number = track.phone_number

# Print the phone number
print("Tracked phone number:", tracked_phone_number)

# Check if the phone number was successfully tracked
if tracked_phone_number:
    print("Tracking completed!")
else:
    print("Invalid!")

# Say "completed!!!!" using text-to-speech
engine = pyttsx4.init()
engine.say("completed!!!!")
engine.runAndWait()

