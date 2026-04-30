import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from models.ai_assistant import ask_ai


recognizer = sr.Recognizer()
# engine = pyttsx3.init()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
  
  
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif c.lower().startswith("fuck"):
        speak("thankyou buddy")

    # AI fallback (MOST IMPORTANT)
    else:
        speak("Thinking...")
        response = ask_ai(c)
        print("Ai: ", response)
        speak(response)
       

if __name__ == "__main__":
    speak("Initializing jarvis")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        # recognize speech using google
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
            



