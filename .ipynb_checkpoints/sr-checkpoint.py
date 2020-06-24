import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play
from gtts import gTTS as tts

def capture():
    """Capture audio"""
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('I\'M LISTENING...')
        audio = rec.listen(source, phrase_time_limit=5)
    try:
        text = rec.recognize_google(audio, language='en-US')
        return text
    except:
        speak('Sorry, I could not understand what you said.')
        return 0
    
def process_text(name, input):
    """Process what is said"""
    speak(name + ', you said: "' + input + '".')
    return

def speak(text):
    """Say something"""
    # Write output to console
    print(text)
    # Save audio file
    speech = tts(text=text, lang='en')
    speech_file = 'input.mp3'
    speech.save(speech_file)
    # Play audio file
    sound = AudioSegment.from_mp3(speech_file)
    play(sound)
    os.remove(speech_file)

if __name__ == "__main__":
    # First get name
    speak('What is your name?')
    name = capture()
    speak('Hello, ' + name + '.')
    # Then just keep listening & responding
    while 1:
        speak('What do you have to say?')
        captured_text = capture().lower()
        if captured_text == 0:
            continue
        if 'quit' in str(captured_text):
            speak('OK, bye, ' + name + '.')
            break
        # Process captured text
        process_text(name, captured_text)
