import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import time
import webbrowser
import pywhatkit as kit
import smtplib
import sys



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voices", voices[1].id)


#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#converts voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}")

    except Exception as e:
        speak("say that again sir...")
        return "None"
    return query

#to WISH
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning mister patel")
    elif hour>=12 and hour<18:
        speak("Good afternoon mister patel")
    else:
        speak("Good Evening mister patel")
    speak("This is Jarvis how can i help you?")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your email id", "your password")
    server.sendmail("your email id", to, content)
    server.close()
if __name__ == "__main__":
    #speak("hello papa")
    #takecommand()
    wish()
    while True:
    #if 1:
        query = takecommand().lower()

        #logic building for task

        if "open notepad" in query:
            npath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Notepad.lnk"
            os.startfile(npath)

        elif "open the camera" in query:
            speak("sure sir")
            cap = cv2.VideoCapture(0)
            count=1
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam",img)
                k = cv2.waitKey(50)
                if count==1:
                    speak("2 rupee ki pepsi mera bhai sexy")
                    count-=1
                if k == 7:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play me a song" in query:
            music_dir = r'C:\Users\AYAZ PATEL\Music'
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            #os.startfile(os.path.join(music_dir, rd))

            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("please wait sir am working on it.......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("Your request is in process sir...")
            webbrowser.open("www.youtube.com")
            time.sleep(4)

        elif "open facebook" in query:
            speak("am working on your request sir please wait.... ")
            webbrowser.open("www.facebook.com")
            time.sleep(4)

        elif "open google" in query:
            speak("am opening google sir please wait... ")
            #cd = takecommand().lower()
            webbrowser.open("www.google.com")
            #webbrowser.open(f"{cd}")
            time.sleep(4)

        elif "message srikant" in query:
            speak("sure sir am working on it please wait.... ")
            kit.sendwhatmsg("+917676767981","kaisan baa",19,20)

        elif "my song" in query:
            speak("sure sir...")
            kit.playonyt("libaas")
            time.sleep(5)
            speak("enjoy sir")
            time.sleep(2)

        elif "shrikant patil" in query:
            speak("shrikanth patil is your friend and he is huli, that is tiger of basavakalyan")

        elif "9" in query:
            speak("jaheera bee hamare dadi ammi hain, toglor maen 9 acer khet liye uno")

        elif "email" in query:
            try:
                speak("what should i say?")
                time.sleep(4)
                content = takecommand().lower()
                time.sleep(2)
                to = "karan314.k@gmail.com"
                sendEmail(to,content)
                speak("email has been send to karan")

            except Exception as e:
                print(e)

        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day.")
            sys.exit()
        speak("sir do you have any other work? ")

