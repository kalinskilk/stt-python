import speech_recognition as sr

def speechToText():
    print('sr.__version__')
    print(sr.__version__)
    r = sr.Recognizer()
    print('lendo audio')
    harvard = sr.AudioFile('harvard.wav')
    with harvard as source:
        audio = r.record(source, offset=4, duration=3)
    print('transformando em texto')    
    a = r.recognize_google(audio)        
    print('resultado: '+a)

speechToText()
