import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')

def speak(text) :
    engine.say(text)
    engine.runAndWait()

while True :
    print('Enter the text you want me to convert into speech')
    speak('Enter the text you want me to convert into speech')
    text = input()
    if text=='' :
        speak('Enter the text')
    elif 'exit' in text.lower() or 'stop' in text.lower() :
        speak('I am shutting down.....Bye')
        break
    else :
        speak(text)

