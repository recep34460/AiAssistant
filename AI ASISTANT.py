import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import news_module
import pyautogui
#import instadownloader
#import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=15,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query
#pdf reader start
#def pdf_reader():
#    book = open('Level Design - In pursuit of better levels.pdf','rb')
#    pdfReader = PyPDF2.PdFileReader(book) #pip install PyPDF2
#    pages = pdfReader.numPages
#    speak(f"Total numbers of pages in this book {pages} ")
#    speak("please enter the page number i have to read")
#    pg = pdfReader.getPage(pg)
#    text = page.extractText()
#    speak(text)
#pdf reader stop
#news start
#newsapi.org
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513'

    main_page = requests.get(main_url).json()
    print (main_page)
    articles = main_page["articles"]
    print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth",]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"today's {day[i]} news is: " head[i])
        speak(f"today's {day[i]} news is: {head[i]}")
    # news stop
#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0  and hour<12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("please tell me how can I help you")

#send email
#def sendEmail(to,content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('your email id', to, content)
    #server.close()
    #send email close
def start():
    wish()
    while True:
    #if 1:
        query = takecommand().lower()
        #logic building for tasks

        if "open notepad" in query:
            speak("okay..., opening notepad")
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            speak("what should i search")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        #mesaj gonderme
        ###elif "send message" in query:
            ###kit.sendwhatmsg("+919992432188", "this is testing protocol", 2,25)
        elif "play songs on youtube" in query:
            kit.playonyt("glimpse of us")
        #sending email
        #elif "email to avi" in query:
         #   try:
          #      speak("what should i say")
           #     content = takecommand().lower()
            #    to = "avi999880@gmail.com"
             #   sendEmail(to,content)
              #  speak("Email has been sent to avi")

            #except Exception as e:
            #    print(e)
            #    speak("sorry, i am not  able to sent this mail")
            #pip install secure-smtplib #send e mail close
        elif "exit" in query:
            speak("have a good day")
            sys.exit()

        elif "close notepad" in query:
            speak("okay, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        #elif "set alarm" in query:
            #nn = int(datetime.now().hour)
            #if nn==22:
                #music_dir = 'E:\\music'
                #songs = os.listdir(music_dir)
                #os.startfile(os.path.join(music_dir,songs[0]))
        #to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
        #shutdown system
        #elif "shut down the system" in query:
            #os.system("shutdown /s /t 5")
        #restart system
        #elif "restart the system" in query:
            #os.system("shutdown /r /t 5")
        #sleep system
        #elif "sleep the system" in query:
            #os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        #speak("do you have any other work")

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait, fetching the latest news")
            news()
        #email pic sending start
        #elif "email to avinash" in query:
            #speak("sir what should i say")
            #query = takecommand().lower()
            #if "send a file with gmail" in query:
                #email = 'your@gmail.com' #your e mail
                #password = 'your_pass' #your email account password
                #send_to_email = 'person@gmail.com' #whom you are sending the message
                #speak("okay, what is the subject for this email")
                #query = takecommand().lower()
                #subject = query
                #speak("and, what is the message for this email")
                #query2 = takecommand().lower()
                #message = query2
                #speak("please enter the correct path of the file into the shell")
                #file_location = input("please enter the path here") #the file attachment in the email

                #speak("please wait,i am sending email now")

                #msg = MIMEMulitplayer()
                #msg['from'] = email
                #msg['to'] = send_to_email
                #msg['subject'] = subject

                #msg.attach(MIMEText(message, 'plain'))

                #Setup the attachment
    # email pic sending stop

    ###########################################################################################################################
    ################################################################################
    #-------------------------------- to find my location using IP Address

        #elif "where i am" in query or "where we are" in query:
            #speak("pleas wait,let me check")
            #try:
                #ipAdd = requests.get("https://api.ipify.org")
                #print(ipAdd)
                #url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                ##geo_requests = requests.get(url)
                #geo_data = geo_requests.json()
                #print(geo_data)
                #city = geo_data['country']
                #speak(f"i am not sure, but i think we are in {city} city of {country} country")
            #except Exception as e:
                #speak("sorry, Due to network issue i am not able to find where we are.")
                #pass

                #-------------------------------- to find my location using IP Address stop
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("please enter the user name correctly")
            name = input("Enter username here.")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"here is the profile of the user {name}")
            time.sleep(5)
            speak("would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                #mod = instaloader.Instaloader() #pip install instadownloader
                #mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder")
            else:
                pass
            
            #__________________________ To take screenshot
            
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("please tell me name of this screenshot")
            name = takecommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done, screenshot saved")

        #elif "read pdf" in query:
        #    pdf_reader()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d") #os module
                speak("all the files in this folder are now hidden")

            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("all the files in this folder are now visible to everyone")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok")
if __name__ == "__main__":
    start()