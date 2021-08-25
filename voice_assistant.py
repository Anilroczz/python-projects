import speech_recognition as sr
import pyttsx3
import wikipedia
#from ecapture import ecapture as ec
import datetime
import os
import time
import webbrowser
import subprocess
import json
import requests
import wolframalpha
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12 :
        speak("Good Morning Boss")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon Boss")
        print("Hello,Good Afternoon")
    else :
        speak("Good Evening Boss")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said '+text)
        except Exception as e :
            speak('Pardon me, please say that again')
            return 'none'
        return text

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # eg Friday
    monthNum = now.month
    dayNum = now.day

    # list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    # list of ordinal numbers
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th',
                      '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th',
                      '28th', '29th'
        , '30th', '31st']

    return 'Today is ' + weekday + ' the ' + ordinalNumbers[dayNum - 1] + ' of ' + month_names[monthNum - 1] + '.'


print('Loading your AI personal assistant Jarvis')
speak('Loading your AI personal assistant Jarvis')
wishMe()

while True :
    speak("How can i help u now...?")
    text = takeCommand().lower()

    if text == 'none' :
        continue

    if 'bye' in text or 'exit' in text or 'stop' in text or 'shut down' in text:
        speak("your personal assistant Jarvis is shutting down,see ya boss")
        print("Jarvis is shutting down,Good bye")
        break

    elif 'open youtube' in text:
        webbrowser.open_new_tab("https://www.youtube.com")
        speak("youtube is open now")
        time.sleep(5)

    elif 'open google' in text:
        webbrowser.open_new_tab("https://www.google.com")
        speak("Google chrome is open now")
        time.sleep(5)

    elif 'open gmail' in text:
        webbrowser.open_new_tab("gmail.com")
        speak("Google Mail open now")
        time.sleep(5)
    elif 'time' in text:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    elif 'date' in text:
        speak(getDate())
    elif 'search' in text:
        text = text.replace("search", "")
        webbrowser.open_new_tab(text)
        time.sleep(5)
    elif 'ask' in text:
        speak('I can answer to computational and geographical questions  and what question do you want to ask now')
        question = takeCommand()
        app_id = "HYYX2R-PXLEX9G6KP"
        client = wolframalpha.Client('HYYX2R-PXLEX9G6KP')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)
    elif 'who are you' in text or 'what can you do' in text:
        speak('I am Jarvis 1 point O your personal assistant. I am programmed to minor tasks like'
              'opening youtube,google chrome and gmail ,predict time and date '
              'and you can ask me computational or geographical questions too!')


    elif 'who made you' in text or "who created you" in text or "who discovered you" in text:
        speak("I was built by My boss Anil Kumar")
        print("I was built by My boss Anil Kumar")

    else :
        speak(text)

