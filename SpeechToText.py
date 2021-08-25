import speech_recognition as sr
from gtts import  gTTS
import os

def recordAudio() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('Say Something')
        audio = r.listen(source)

        data=''
        try :
            data = r.recognize_google(audio)
        except sr.UnknownValueError :
            print('Google speech recognition cannot understand the audio.')
        except sr.RequestError :
            print('Request results from Google speech recognition error')
        return data

while True :
    text = recordAudio()
    if 'exit' in text.lower() :
        break
    print(text)