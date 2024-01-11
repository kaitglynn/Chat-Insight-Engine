```python
import speech_recognition as sr
from gtts import gTTS
import os
import pyaudio
import wave

class VoiceChat:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            print("Recognizing...")
            voice_data = self.recognizer.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
            return self.listen()

    def respond(self, response):
        tts = gTTS(text=response, lang='en')
        tts.save('response.mp3')
        os.system('start response.mp3')

    def record_voice(self, filename, duration):
        chunk = 1024  
        sample_format = pyaudio.paInt16  
        channels = 2
        fs = 44100  

        p = pyaudio.PyAudio()  

        print('Recording')

        stream = p.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

        frames = []

        for i in range(0, int(fs / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        print('Finished recording')

        wf = wave.open(filename, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

    def play_voice(self, filename):
        chunk = 1024  

        wf = wave.open(filename, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(chunk)

        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()

        p.terminate()
```