import email
from pickle import TRUE
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui as p
import webbrowser
from time import sleep
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alice Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        query.lower()
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "search" in query:
            query = query.replace("search"," ")
            print(f"Searching {query}")
            speak(f"Searching {query}")
            os.startfile("C:\\Users\\Public\\Desktop\\Google Chrome.lnk")
            sleep(3)
            p.typewrite(query)
            p.press('enter')
            sleep(2)
            p.click(214,439)

        elif "hello alice" in query:
            print("Hello")
            speak("Hello")

        elif "who is maaz" in query:
            print("maaz is btech 1st year student")
            speak("maaz is btech 1st year student")

        elif "who is alina" in query:
            print("alina is the project leader")
            speak("alina is the projet leader")

        elif "who is anshu" in query:
            print("anshu is btech 1st year student ")
            speak("anshu is btech 1st year student")

        elif "who is kushal" in query:
            print("kushal is btech 1st year student")
            speak("kushal is btech 1st year student")
        
        elif "pratish rawat" in query:
            print("did you mean")
            speak("did you mean")
            webbrowser.open("https://www.instagram.com/pratish.rawat/")

        elif"hello" in query:
            print("hello")
            speak("hello")
        
        elif"how are you" in query:
            print("i am fine what about you")
            speak("i am fine what about you")
        
        elif"i am not fine"in query:
            print("what happened sir")
            speak("what happened sir")

        elif"i am fine " in query:
            print("okay sir")
            speak("okay sir")
        elif "i am not feeling well" in query:
            print("you should go to a nearby hospital sir")
            speak("you should go to a nearby hospital sir")
        
        elif "doctor near me" in query:
            print("searching")
            speak("searching")
            webbrowser.open("https://www.google.com/search?q=doctor+near+me&sxsrf=ALiCzsZvwqoFkMZn--pxwaKhHBvLZRwXRw%3A1668446345585&ei=iXhyY_mgI_PRseMPuYS_iAw&ved=0ahUKEwi5iYX-lq77AhXzaGwGHTnCD8EQ4dUDCA8&oq=doctor+near+me&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQDEoECE0YAUoECEEYAEoECEYYAFAAWABgAGgAcAF4AIABAIgBAJIBAJgBAA&sclient=gws-wiz-serp")
        
        elif "what is your nickname Alice" in query:
            print("billi miyau")
            speak("billi miyau")
        
        elif "main kaun hun" in query:
            query = takeCommand().lower()
            print("you are maaz")
            speak("you are maaz")
        
        elif "hello alice guess who  i am ?" in query:
            query = takeCommand().lower()
            print("you are alina")
            speak("you are alina")

        elif "guess who is speaking" in query:
            print("anshu is speaking")
            speak("anshu is speaing")

        elif "alice guess who is speaking" in query:
            print("ayushi is speaking")
            speak("ayushi is speaking")

        elif "who am i" in query:
            print("kushal is speaking")
            speak("kushal is speaking")
        
        

        elif "open poornima website" in query:
            query = takeCommand().lower()
            print("opening")
            speak("opening sir")
            webbrowser.open("https://www.poornima.edu.in/")
            
        elif "tell me a joke" in query:
            print("look at yourself in mirror")
            speak("look at yourself in mirror")
            os.startfile("C:\\Users\\91909\\Pictures\\meme")
        
        elif "coordinates of mouse" in query:
             print("wait a moment sir")
             speak("wait a moment sir")
             print(p.position())
             speak(p.position())

        elif "open mouse" in query:
            query.lower()
            os.startfile("virtual\main.py")
            break

        elif "open virtual controller" in query:
            os.startfile("virtual\\controller.py")
            webbrowser.open("https://poki.com/en/g/crazy-cars")
            break


        elif "bluetooth" in query:
            p.press("win")
            sleep(1)
            p.typewrite("bluetooth")
            sleep(1)
            p.press("enter")
            sleep(3)
            p.click(1722,180)
            sleep(1)
            p.click(1649,521)

        elif "weather" in query:
            webbrowser.open("https://www.google.com/search?q=weather&oq=whe&aqs=chrome.1.69i57j0i10i131i433i512j0i512j0i131i433j0i512l3j46i175i199i512j0i512l2.2479j0j7&sourceid=chrome&ie=UTF-8&dlnr=1&sei=3A9VY7_JGLqgseMPsICr-AU")

        elif "country code" in query:
            os.startfile("country code\country.py")
            
        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com/")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif "create a text file" in query:
            os.startfile("files\\1.txt")

        elif 'play music' in query:
            dirs = "D:\\music\\Besabriyaan (MS Dhoni - The Untold Story).mp3"
            os.startfile("D:\\music\\Besabriyaan (MS Dhoni - The Untold Story).mp3")
            break

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Metro\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

            
        elif "message on instagram" in query:
            speak("Enter the username please")
            usrn = input("Enter username:\n")
            print("What should i say")
            speak("What should i say")
            content = takeCommand().lower()
            webbrowser.open(f"https://www.instagram.com/{usrn}/")
            sleep(10)
            p.click(1339,196)
            sleep(8)
            p.typewrite(content)
            p.press('enter')
            print(p.position())
            break



            

        elif 'email to mass' in query:
            email1 = "nabeel.ali.private@gmail.com"
            print("What should i say")
            speak("What should i say")
            content = takeCommand()
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            sleep(5)
            p.click(120,265)
            sleep(1)
            p.typewrite(email1)
            p.click(1220,558)
            p.typewrite(content)
            p.click(1151,954)

        elif "table of" in query:
            inp = query.replace("table of","")
            inp = int(inp)          

            for i in range(11):

                i1 = inp*i
                form = f"{inp} x {i} = {i1}"
                form1 = f"{inp} {i}s are {i1}"
                print(form)
                speak(form1)


        elif "by" in query:
            try: 
                def test():
                    inp = query

                    val = "by"

                    if val in inp:
                        inp = inp.replace(val,"")
                        if "what is" in inp:
                            inp = inp.replace("what is","")
                            inp = inp.split()
                            pr1 = int(inp[0])
                            pr2 = int(inp[1])
                            print(f"{pr1} x {pr2} = {pr1*pr2}")
                            speak(f"{pr1} x {pr2} = {pr1*pr2}")


                test()
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")



        elif "cube" in query:
            try:
                inp = query
                if "cube" in inp:
                    if "what is the cube of" in  inp:
                        inp = inp.replace("what is the cube of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp*inp}")
                        speak(f"The answer is {inp*inp*inp}")
                        

                    else:
                        inp = inp.replace("cube of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp*inp}")
                        speak(f"The answer is {inp*inp*inp}")
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")
            

        elif "plus"or"+" in query:
            try: 
                def test():
                    inp = query

                    val = "plus"
                    val1 = "+"

                    if val in inp:
                        inp = inp.replace(val,"")
                        if "what is" in inp:
                            inp = inp.replace("what is","")
                            inp = inp.split()
                            pr1 = int(inp[0])
                            pr2 = int(inp[1])
                            print(f"{pr1} + {pr2} = {pr1+pr2}")
                            speak(f"{pr1} + {pr2} = {pr1+pr2}")

                    elif val1 in inp:
                        inp = inp.replace(val1,"")
                        if "what is" in inp:
                            inp = inp.replace("what is","")
                            inp = inp.split()
                            pr1 = int(inp[0])
                            pr2 = int(inp[1])
                            print(f"{pr1} + {pr2} = {pr1+pr2}")
                            speak(f"{pr1} + {pr2} = {pr1+pr2}")
                test()
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")


        elif "square" in query:
            try:
                inp = query
                if "square" in inp:
                    if "what is the square of" in  inp:
                        inp = inp.replace("what is the square of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp}")
                        speak(f"The answer is {inp*inp}")
                        

                    else:
                        inp = inp.replace("square of","")
                        inp = int(inp)
                        print(f"The answer is {inp*inp}")
                        speak(f"The answer is {inp*inp}")
            except Exception as e:
                print("This method is only for intgers not for string")
                speak("This method is only for intgers not for string")
 

        with open("db.txt","a")as f:
            f.write(query)
            f.write("\n")



      
