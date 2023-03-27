import utilities
import answer
import Talk

keyItems = {#answer
            'set voice': (answer.changeGender, 'woman or man'),
            'change voice': (answer.changeGender, 'woman or man'),
            'change your voice': (answer.changeGender, 'woman or man'),
            'change speed': (answer.setRate, 'increase or decrease'),
            'set name': (answer.setName, 'your Name'),
            "what's my name": (answer.whatIsMyName, None),
            "what is my name": (answer.whatIsMyName, None),
            'time': (answer.time, None),
            #utilities
            'camera': (utilities.takePhoto, None),
            'take a photo': (utilities.takePhoto, None),
            'take your photo': (utilities.takePhoto, None),
            'Display system information': (utilities.system_information, None),
            'system information': (utilities.system_information, None),
            'CPU': (utilities.system_information, None),
            'RAM': (utilities.system_information, None),
            'battery percent': (utilities.battery_percent, None),
            #Talk
            'how are you': (Talk.how, None),
            'are you ok': (Talk.how, None),
            'are you good': (Talk.how, None),
            'how is it going': (Talk.how, None),
            'thanks': (Talk.how, None),
            'thank you': (Talk.how, None),
            'who are you': (Talk.who, None),
            'what can you do': (Talk.who, None),
            'are you crazy': (Talk.crazy, None),
            'you are crazy': (Talk.youcrazy, None),
            'can I change your name': (Talk.changeAmandaName, None),
            'change your name': (Talk.changeAmandaName, None),}
