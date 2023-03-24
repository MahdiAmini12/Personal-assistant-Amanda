import speech_recognition as sr
import answer
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


# keyItem تعریف
while True:
    try:
        query = setMic().lower()
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
