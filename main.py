import requests
import time
import webbrowser
import winsound
import keyboard
import datetime
from bs4 import BeautifulSoup
import pyttsx3

engine = pyttsx3.init()

test_url = "https://in.bookmyshow.com/kochi/movies/doctor-strange-in-the-multiverse-of-madness/ET00310791"

test_string = "Book tickets"


def checking_function():
    r = requests.get(test_url)
    soup = BeautifulSoup(r.content,'html.parser')
    if test_string in soup.text:
        print("booking started")
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        engine.say("Booking open. Press Q to open book my show")
        print("Press Q to open bookmyshow")
        engine.runAndWait()
    else:
        print("booking not started")

while True:
    time.sleep(3)
    print(datetime.datetime.now())
    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        webbrowser.open(
            test_url,
            new=2)
        print('You Pressed Q!')
        break  # finishing the loop
    else:
        pass
    checking_function()