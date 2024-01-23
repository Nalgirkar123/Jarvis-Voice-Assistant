import pyttsx3  # pip install pyttsx3
from decouple import config
import time
USER = config('USER')
BOTNAME = config('BOTNAME')


def speak(Text):
    Text = str(Text)
    Text = Text.replace("<USER>", USER)
    Text = Text.replace("<BOTNAME>", BOTNAME)
    engine = pyttsx3.init('sapi5')  # object creation
    # pyttsx3 supports three TTS engine:


    # These two lines will set jarvis voice, it's rate if device doesn't have it set
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate', 200)
    # say method on the engine that passing input text to be spoken
    print(f"\nJarvis : {Text}\n")
    engine.say(Text)
    # run and wait method, it processes the voice commands.
    engine.runAndWait()
