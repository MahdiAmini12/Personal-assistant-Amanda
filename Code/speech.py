import speech_recognition as sr
import pyttsx3  as  pt
import startAnimation
import utilities
import answer
import Talk
import keys 


# Recognizer voice
def setMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print(query)
    return query

# input name
def name():
    with open('namesave.txt', 'r') as name:
        if name.read():
            answer.wishMe()
        else:
            answer.say('hi this is your personal assistant Amanda')
            answer.say(
                'But ,      But i dont know you , please give me your Name: ')
            name = setMic().lower()
            answer.setName(name)


name()

# keyItem تعریف
while True:
    try:
        query = setMic().lower()
        if "stop program" in query or "stop the program" in query or "stop Amanda" in query or "stop the Amanda" in query or "Amanda stop" in query or "exit program" in query or "exit the program" in query:
            pt.speak('Exiting the program') 
            print("Exiting...")
            break
        for keyEl in keys.keyItems:
            if keyEl in query:
                if keys.keyItems[keyEl][1]:
                    answer.say(f'tell me {keys.keyItems[keyEl][1]}')
                    ans = setMic().lower()
                    keys.keyItems[keyEl][0](ans)
                else:
                    keys.keyItems[keyEl][0](query)
    except Exception as e:
        print(e)
