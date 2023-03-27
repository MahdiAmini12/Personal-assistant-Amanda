import pyttsx3 as pt
import random


def how(query):
    listOfAnswers = ['thanks , iam fine', 'Just great! Thanks for asking. You can also ask for my help. Try something like, take photo.', 'Im happy its good day!','Im fine and dandy and ready to be handy. Try asking, "What can you do?"', 'Great, thanks. To learn how I can help, ask, "What can you do?"', 'Im doing well how are you?']

    char = random.choice(listOfAnswers)
    if 'thanks' in query or 'thank you' in query:
        char = 'your wellcome'
    pt.speak(char)

def who(query):
    pt.speak('I am Amanda version M1 point O your personal assistant. I am     programmed to minor tasks like'
    'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
    'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

def crazy(query):
    listOfAnswers = ['My self-characterization is a little different.', 'Im going to pretend I didnt hear that.']

    char = random.choice(listOfAnswers)
    pt.speak(char)

def youcrazy(query):
    pt.speak('I didnt catch that, but it sounds like youre frustrated. To learn about my functions, try asking, "What can you do?"')

def changeAmandaName(query):
    pt.speak('Nah. I like being Amanda.')
