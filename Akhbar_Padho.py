# 000da90870d94423b68ad0961e4f4ec7  -> NEWS API CODE

import requests
import json

def speak(str) :
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.speak(str)

if __name__ == '__main__' :
    speak("Kaise ho kushal vai")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=000da90870d94423b68ad0961e4f4ec7"