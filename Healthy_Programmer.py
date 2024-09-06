#-------------- HEALTHY PROGRAMMER---------------
# 9am - 5pm
# Water - Water mp3(3.5litres) -in every 40 minutes - Drank - log
# Eyes - eyes.mp3 - in every 30 minutes - Eydone - log
# Physical activity - physical.mp3 - in every 45 minutes - Exdone - log

# Pygame module to play module


from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper) :
    mixer.init()                  # init is a function of mixer to initialize
    mixer.music.load(file)
    mixer.music.play()
    while True :
        a = input()
        if a == stopper :
            mixer.music.stop()
            break

def log_now(msg) :  # To create log when drank, eydone, exdone will be done by user
    with open("mylogs.text", "a") as f :
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__' :
    # musiconloop("Water.mp3", "stop")

    init_water = time()
    init_eyes = time()
    init_exercise = time()

    watersecs = 40 * 60
    eyesecs = 30 * 60
    exsecs = 45 * 60

    while True :
        if time() - init_water > watersecs :
            print("Water drinking time. write 'drank' to stop the alarm")
            musiconloop("Water.mp3", 'drank')
            init_water = time()
            log_now("drank water at")

        if time() - init_eyes > eyesecs :
            print("Eye exercise time. write 'eydone' to stop the alarm")
            musiconloop("Eye.mp3", 'eydone')
            init_eyes = time()
            log_now("Eye exercise done at")

        if time() - init_exercise > exsecs :
            print("Physical exercise time. write 'exdone' to stop the alarm")
            musiconloop("Ex.mp3", 'exdone')
            init_exercise = time()
            log_now("Physicalexercise done at")

