from turtle import *
import pyttsx3 as pt
import time

pt.speak('Amanda is loading')

def drawText(text, x, y, size=20):
    penup()
    goto(x, y)
    pendown()
    write(text, align='center', font=('Arial', size, 'bold'))

def startAnimation():
    bgcolor('black')
    color('cyan')
    speed(15)
    right(45)

    for i in range(150):
        circle(30)
        if 7 < i < 62:
            left(5)
        if 80 < i < 133:
            right(5)
        if i < 80:
            forward(10)
        else:
            forward(5)
            
    drawText("Amanda M1 ...", x=0, y=-150)
    time.sleep(2)
    bye()

startAnimation()
