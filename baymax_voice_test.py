import os
import pyttsx3
from dotenv import load_dotenv

load_dotenv()

# Set up pyttsx3 voice engine
engine = pyttsx3.init()

# Make voice slower and cleaner — easier to understand
engine.setProperty('rate', 150)    # speed — 150 is calm and clear
engine.setProperty('volume', 1.0)  # volume — max is 1.0

# Pick a voice — 0 is usually male, 1 is female on Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # change to voices[1].id for female

# Baymax speaks!
text = "Hello. I am Baymax, your personal healthcare companion. How are you feeling today?"

print(f"Baymax: {text}")
engine.say(text)
engine.runAndWait()  # waits until speaking is done

print("Done!")