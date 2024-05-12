#!/usr/bin/env python
# coding: utf-8

# Install SpeechRecognition Module 
# (It help for speech recognition from the microphone)
# Install pyttsx3 Module 
# (It Convert Text to Speech)
# Install pywhatkit Module 
# (It use for automation)
# Install pyaudio Module 
# (With PyAudio, you can easily use Python to play and record audio on a variety of platforms,
# such as Microsoft Windows, and Apple macOS)


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from colorama import Fore


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print(Fore.GREEN+"listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if "computer" in command:
                command = command.replace("computer", "")
                print(Fore.BLUE+command)
                
    except:
        command=' '
        pass
    
    return command


def run_alexa():
    command = take_command()
    print(Fore.BLUE+command+" ?" )

    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("the current time is " + time)
    
    elif "date" in command:
        date = date.today().strftime("%d/%m/%Y")
        talk("the Today Date is " + date)
    
    elif "tell me about" in command:
        person = command.replace("tell me about", "")
        info = wikipedia.summary(person, 1)
        talk(info)
        print(Fore.CYAN+info)

    elif "your favourite artist" in command:
        talk("Mr worldwide aka pitbull")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    else:
        talk("Please! Give command to perform task")


while True:
    run_alexa()
