import clipboard
import datetime
import os
import psutil
import pyautogui
import pyjokes
import pyttsx3
import wikipedia
import pywhatkit
import wolframalpha
import smtplib
import ctypes
from urllib.request import urlopen
import requests
import tkinter
import subprocess
import json
import smtplib
import speech_recognition as sr
import time as ti
import webbrowser as we
from email.message import EmailMessage
from newsapi import NewsApiClient
from time import sleep

user = "Arnav"
assistant = "Technow"
engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)
def output(audio):
    print(audio) 
    engine.say(audio)
    engine.runAndWait()

def inputCommand():
    query = input() 
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 0
        try:
            query = r.recognize_google(r.listen(source), language="en-IN")
        except Exception as e:
            output("Speak again, Sauron")
    return query
def greet():
        hour = datetime.datetime.now().hour
        if (hour >= 6) and (hour < 12):
           output(f"Good Morning {user}, this is Technow")
        elif (hour >= 12) and (hour < 18):
           output(f"Good afternoon {user}, this is Technow")
        elif (hour >= 18) and (hour < 21):
           output(f"Good Evening {user}, this is Technow")
           output("How may I assist you, Chairman and Founder?")
def sendEmail():
    senderemail = "arnavnandurkar3@gmail.com"
    password = "enterpasswordhere"
    email_list = {
        "one": "enteremail1", 
        "two": "enteremail2"
    }
    try:
        email = EmailMessage()
        output("To which human do you want to send the mail?")
        name = inputCommand().lower()
        email['To'] = email_list[name]
        output("What is the subject of the mail?")
        email["Subject"] = inputCommand()
        email['From'] = senderemail
        output("What should I Say?")
        email.set_content(inputCommand())
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(senderemail, password)
        s.send_message(email)
        s.close()
        output("Email has been sent")
    except Exception as e:
        print(e)
        output("Unable to send the Email")
def sendWhatMsg():
    user_name = {
        'enternamehere': 'entermobilenumber'
    }
    try:
        output("To whom you want to send the message, O Lord of the Ring?")
        name = inputCommand()
        output("What is the message?")
        we.open("https://web.whatsapp.com/send?phone=" +
                user_name[name]+'&text='+inputCommand())
        sleep(3)
        pyautogui.press('enter')
        output("Message sent")
    except Exception as e:
        print(e)
        output("Unable to send the Message")
def weather():
    city = "Pune"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
def news():
    newsapi = NewsApiClient(api_key='5840b303fbf949c9985f0e1016fc1155')
    output("What news do thou seek, master?")
    topic = inputCommand()
    data = newsapi.get_top_headlines(
        q=topic, language="en", page_size=5)
    newsData = data["articles"]
    for y in newsData:
        output(y["description"])
def idea():
    output("What's your new idea or invention?")
    data = inputCommand().title()
    output("Your latest idea or invention was: " + data)
    with open("data.txt", "a", encoding="utf-8") as r:
        print(data, file=r)
greet()
while True:
    query = inputCommand().lower()
    if ("time" in query):
        output("Current time is " +
               datetime.datetime.now().strftime("%I:%M"))

    elif ('date' in query):
        output("Current date is " + str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))

    elif ('send mail' in query):
        sendEmail()

    elif ('message' in query):  
        print("Sending...")
        sendWhatMsg()

    elif ("search" in query):
        output("what you want to search?")
        we.open("https://www.google.com/search?q="+inputCommand())

    elif ("youtube" in query):
        output("What you want to search on Youtube?")
        pywhatkit.playonyt(inputCommand())

    elif ('weather' in query):
        weather()

    elif ("news" in query):
        news()

    elif ("read" in query):
        output(clipboard.paste())

    elif ("workspace" in query):
        output("Which workspace you want to work on")
        os.startfile("D:\\Work Spaces\\" +
                     inputCommand()+".code-workspace")

    elif ("joke" in query):
        output(pyjokes.get_joke())

    elif ("idea" in query):
        idea()

    elif ("do you know" in query):
        ideas = open("data.txt", "r")
        output(f"One of your inventions was:\n{ideas.read()}")

    elif ("screenshot" in query):
        pyautogui.screenshot(str(ti.time()) + ".png").show()

    elif "cpu" in query:
        output(f"Cpu is at {str(psutil.cpu_percent())}")

    elif "who" in query:
        output("I am Technow, a basic voice assistant created by Arnav Nandurkar. What may I do for you?")
    
    elif "about technow" in query:
        output("Technow is a Science Club started by Arnav Nandurkar on 30th March 2016.")

    elif "hello" in query:
        greet()
    
    elif "good night" in query:
        hour = datetime.datetime.now().hour
        if (hour >= 21) and (hour < 6):
            output(f"Good Night {user}!")
        else:
            output(f"Good Night {user}!")
        quit()
    elif "bye" in query:
        output('The Technow AI Assistant is closing. I wish you a pleasant day! ')
    
  
    elif 'how are you' in query:
        output("I'm always fine. I'm not real. Of course I would be fine." or "Good, thank you, and you?")

    elif 'fine' in query:
        output("Fine? Good? Not for long.")
    
    elif 'rings poem' in query:
        output("Three Rings for the Elven Kings under the sky. Seven for the Dwarf Lords in their halls of stone. Nine for mortal men doomed to die. One for the Dark Lord on his Dark Throne in the Land of Mordor where the shadows lie. One ring to rule them all, One Ring to find them, One ring to bring them all and in the darkness bind them, in the Land of Mordor Where the shadows lie.")
    
    elif 'may the force be with you' in query:
        output("May the Force be with you, Jedi.")
 