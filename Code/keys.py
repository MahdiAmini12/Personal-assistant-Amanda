import answer
keyItems = {'set voice': (answer.changeGender, 'woman or man'),
            'change voice': (answer.changeGender, 'woman or man'),
            'change your voice': (answer.changeGender, 'woman or man'),
            'change speed': (answer.setRate, 'increase or decrease'),
            'set name': (answer.setName, 'your Name'),
            "what's my name": (answer.whatIsMyName, None),
            "what is my name": (answer.whatIsMyName, None),
            'time': (answer.time, None),}
