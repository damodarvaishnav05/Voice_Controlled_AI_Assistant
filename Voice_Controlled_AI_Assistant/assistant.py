# Importing necessary libraties for voice_controlled_ai_assistant

import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import pyjokes
import Musicplayer

# Initializing pyttsx3 for text to speech
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("\nListening")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=4)
            
        # Here the error will be handled sapertly
        except Exception as e: 
            print("Listening")
            print("Please try to speak again!")
            return "none"


# now error handling using try and error block

    try:
        print("Recognizing")
        statement = r.recognize_google(audio, language = "en-in")
        print(f"You said:{statement}\n")


# If not recognized voice properly then it passes the error to exception block

    except Exception as e:
        print("Sorry i could not understand, Plz say that again!!")
        return "None"
    return statement.lower()


# Here we define a wish me function for current datetime
 
def wish_me():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("\nGood Morning")

    elif 12 <= hour < 18:
        speak("\nGood Aftenoon")
    
    else:
        speak("Good Evening")

speak("I am your voice assistant, How can i help you")


notes = "notes.txt" # the txt file named notes


# Take note function 

def take_note():
    speak("what should i write in your note")

    note = take_command()

    if note != "None":
        with open(notes,'a') as f:
            f.write(f"{datetime.datetime.now()} - {note}\n")
        speak("Note saved successfully.")
    
    else:
        speak("I can't understand your note")



# For running the program

if __name__ == "__main__":
    wish_me()


    while True:

        statement = take_command()

        if statement == "None":
            continue

        elif "stop the program" in statement or "exit" in statement or "bye" in statement or "stop" in statement:
            speak("Good by, have a nice day Damodar!!!")
            break


        elif "note" in statement or "take note" in statement:
            take_note()


        elif "google" in statement or "open google" in statement:
            webbrowser.open("https://google.com")


        elif "chrome" in statement or "open chrome" in statement:
            webbrowser.open("https://chrome.com")


        elif "linkedin" in statement or "open linkedin" in statement:
            webbrowser.open("https://linkedin.com")


        elif "youtube" in statement or "open youtube" in statement:
            webbrowser.open("https://youtube.com")


        elif "github" in statement or "open github" in statement:
            webbrowser.open("https://github.com")


        elif "instagram" in statement or "open instagram" in statement:
            webbrowser.open("https://www.instagram.com")


        elif "facebook" in statement or "open facebook" in statement:
            webbrowser.open("https://www.facebook.com")


        elif "twitter" in statement or "open twitter" in statement or "open x" in statement:
            webbrowser.open("https://www.twitter.com")


        elif "gmail" in statement or "open gmail" in statement:
            webbrowser.open("https://mail.google.com")


        elif "whatsapp" in statement or "open whatsapp" in statement:
            webbrowser.open("https://web.whatsapp.com")


        elif "chat gpt" in statement or "open chat gpt" in statement:
            webbrowser.open("https://chat.openai.com")


        elif "stack overflow" in statement or "open stackoverflow" in statement:
            webbrowser.open("https://stackoverflow.com")


        elif "netflix" in statement or "open netflix" in statement:
            webbrowser.open("https://www.netflix.com")


        elif "amazon" in statement or "open amazon" in statement:
            webbrowser.open("https://www.amazon.in")


        elif "flipkart" in statement or "open flipkart" in statement:
            webbrowser.open("https://www.flipkart.com")


        elif "spotify" in statement or "open spotify" in statement:
            webbrowser.open("https://www.spotify.com")


        elif "zoom" in statement or "open zoom" in statement:
            webbrowser.open("https://zoom.us")


        elif "maps" in statement or "open maps" in statement:
            webbrowser.open("https://www.google.com/maps")


        elif "news" in statement or "open news" in statement:
            webbrowser.open("https://news.google.com")


        elif "weather" in statement or "open weather" in statement:
            webbrowser.open("https://weather.com")


        elif "pinterest" in statement or "open pinterest" in statement:
            webbrowser.open("https://www.pinterest.com")


        elif "reddit" in statement or "open reddit" in statement:
            webbrowser.open("https://www.reddit.com")


        elif "quora" in statement or "open quora" in statement:
            webbrowser.open("https://www.quora.com")


        elif "code forces" in statement or "open codeforces" in statement:
            webbrowser.open("https://codeforces.com")


        elif "best code" in statement or "open leetcode" in statement:
            webbrowser.open("https://leetcode.com")


        elif "geeksforgeeks" in statement or "open geeks for geeks" in statement:
            webbrowser.open("https://www.geeksforgeeks.org")


        elif statement.lower().startswith("play"):
            parts = statement.split(" ", 1)
            if len(parts) > 1:
                song = parts[1].replace(" ", "_")
                link = Musicplayer.musics.get(song)

                if link:
                    speak(f"Playing {parts[1]}")
                    webbrowser.open(link)

                else:
                    speak(f"Could'nt find song {parts[1]}")
            else:
                speak("Please tell me the song which you want!")


        # Search results are on the basis of out voice as you speak

        elif "search" in statement:
            speak("What do you want to search ?")
            search_term = take_command()
            if search_term != "None":
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
                speak(f"Here are search result's for {search_term}")
            else:
                speak("Sorry i did'nt catch that.")



        elif "joke" in statement:
            speak(pyjokes.get_joke())


        elif "open camera" in statement:
            os.system("start microsoft.windows.camera:")


        elif "open notepad" in statement:
            os.system("notepad")


        elif "lock system" in statement:
            speak("Locking your system")
            os.system("rundll32.exe user32.dll, LockWorkStation")


        elif "shutdown" in statement:
            speak("Shutting down your system.")
            os.system("shutdown /s /t 1")


        elif "restart" in statement:
            speak("Restarting system.")
            os.system("shutdown /r /t 1")


        else:
            speak("Sorry i did'nt got it!!")