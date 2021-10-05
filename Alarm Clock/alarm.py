import os
import datetime
from playsound import playsound


os.system('cleart')

heheH = int(input("input Hour > "))
heheM = int(input("input Minutes > "))
amPm = str(input("input Am or PM > "))

os.system('cleart')
print("Waiting for alarm to play in ", heheH, heheM, amPm)
if (amPm == "pm"):
    heheH = heheH + 12
    while (1==1):
        if (heheH == datetime.datetime.now().hour and 
                heheM == datetime.datetime.now().minute) :
                print("Time to wake up")
                playsound('sound.wav') 
                playsound('sound.wav')
                playsound('sound.wav') 
                playsound('sound.wav')
                playsound('sound.wav')
                break
