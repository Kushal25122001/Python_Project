from platform import system_alias
from sys import exception

import speech_recognition as sr
from os import system
import os
import webbrowser
from openai import OpenAI
import datetime
import subprocess, sys



# Function for chat bot
chatstr = ""
def chat(query) :
    global chatstr
    client = OpenAI(
        api_key="API Key",
    )

    chatstr += f"Kushal:{query}\n Jarvis:"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatstr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    chatstr += response["choices"][0]["text"]
    return response["choices"][0]["text"]




# Function for Artificial Intelligence
def ai(prompt) :
    client = OpenAI(
        api_key="API Key",
    )
    text =f"OpenAI response for prompt{prompt}  \n **************\n\n"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try :
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]

        if not os.path.exists("Openai") :
            os.mkdir("Openai")

        # with open(f"Openai/prompt-{random.randint(1, 4346436)}", "w") as f :
        # File name will be all word of prompt(command) after ai
        with open(f"Openai/{''.join(prompt.split('ai')[1 :]).strip()}.txt", "w") as f :
            f.write(text)

    except exception as e :
        print(e)



## Speak function to say some text
def say(text) :
    system(f"say {text}")

# take command function is taking input command from microphone
def takecommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        #r.pause_threshold = 1
        ## listen is function which take sr.microphone() as source
        audio = r.listen(source)
        try :
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e :
            return " Some Error occurred. Sorry  from jarvis"

if __name__ =='__main__' :
    print("kushal")
    say("Hello I am jarvis A.I")

    ## while loop is for taking input again and again
    while True :
        print("listening...")
        query = takecommand()

        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
                    ["google", "https://google.com"], ["facebook", "https://facebook.com"],
                    ["instagram", "https://instagram.com"]]

        # For open application
        apps = [["facetime", f"open /System/Applications/FaceTime.app"],["calculator", f"open /System/Applications/Calculator.app"],
                ["chess", f"open /System/Applications/Chess.app"], ["contact", f"open /System/Applications/Contacts.app"],
                ["notes", f"open /System/Applications/Notes.app"], ["exel", f"open /Applications/Microsoft Excel.app"]]

        # Open web sites
        for site in sites :
            if f"Open {site[0]}".lower() in query.lower() :
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        # Open system apps
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} sir...")
                os.system(app[1])

        if "open music".lower() in query.lower() :
            music_path = "/Users/kushalsamanta/Desktop/KUSHAL/MP3/Hanumankind – Big Dawgs _ Ft. Kalmi Def Jam India.mp3"
            # os.system(f"open{music_path}")



            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, music_path])

        # To know the time
        elif "the time".lower() in query.lower() :
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"sir the  time is {strfTime}")


        # Artificial Intelligence
        elif " using ai".lower() in query.lower() :
            ai(prompt= query)

        elif "jarvis quit".lower() in query.lower() :
            exit()

        elif "reset chat".lower() in query.lower() :
            chatstr = ""

        else :
            print("chatting")
            chat(query)