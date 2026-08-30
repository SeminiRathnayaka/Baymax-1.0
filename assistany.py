import cv2
import pyttsx3
import speech_recognition as sr
import datetime

# Text to Speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Voice Recognition
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        return ""

# Face Detection
face = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    'haarcascade_frontalface_default.xml'
)

camera = cv2.VideoCapture(0)

speak("Assistant started.")

while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("AI Assistant", frame)

    command = listen()

    if "hello" in command:
        speak("Hello! Nice to see you.")

    elif "time" in command:
        current = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current}")

    elif "exit" in command:
        speak("Goodbye!")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()