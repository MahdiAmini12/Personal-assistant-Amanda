import time
import psutil
import pyttsx3 as pt
from ecapture import ecapture as ec
# import subprocess
# import webbrowser
# import requests
# import json


#نمایش اطلاعات سیستم
def system_information(query):
    # نمایش درصد استفاده از CPU
    pt.speak(f"CPU usage: {psutil.cpu_percent()}%")
    print(f"CPU usage: {psutil.cpu_percent()}%")

    # نمایش درصد استفاده از حافظه RAM   
    pt.speak(f"RAM usage: {psutil.virtual_memory().percent}%")
    print(f"RAM usage: {psutil.virtual_memory().percent}%")

    # نمایش درصد شارژ باتری (در صورتی که سیستم شما با باتری کار می‌کند)
    battery = psutil.sensors_battery()
    if battery:
        pt.speak(f"Battery percent: {battery.percent}%")
        print(f"Battery percent: {battery.percent}%")
    else:
        pt.spead("The system is not running on battery power.")
        print("The system is not running on battery power.")


def battery_percent(query):
    battery = psutil.sensors_battery()
    percent = battery.percent

    print(f"Battery percent: {battery.percent}%")
    pt.speak(f"Battery percent: {battery.percent}%")



# take a photo
def takePhoto(query):
    ec.capture(0,"robo camera","img.jpg")
