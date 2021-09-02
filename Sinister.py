import pyttsx3
import speech_recognition as sr
import datetime
import os
import os.path
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyautogui
import time
import pyjokes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import PyPDF2
from GoogleNews import GoogleNews
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import psutil
import json
from selenium import webdriver
from time import sleep
from twilio.rest import Client
from speedtest import Speedtest
import ctypes
import winshell
import wolframalpha
import subprocess
import numpy as np
import wikipedia as googleScrap
import operator
import sounddevice
from scipy.io.wavfile import write


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[-1].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 175)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1.5
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print("Recognizing..")
        command = r.recognize_google(audio, language='en-us')
        print(f"Master said: {command}")

    except Exception as q:
        return "none"
    return command


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"Good Morning Sir/Ma'am. Its {tt}")
    elif hour>12 and hour<18:
        speak(f"Good Afternoon Sir/Ma'am. Its {tt}")
    else:
        speak(f"Good Evening Sir/Ma'am. Its {tt}")
    speak("I am your virtual voice assistant , how can I help you..")


def CommandExecution():
    wish()

    while True:

        command = takecommand().lower()

        # logic building for tasks

        if "open notepad" in command:
            speak("Okay sir, initiating notepad")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open microsoft edge" in command:
            speak("Okay sir, initiating Edge")
            apath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(apath)

        elif "i want to play some games" in command or "I want to play some games" in command:
            speak("Okay sir, which game do you want to play?")
            speak("You currently have 6 games to play which are - Counter Strike , IGI , IGI2 , Minecraft , KSP , GTA San Andreas")
            game = takecommand().lower()
            if "counter strike" in game:
                speak("Enjoy your game sir I am going to sleep")
                spath = "C:\Games\Counter-Strike 1.6\Counter-Strike.exe"
                os.startfile(spath)
                break

            elif "igi" in game or "Igi" in game or "IGI" in game:
                speak("Enjoy your game sir I am going to sleep")
                fpath = "C:/Users/roopa/Desktop/Roopak/IGI1-Gameslay.net/IGI1-Gameslay.net/Game/IGI.exe"
                os.startfile(fpath)
                break

            elif "igi2" in game or "Igi2" in game or "IGI2" in game:
                speak("Enjoy your game sir I am going to sleep")
                rpath = "C:/Users/roopa/Desktop/Roopak/IGI 2 - Covert Strike/pc/igi2.exe"
                os.startfile(rpath)
                break

            elif "minecraft" in game or "Minecraft" in game:
                speak("Enjoy your game sir I am going to sleep")
                mpath = "C:/Program Files (x86)/Minecraft Launcher/oMinecraftLauncher.exe"
                os.startfile(mpath)
                break

            elif "ksp" in game or "Kerbal space program" in game or "KSP" in game or "Kerbal Space Program" in game or "space program" in game:
                speak("Enjoy your game sir I am going to sleep")
                kpath = "C:/Users/roopa/Desktop/Roopak/Kerbal Space Program/Kerbal.Space.Program.Away.with.Words.v1.3.1.1891/Kerbal Space Program/KSP.exe"
                os.startfile(kpath)
                break

            elif "gta sa" in game or "gta san andreas" in game or "GTA SA" in game or "GTA san andreas" in game:
                speak("Enjoy your game sir I am going to sleep")
                gpath = "C:/Users/roopa/Desktop/Roopak/New folder (2)/GTA SanAndreas/GTA-SanAndreas By AKTV/gta_sa.exe"
                os.startfile(gpath)
                break

        elif "open spotify" in command:
            speak("Okay sir, initiating spotify")
            epath = "C:\\Users\\roopa\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(epath)

        elif "open visual studio code" in command:
            speak("Okay sir, initiating VS Code")
            ppath = "C:\\Users\\roopa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(ppath)

        elif "open command prompt" in command:
            speak("Okay sir, opening CMD")
            os.system("start cmd")

        elif "open camera" in command:
            speak("Okay sir, opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()  

        elif "play music" in command:
            music_dir = "C:\\Users\\roopa\\Desktop\\Roopak\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                   os.startfile(os.path.join(music_dir, rd))

        elif "what is my IP address" in command:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "order pizza" in command:
            pizza()
            
        elif "wikipedia" in command:
            speak("searching wikipedia...")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "tell me the location of" in command or "where is" in command:
            speak("Okay sir which place you want location of?")
            location = takecommand().lower()
            url = f"https://www.google.com/maps/place/{location}"
            speak(f"This is where {location} is")
            webbrowser.open(url)

        elif "open YouTube" in command or "open youtube" in command or "open Youtube" in command:
            speak("Okay sir, what do you want me to search?")
            s = takecommand().lower()
            speak(f"Opening YouTube and searching {s}")
            webbrowser.open(f"https://www.youtube.com/results?search_command={s}")

        elif "open discord" in command:
            speak("Okay sir, opening Discord")
            webbrowser.open("www.discord.com")

        elif "change background" in command or "change wallpaper" in command:
            img = r'C:\\Users\\roopa\\Desktop\\Roopak\\Wallpapers'
            list_img = os.listdir(img)
            imgChoice = random.choice(list_img)
            randomImg = os.path.join(img, imgChoice)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
            speak("Background wallpaper has been changed succesfully")

        elif "empty recycle bin" in command:
            winshell.recycle_bin().empty(
                confirm=True, show_progress=False, sound=True
            )
            speak("Recycle bin is now empty")

        elif "make a note" in command or "remember this" in command:
            speak("What do you want me to note down?")
            note_text = takecommand().lower()
            note(note_text)
            speak("I have wrote down everything you wanted me to write down")

        elif "open Amazon" in command or "i want to buy something" in command or "I want to buy something" in command:
            speak("Okay sir what do you want to search?")
            d = takecommand().lower()
            webbrowser.open(f"https://www.amazon.in/s?k={d}")

        elif "show me some cooking recipes" in command or "i am hungry" in command:
            webbrowser.open("www.youtube.com/results?search_command=cooking+recipes+")

        elif "show me some gaming videos" in command:
            webbrowser.open("https://www.youtube.com/results?search_command=gaming+videos")

        elif "open google" in command or "open Google" in command:
            speak("Okay sir , what should I search?")
            s = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={s}")

        elif "search on google" in command or "search on Google" in command:
            command = command.replace("search on","")
            command = command.replace("google","")
            speak("This is what I found on web")
            kit.search(command)

            try:
                result = googleScrap.summary(command,3)
                speak(result)

            except:
                speak("No speakable data availiable.")

        elif "send Whatsapp message" in command or "send WhatsApp message" in command:
            person = takecommand().lower()
            speak("Okay sir whom do you want to text?")
            if "mom" in person or "mummy" in person:
                speak("Okay sir what should be the context of this message?")
                content = takecommand().lower()
                kit.sendwhatmsg("+919412201915", f"{content}", 4, 9)
                time.sleep(2)
                speak("Message has been sent sir")

            elif "daddy" in person or "dad" in person:
                speak("Okay sir what should be the context of this message?")
                content = takecommand().lower()
                kit.sendwhatmsg(f"+919412709676", f"{content}", 4, 9)
                time.sleep(2)
                speak("Message has been sent sir")

            else:
                speak(f"No one found named {person}")

        elif "play songs on YouTube" in command:
            speak("Okay sir which song do you want to listen?")
            g = takecommand().lower()
            kit.playonyt(f"{g}")

        elif "send email" in command:
            try:
                speak("Sir do you want to send normal mail or mail with attachment?")
                mail_type = takecommand().lower()
                if "send a file" in mail_type or "mail with attachment" in mail_type:
                    speak("Okay sir whom do you want to send mail? Please enter reciever's email address hre")
                    send_to_mail = input(str("Enter the reciever's email address here: "))
                    email = 'shuklaroopak@gmail.com'
                    password = 'Makeyeno.1'
                    speak("Okay sir, what is the subject for this email")
                    command = takecommand().lower()
                    subject = command
                    speak("And sir , what is the content for this email?")
                    command2 = takecommand().lower()
                    message = command2
                    speak("Sir please enter the correct path of the file in shell")
                    file_location = input("Enter path of file here: ")

                    speak("Please wait sir I am sending the email now...")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_mail
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" %filename)

                    # Attach the attachment to MIMEMultipart object
                    msg.attach(part)
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_mail, text)
                    server.quit()
                    speak(f"Email has been sent to {send_to_mail}")    

                elif "normal mail" in mail_type:
                    send_to_mail = input(str("Enter reciever's email address: "))
                    email = 'shuklaroopak@gmail.com'
                    password = 'Makeyeno.1'
                    message = command

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_mail, message)
                    server.quit()
                    speak(f"Sir, Email has been sent to {send_to_mail} ")
                    
            except Exception as h:
                print(h)
                speak(f"Sorry sir, I am not able to send your email to {send_to_mail}")


