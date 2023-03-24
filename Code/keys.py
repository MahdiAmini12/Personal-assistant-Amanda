import answer
import utilities

keyItems = {'set voice': (answer.changeGender, 'woman or man'),
            'change voice': (answer.changeGender, 'woman or man'),
            'change your voice': (answer.changeGender, 'woman or man'),
            'change speed': (answer.setRate, 'increase or decrease'),
            'set name': (answer.setName, 'your Name'),
            "what's my name": (answer.whatIsMyName, None),
            "what is my name": (answer.whatIsMyName, None),
            'time': (answer.time, None),
            'camera': (utilities.takePhoto, None),
            'take a photo': (utilities.takePhoto, None),
            'take your photo': (utilities.takePhoto, None),
            'Display system information': (utilities.system_information, None),
            'system information': (utilities.system_information, None),
            'CPU': (utilities.system_information, None),
            'RAM': (utilities.system_information, None),
            'Battery percent': (utilities.system_information, None)}
