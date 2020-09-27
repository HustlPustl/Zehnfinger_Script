import time
import keyboard
text=""""""
time.sleep(5)
print("Keybord Eingabe startet, bitte warten")
keyboard.write(text)
dot="."
strlen=1
apm=0
for c in text:
    strlen+=1 
zeit=0.02
while 1:
    apm=strlen*60/zeit
    zeit+=0.02
    time.sleep(0.02)
    if apm < 670:
        print("Eingabe zuenden")
        keyboard.write(dot)
        break