# to close any application
        elif "close notepad" in command:
            speak("Okay sir closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close Microsoft edge" in command or "close edge" in command:
            speak("Okay sir, closing Microsoft edge")
            os.system("taskkill /f /im msedge.exe")

        elif "close Spotify" in command:
            speak("Okay sir closing Spotify")
            os.system("taskkill /f /im Spotify.exe")

        elif "close igi" in command or "close Igi" in command or "close IGI" in command:
            speak("Ok sir terminating IGI")
            os.system("taskkill /f /im IGI.exe")

        elif "close igi2" in command or "close Igi2" in command or "close IGI 2" in command:
            speak("Ok sir terminating IGI 2")
            os.system("taskkill /f /im igi2.exe")

        elif "close space program" in command:
            speak("Okay sir terminating KSP")
            os.system("taskkill /f /im KSP.exe")

        elif "close Minecraft" in command:
            speak("Ok sir terminating Minecraft")
            os.system("taskkill /f /im MinecraftLauncher.exe")

        elif "close counter strike" in command:
            speak("Ok sir terminating Counter Strike")
            os.system("taskill /f /im Counter-Strike.exe")

        elif "close gta" in command:
            speak("Okay sir terminating GTA San Andreas")
            os.system("taskkill /f /im gta_sa.exe")
    

# new tab and minimise windows and volume up/down commands
        elif "minimise windows" in command or "minimise Windows" in command or "minimise this application" in command:
            pyautogui.press("Win"+"d")

        elif "new tab" in command:
            pyautogui.hotkey('ctrl','t')

        elif "volume up" in command:
            pyautogui.hotkey('volumeup')

        elif "volume down" in command:
            pyautogui.hotkey('volumedown')

        elif "mute" in command:
            pyautogui.press("volumemute")

        elif "what is today's date" in command:
            today_date()


# to check battery percentage
        elif "how much battery is left" in command or "battery" in command:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system is left up with {percentage} percent battery")
            if percentage>=75:
                speak("We have enough energy to keep moving")
            elif percentage>=40 and percentage<=50:
                speak("Sir I think you should connect this system to charging")
            elif percentage>=15 and percentage<=30:
                speak("We dont have enough power to work please connect it to charging")
            elif percentage<=15:
                speak("ALERT! ALERT! WE HAVE VERY LOW BATTERY CONNECT IT TO CHARGING NOW OR ELSE THE SYSTEM WILL SHUT DOWN SOON")


# to check internet speed
        elif "internet speed" in command:
            speak("Okay sir, this might take some time")
            downl = Speedtest.download('self')
            upl = Speedtest.upload()
            speak(f"Sir your internet's download speed is: {downl}")
            speak("And")
            speak(f"Your internet's upload speed is: {upl}")


# to get current date and time
        elif "what is todays date" in command or "what is today's date" in command:
            import datetime as DateTme
            now3 = DateTme.datetime.now()
            speak("Current Date and Time is")
            print(now3.strftime("%d-%m-%y %H:%M:%M %p"))


# to do conversation with Sinister

        elif "hello" in command or "hey" in command:
            speak("Hello sir I am Sinister , how may I help you?")

        elif "how are you" in command:
            speak("I am doing good sir , how are you?")

        elif "i am also good" in command:
            speak("That's great to hear from you")

        elif "thank you" in command:
            speak("That's my pleasure sir")

        elif "what is todays date" in command:
            today_date()
 
        elif "go to sleep" in command:
            speak("Okay sir, I am going to sleep now")
            break


# to set alarm
        elif "set alarm" in command:
            from datetime import datetime 
            from playsound import playsound
            alarm_time = input("Enter the time of alarm to be set HH:MM:SS  AM/PM:  ")
            alarm_hour=alarm_time[0:2]
            alarm_minute=alarm_time[3:5]
            alarm_seconds=alarm_time[6:8]
            alarm_period=alarm_time[9:11]

            speak("Alarm set!")

            while True:
                now = datetime.now()
                current_hour = now.strftime("%I")
                current_minute = now.strftime("%M")
                current_seconds = now.strftime("%S")
                current_period = now.strftime("%p")
                if(alarm_period==current_period and alarm_hour==current_hour and alarm_minute==current_minute and alarm_seconds==current_seconds):
                    speak(f"Sir, its {alarm_time}")
                    playsound('C:/Users/roopa/Desktop/Roopak/music/YoonJ - Pain.mp3')
                    break


# to set timer
        elif "set timer" in command:
            import time
            seconds = int(input("How many seconds do you want to set a timer?:  "))
            for i in range(seconds):
                print(str(seconds - i) + "    seconds left")
                time.sleep(1)
            speak("Time is up")


# to record voice
        elif "start voice recording" in command:
            fs=44100
            second=10

            speak("Recording...")

            record_voice = sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
            sounddevice.wait()
            write("voice_recording.wav",fs,record_voice)


# to get passwords of all near Wi-Fis 
        elif "show me all wifi passwords" in command or "show me all Wi-Fi password" in command or "show me all Wi-Fi passwords" in command or "show me all wi-fi password" in command:
            wifi_pass()


# to get weather report
        elif "temperature" in command or "weather" in command:
            speak("Of which place do you want temperature of?")
            search = int(str("Enter the name of your district/city:  "))
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"Current {search} is {temp}")


