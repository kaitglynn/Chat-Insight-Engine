```python
import speech_recognition as sr

def controlVoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        voiceCommand = r.recognize_google(audio, language='en-us')
        print(f"User said: {voiceCommand}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return voiceCommand

def executeVoiceCommand(command):
    if 'exit' in command:
        exit()
    # Add more voice commands and their corresponding actions here

def main():
    while True:
        command = controlVoice().lower()
        executeVoiceCommand(command)

if __name__ == "__main__":
    main()
```