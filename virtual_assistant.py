import speech_recognition as sr
import os
from gtts import gTTS
import warnings
import datetime
import calendar
import random
import wikipedia

# Ignore any warnings
warnings.filterwarnings('ignore')


# record audio and return it as a string
def recordAudio():
    # Record the audio
    r = sr.Recognizer()  # Creating recognizer object

    # open the microphone and start recording
    with sr.Microphone() as source:
        print('Say Something!')
        audio = r.listen(source)

    # Use googles speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said ' + data)
    except sr.UnknownValueError:
        print("Google speech recognition could not understand the audio")
    except sr.RequestError as e:
        print('Request results from google speech recognition service error' + e)

    return data


# function to get the virtual assistant response
def assistantResponse(text):
    print(text)

    # convert the text to speech
    myobj = gTTS(text=text, lang='en', slow=False)

    # save the converted audio to a file
    myobj.save('assistant_response.mp3');

    # play the converted file
    os.system('start assistant_response.mp3')


# function for wake words or phrase
def wakeWord(text):
    Wake_Words = ['hey friday', 'ok friday', 'friday']

    text = text.lower()  # converts the text to all lowercase words

    # check to see if the user command/text contains a wakw word
    for phrase in Wake_Words:
        if phrase in text:
            return True

    # if the wake word is not found in the text from the loop then return false
    return False


# function to get the current date
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


# a function to return a random greeting response
def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'hello', 'greetings', 'wassup']

    # Greeting responses
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    # if the user input is a greeting , then return e randomly choosen greeting
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # if no greeting was detected then returned an empty string
    return ''


# a function to get a persons first and last names from the text
def getPerson(text):
    wordList = text.split()

    for i in range(0, len(wordList)):
        if (i + 3) <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return wordList[i + 2] + ' ' + wordList[i + 3]
    return ''

while True:

    # record the audio
    text = recordAudio()
    response = ''

    # check for the wake words
    if wakeWord(text) == True :

        # check for greetings by the user
        response = response + greeting(text)

        # check if the user wants to do anything with the date
        if 'date' in text:
            get_date = getDate()
            response = response + ' ' + get_date

        # check if the user wants to do anything with the time
        if 'time' in text:
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour > 12:
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + meridiem + '.'

        # check to see if the user said 'who is'
        if 'who is' in text:
            person = getPerson(text)
            #print(person)
            try:
                wiki = wikipedia.summary(person,sentences=2)
                response = response + ' ' + wiki
            except ValueError:
                print('Page Error ')

        # have the assistant respond back using audio
        assistantResponse(response)
