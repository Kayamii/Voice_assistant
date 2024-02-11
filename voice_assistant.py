import speech_recognition as sr
import pyttsx3
import subprocess
import webbrowser
import pyautogui


r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            engine.say("Sorry, I did not get that")
            return 0

def respond(text):
    if text:
        print("You said: ", text)
        if 'open browser' in text.lower():
            engine.say("Opening browser")
            engine.runAndWait()
            webbrowser.open('http://google.com')  # Opens the default web browser to Google's homepage
        elif 'open calculator' in text.lower():
            engine.say("Opening calculator")
            engine.runAndWait()
            subprocess.run(['calc'])  # Opens the calculator
        elif 'open notepad' in text.lower():
            engine.say("Opening notepad")
            engine.runAndWait()
            subprocess.run(['notepad'])  # Opens notepad
        elif 'exit' in text.lower():
            engine.say("Goodbye")
            engine.runAndWait()
            exit()
        elif 'calculate' in text.lower(): # Calculate the result of a mathematical expression
            try:
                
                calculation = eval(text.lower().replace('calculate', ''))
                engine.say("The result is " + str(calculation))
                engine.runAndWait()
            except:
                engine.say("Sorry, I could not perform the calculation.")
                engine.runAndWait()    
        elif 'search on google' in text.lower(): #search for something on the web
            try:
                search = text.lower().replace('search on google', '')
                engine.say("Searching for " + search)
                engine.runAndWait()
                webbrowser.open('http://google.com/search?q=' + search)
            except:
                engine.say("Sorry, I could not perform the search.")
                engine.runAndWait()
        elif 'search on youtube' in text.lower(): #search for a video on youtube
            try:
                search = text.lower().replace('search on youtube', '')
                engine.say("searching for " + search)
                engine.runAndWait()
                webbrowser.open('http://youtube.com/search?q=' + search)

            except:
                engine.say("Sorry, I could not play the video.")
                engine.runAndWait()
        elif 'take a screenshot' in text.lower(): #take a screenshot
            engine.say("Taking a screenshot")
            engine.runAndWait()
            pyautogui.screenshot('screenshot.png')

                       
        else:
            engine.say("Sorry, I did not understand that.")
            engine.runAndWait()



while True:
    
    respond(listen())