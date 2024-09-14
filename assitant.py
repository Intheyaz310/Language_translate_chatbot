import sounddevice as sd
import numpy as np
from gtts import gTTS
import tempfile
import os
import speech_recognition as sr
import pygame
import time

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    # Create a temporary directory to store the audio file
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_file_path = os.path.join(temp_dir, 'output.mp3')

        # Generate speech audio file
        tts = gTTS(text=text, lang='en')
        tts.save(temp_file_path)

        # Play speech audio file
        pygame.init()
        pygame.mixer.init()
        if os.path.exists(temp_file_path):
            pygame.mixer.music.load(temp_file_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        else:
            print("Audio file not found.")

        # Wait for a short duration before cleanup
        time.sleep(3)  # Adjust this delay based on the length of your audio

# Rest of the code remains the same...
def print_devices():
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        print(f"Device {idx}: {device['name']}, Input channels: {device['max_input_channels']}")

def listen():
    print("Available input devices:")
    print_devices()
    
    device_index = int(input("Enter the device index to use for recording: "))
    fs = 44100  # Sample rate

    try:
        print("Listening...")
        with sd.InputStream(device=device_index, channels=1, samplerate=fs, dtype=np.int16) as source:
            audio = []
            while True:
                rec_chunk, overflowed = source.read(fs)
                audio.append(rec_chunk)
                if len(audio) > 5 * fs:
                    break

        audio_array = np.concatenate(audio)
        print("Recognizing...")
        query = recognizer.recognize_google(audio_array, language="en-US", show_all=False)
        print("You said:", query)
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("I'm sorry, I couldn't access the recognition service.")
        return ""

if __name__ == "__main__":
    speak("Hello! How can I assist you?")

    while True:
        command = listen()

        if "exit" in command:
            speak("Goodbye!")
            break

        if command:
            # Your task execution logic here based on the recognized command
            pass  # Placeholder for task execution logic