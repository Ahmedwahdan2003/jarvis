import pyttsx3
import speech_recognition as sr
import subprocess
import webbrowser
import pywhatkit as wp
from datetime import datetime
import time
import os

# Initialize recognizer and keywords    
now = datetime.now()
r = sr.Recognizer()
keywords = [("jarvis", 1), ("hey jarvis", 1)]
source = sr.Microphone()
whatsapp = [("mama", "01116877464"),]
# Function to speak text
#we here use the pytts library to convert text to speech
def speak(text):
    rate = 100
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', rate + 75)
    engine.say(text)
    engine.runAndWait()


# Callback function for speech recognition
#this function recognize what you say and convert it into text then when jarvis wakes up it calls the recognize_main fun 
def callback(recognizer, audio):
    try:
        speech_as_text = recognizer.recognize_sphinx(audio, keyword_entries=keywords)
        print(speech_as_text)
        if "jarvis" in speech_as_text or "hey jarvis" in speech_as_text:
            speak("Welcome back master ahhmmeddd... How can I help you?")
            recognize_tasks()
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
        speak("Sorry, sir. Can you repeat that again?")



# Function to start the recognizer
def start_recognizer():
    print("Waiting for a keyword... 'jarvis' or 'Hey jarvis'")
    r.listen_in_background(source, callback)  #begin recognizing and when it hears wake up keyword it calls the callback function 
    input("Press Enter to stop the recognizer.")


# Main function||| for recognition and performing the tasks
#ADD TASKS HERE\|/
def recognize_tasks():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    data = ""
    try:
        data = r.recognize_google(audio)
        data = data.lower()
        print("You said: " + data)
        if "how are you" in data:
            speak("Never been better, sir.")
        elif "hello" in data:
            speak("Hi there.")
        elif "open google" in data:
            webbrowser.open_new('http://google.com')
        elif "go to sleep" in data:
            speak("Okay, goodnight sir.")
            exit()
        elif "send the message to m" in data: 
            wp.sendwhatmsg("+201112187775", "Hey im jarvis just saying hi", datetime.now().hour,(datetime.now().minute+1),10,True,2)
        elif "vs" in data:
            subprocess.Popen('"C:\\Users\\wahda\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"')
        else:
            speak("I'm sorry, sir. I did not understand your request.")
    except sr.UnknownValueError:
        print("Jarvis did not understand your request")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))


# Main program
if __name__ == '__main__':
    start_recognizer()