# to find joke
        elif "tell me a joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)


# to control power options of system
        elif "shutdown the system" in command:
            os.system("shutdown /s /t 5")

        elif "restart the system" in command:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in command:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# to switch window
        elif "switch window" in command:
            speak("Switching window...")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(0)
            pyautogui.keyUp("alt")


# to listen latest headlines
        elif "tell me news" in command or "tell me latest news" in command:
            speak("Okay sir , fetching latest news")
            news()


# to get space news
        elif "space news" in command:
            speak("Enter the date for news extraction")
            Date = str(input("Enter the date here:  "))
            from functions import DateConverter
            Value = DateConverter(Date)

            from nasa import NasaNews
            NasaNews(Value)


# to do some calculations using voice
        elif "do some calculations" in command or "can you calculate" in command:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What do you want to calculate sir?")
                print("Listening..")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add, #plus
                    '-' : operator.sub, #minus
                    'x' : operator.mul, #multiply
                    'divided' :operator.__truediv__, #divide
                }[op]
            def eval_binary_expr(op1, oper, op2): #5 plus 5
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("Your result is:")
            speak(eval_binary_expr(*(my_string.split())))


# to find/search about someone
        elif "who is" in command:
            app_id = "EW6LGU-K5YWTRP6WV"
            client = wolframalpha.Client(app_id)
            ind = takecommand().lower().split().index("is")
            text = text.split()[ind + 1:]
            res = client.command(" ".join(text))
            answer = next(res.results).text
            speak(f"{answer}")


