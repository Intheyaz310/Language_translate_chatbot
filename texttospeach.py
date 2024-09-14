from gtts import gTTS
import os

text = "Hello, this is a text-to-speech conversion!"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
os.system("start output.mp3")  # Opens the generated file using the default audio player
