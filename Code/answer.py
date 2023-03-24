import pyttsx3 as pt
import random
import datetime
import playsound
import cv2



gender = 0
engine = pt.init()
name = ''

engine.setProperty('voice', engine.getProperty('voices')[1].id)

with open('namesave.txt', 'r') as n:
    name = n.read()



def setName(query):
    with open('namesave.txt', 'w') as sName:
        sName.write(query)
    pt.speak(f'Ok i changed your name to {query}')


def whatIsMyName(query):
    with open('namesave.txt', 'r') as name:
        pt.speak('your name is ' + name.read())


# Amanda voice
def setRate(type):
    speed = engine.getProperty('rate')
    speed += 50 if type == 'increase' else 0
    speed -= 50 if type == 'decrease' else 0
    engine.setProperty('rate', speed)
    pt.speak('Ok im ready')


def changeGender(text):
    global gender, engine
    if ('man' in text and 'woman' not in text) or ('men' in text and 'women' not in text):
        gender = 0
        text = 'man'
    elif 'woman' in text or 'women' in text:
        gender = 1
        text = 'woman'
    engine.setProperty('voice', engine.getProperty('voices')[gender].id)
    pt.speak(f'Ok im on {text} form')


# Start greeting
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        pt.speak(f"Hello {name},Good Morning")
    elif hour >= 12 and hour < 18:
        pt.speak(f"Hello {name},Good Afternoon")
    else:
        playsound.playsound(r'ttsMP3.com_VoiceText_2023-1-4_20_41_15.mp3')

# time
def time(query):
    strTime = datetime.datetime.now()
    pt.speak(f"the time is {strTime.hour}:{strTime.minute}")


def say(text):
    pt.speak(text)
