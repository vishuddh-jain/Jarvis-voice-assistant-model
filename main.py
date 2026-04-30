import speech_recognition as sr
import webbrowser
import pyttsx3


recognizer = sr.Recognizer()
# engine = pyttsx3.init()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
  

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    if "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    if "open chatgpt" in c.lower():
        webbrowser.open("https://facebook.com")
    if "open github" in c.lower():
        webbrowser.open("https://github.com")
        
       

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
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
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
            



