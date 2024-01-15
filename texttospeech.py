# import the pyttsx module inside program
import pyttsx4

# initializing the module
engine = pyttsx4.init()

# .say() function is used to speak the text you have written
# inside the function
engine.say("welcome back sir !!!.. what shall i do for you ?.. im ready!!!!!")

# this is used to process and run the program commands
engine.runAndWait()

