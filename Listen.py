import speech_recognition as sr  # pip install speech_recognition


def take_user_input(type):

    r = sr.Recognizer()  # object creation
    with sr.Microphone() as source:  # use the default microphone as the audio source
        if(type != 1):
            print("Listening...")
        r.pause_threshold = 1
        # listen for the first phrase and extract it into audio data
        audio = r.listen(source,0,5)
    try:
        if(type != 1):
            print("Recognizing...")
        # recognize speech using Google Speech Recognition
        query = r.recognize_google(audio, language="en-in", show_all=True)
    except:
        return "*Say that again please..."
    if(len(query) != 0):
        query = str(query['alternative'][0]['transcript'])
        if(type != 1):
            print(f"You Said : {query}")
        query = query.lower()
        if(type < 2 and "jarvis" not in query):
            return "*Please include jarvis in your command"
        else:
            query = query.replace("jarvis", "")
        return query
    else:
        return "*Please say something..."


def Listen(type=0):
    query = take_user_input(type)
    while(query[0] == '*'):
        if(type != 1):
            print(f"\nJarvis : {query[1:]}\n")
        query = take_user_input(type)
    return query