# To find/get our location using IP Address
        elif "where am I" in command or "where are we" in command:
            speak("Okay sir , finding our location")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                # print(geo_data)
                city = geo_data['city']
                # state = geo_data['state']
                country = geo_data['country']
                speak(f"Sir I am not sure but we are in {city} city of {country} country.")
            except Exception as j:
                speak("Sorry sir, due to internet connectivity problem I am not able to find our location.")
                pass
        

# to take screen shot
        elif "take screenshot" in command:
            speak("Sir please tell me the name of the file")
            name = takecommand().lower()
            speak("Please wait sir I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot has been took and now I am ready for your next command.")


# to read a pdf using Sinister 
        elif "read a PDF" in command:
            pdf_reader()


# to hide/unhide all file of one particular folder
        elif "hide all files of this folder" in command or "hide this folder" in command or "unhide all files of this folder" in command:
            speak("Sir tell me if you want to hide all files of folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide everything" in condition:
                os.system("attrib +h /s /d")
                speak("Sir now all the files of this folder are hidden.")

            elif "make it visible for everyone" in condition:
                os.system("attrib -h /s /d")
                speak("Sir now all the files of this folder are visible to everyone. I wish you are taking this decision in your peace")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok sir")            


# to activate how-to-do protocol
        elif "activate how to do protocol" in command:
            speak("How-To-Do protocol is now active")
            while True:
                speak("Sir,what do you want me to search through it?")
                how = takecommand()
                try:
                    if "exit" or "leave" in how:
                        speak("Ok sir, Disabling How-To-Do protocol")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as r:
                    speak("Sorry sir, I am not able to find your command.") 


# screen recording
        elif "record screen" in command or "screen recording" in command:
            speak("Starting Screen Recording")
            SCREEN_SIZE = (1366, 768)

            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

            fps = 60
            prev = 0

            while True:

                time_elapsed = time.time() - prev 
                img = pyautogui.screenshot()

                if time_elapsed > 1.0/fps:
                    prev = time.time()
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    out.write(frame)

                cv2.waitKey(0)
                cv2.destroyAllWindows
                out.release()


# screen recorder
# def screen_recording():
 #   SCREEN_SIZE = (1366, 768)

 #   fourcc = cv2.VideoWriter_fourcc(*"XVID")
  #  out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

   # fps = 60
    #prev = 0

   # while True:

    #    time_elapsed = time.time() - prev 
     #   img = pyautogui.screenshot()

      #  if time_elapsed > 1.0/fps:
       #     prev = time.time()
        #    frame = np.array(img)
         #   frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          #  out.write(frame)

     #   cv2.waitKey(100)
      #  cv2.destroyAllWindows
       # out.release()

# for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e060b6156fed4a6086d5f4abad468a2c'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"Today's {day[i]} news is: , {head[i]}")

# pdf reader
def pdf_reader():
    book = open('science ch1.pdf','rb')
    speak(f"Name of PDF is {book}")
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book: {pages}")
    speak("Sir please enter the page number I have to read")
    pg = int(input("Please enter the page number here: "))
    page = pdfReader.getPage(pg)
    text = page.extractText(page)
    speak(text)

def wifi_pass():
    import subprocess
    data = subprocess.check_output(['netsh', 'wlan', 'show',
                                'profiles']).decode('utf-8').split('\n')
    # now we will store the profile by converting them to list
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        # running the 2nd cmd command to check passwords
        password= subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i,'key=clear']).decode('utf-8').split('\n')
        # storing passwords after converting them to list
        password = [b.split(":")[1][1:-1] for b in password if "Key Content" in b]
        # printing the profiles(wifi name) with their passwords using
        # try and except method for exception handing
        try:
            print ("{:<30}|  {:<}".format(i, password[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def pizza():
    driver = webdriver.Edge(r"C:/Users/roopa/Desktop/msedgedriver.exe")
    driver.maximize_window()

    speak("Opening Dominos")
    driver.get('https://www.dominos.co.in/')
    sleep(2)

    speak("Getting ready to order")
    driver.find_element_by_link_text('ORDER ONLINE NOW').click()
    sleep(2)

    speak("Finding your location")
    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
    sleep(2)

    location = ""

    speak("Entering your location")
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(
        location)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]').click()
    sleep(2)

    try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()
        sleep(2)
    except:
        speak("Your location could not be found. Please try again later.")
        exit()

    speak("Logging in")

    phone_num = "9412709676"

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
        phone_num)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    speak("What is your O T P?")
    sleep(3)

    otp_log = takecommand().lower()

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
        otp_log)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
    sleep(2)

    speak("Do you want me to order from your favorites?")
    command_fav = takecommand().lower()

    if "yes" in command_fav:
        try:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()
            sleep(1)
        except:
            speak("The entered OTP is incorrect.")
            exit()

        speak("Adding your favorites to cart")

        speak("Do you want me to add extra cheese to your pizza?")
        ex_cheese = takecommand().lower()
        if "yes" in ex_cheese:
            speak("Extra cheese added")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()
        elif "no" in ex_cheese:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
        else:
            speak("I dont know that")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()

        driver.find_element_by_xpath(
            '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()
        sleep(1)

        speak("Would you like to increase the quantity?")
        qty = takecommand().lower()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            speak("Would you like to increase the quantity of pizza?")
            wh_qty = takecommand().lower()
            if "yes" in wh_qty:
                speak("How many more pizzas would you like to add? ")
                try:
                    qty_pizza = takecommand().lower()
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        speak(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
                except:
                    speak("I dont know that.")
            else:
                pass

            speak("Would you like to increase the quantity of pepsi?")
            pep_qty = takecommand().lower()
            if "yes" in pep_qty:
                speak("How many more pepsis would you like to add? ")
                try:
                    qty_pepsi = takecommand().lower()
                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsis"
                        speak(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
                except:
                    speak("I dont know that.")
            else:
                pass

        elif "no" in qty:
            pass

        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        speak(tell_num)
        check_order = takecommand().lower()
        if "yes" in check_order:
            speak("Checking out")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
            sleep(1)
            total = driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[6]/span[2]/span')
            total_price = f'total price is {total.text}'
            speak(total_price)
            sleep(1)
        else:
            exit()

        speak("Placing your order")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button').click()
        sleep(2)
        try:
            speak("Saving your location")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()
            sleep(2)
        except:
            speak("The store is currently offline.")
            exit()

        speak("Do you want to confirm your order?")
        confirm = takecommand().lower()
        if "yes" in confirm:
            speak("Placing your order")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
            sleep(2)
            speak("Your order is placed successfully. Wait for Dominos to deliver your order. Enjoy your day!")
        else:
            exit()

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    month_now = now.month
    day_now = now.day
    speak(f"Its currently {now} which is {day_now} of {month_now}th month")

if __name__ == '__main__':
    while True:
        permission = takecommand().lower()
        if "wake up" in permission:
            CommandExecution()
        elif "terminate yourself" in permission:
            sys.exit()
            