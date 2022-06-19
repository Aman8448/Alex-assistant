from ast import Return
from importlib.resources import path
from multiprocessing.connection import Client
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import flask
import os
import random
import time
import pywhatkit
import sys
import pyaudio
import webbrowser
import random





try:
    app = wolframalpha.Client("KJHKQT-AWGL28T78H")
except Exception:
    print("Some Network issues...")

print("ALEXA IS ONLINE...")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # it is used to check voices


def speak(audio):
    engine.say(audio)  # this function is used to say something
    engine.runAndWait()  # this function is used to search and wait


def wishtome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morining  sir...")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon  sir...")
    else:
        speak("good evening  Sir....")
    speak("hello,i am your Assistant, What can i do for u sir!...")


def TakeCommand():
    # It takes microphone input from user and returns string outpt

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # this is used to give a sec to user , to spaeak before complete listening by user>........
        # r.energy_threshold = 800
        audio = r.listen(source)

    try:
        print("recogniting...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")

    
    except Exception as e:
       # print (e)
       
        print('say that again please sir')
        speak('say that again please sir')
        return "None"
    return query


# this is a main funtion... this is used call the function ..
if __name__ == "__main__":
    wishtome()
    while True:
        
        query = TakeCommand().lower()


# logic for executing tools. based on query..
        if ' wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipidia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            print('I am fine Sir, Thank you')
            speak('I am fine Sir, Thank you')

        elif 'can we talk' in query:
            print('yes,Sure sir..')
            speak('yes,Sure sir..')

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open whatsapp' in query:
            webbrowser.open("www.whatsapp.com")

       
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")


        elif 'what' in query or 'where' in query or  'who' in query or 'which' in query or 'how' in query or 'in which' in query or 'how many' in query or 'how much' in query or 'of' in query :
            try:
                res=app.query(query)
                ans=next(res.results).text
                print(ans)
                speak(ans)
            except Exception as e:
                print (e)
            

        elif  'say that again please sir' in query:
            pass
            

        elif 'open google' in query:
            print("Sir.what should i search on Google..")
            speak("Sir.what should i search on Google..")
            G=TakeCommand().lower()
            webbrowser.open(G)
            print(G)
            speak(G)


        elif 'open music' in query:
             # to give a path for cpmmand to execute form os
             musicdir = 'D:\songs\soft song'
             songs = os.listdir(musicdir)
            # below line , we will use random function for choose randomly song play..
            #os.startfile(os.path.join(musicdir,song[0]))
             choice = random.choice(songs)   
             os.startfile(os.path.join(musicdir, choice))
             print(choice)
           

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # for showing time with AM and PM ................
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(strTime)
            speak(" sir,the time is:"+strTime)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing'+song)
            pywhatkit.playonyt(song)

        elif 'open notepad' in query:
            # path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
            path="c:\\windows\\System32\\notepad.exe"
            os.startfile(path)

        elif 'open command prompt' in query:
            os.system("start cmd")

        # elif 'open camera' in query:
        #     cap=cv2.VideoCapture(0)
        #     while True:
        #         ret,img = cap.read()
        #         cv2.inshow('webcam',img)
        #         k=cv2.waitkey(50)
        #         if k==27:
        #             break;
        #     cap.release()
        #     cv2.destroyAllWindows()
            

        elif 'open calculator' in query:
            os.system("start calculator")

        
        elif 'no thanks' in query or 'bye' in query or 'abort' in query or 'exit' in query:
            speak("THANKS FOR USING ME SIR,HAVE A GOOD DAY")
            print("THANKS FOR USING ME SIR,HAVE A GOOD DAY")
            sys.exit()
        speak("sir,do you have any other works..")
