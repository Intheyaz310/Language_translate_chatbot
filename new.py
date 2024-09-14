import tkinter as tk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
import io

def translate_text():
    text = input_text.get(1.0, "end-1c")
    target_language = target_language_entry.get()
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    output_text.delete(1.0, "end")
    output_text.insert("end", translated_text.text)
    speak(translated_text.text, target_language)

def speak(text, lang):
    tts = gTTS(text=text, lang=lang)
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

def show_supported_languages():
    # Create a new window to display supported languages
    lang_window = tk.Toplevel(app)
    lang_window.title("Supported Languages")
    
    # Create a text widget to show supported languages
    languages_text = tk.Text(lang_window, height=20, width=40)
    languages_text.pack()

    # Display supported languages in the text widget
    for code, language in LANGUAGES.items():
        languages_text.insert(tk.END, f"Code: {code}, Language: {language}\n")

app = tk.Tk()
app.title("Language Translator Chatbot")

# Configure the gradient background
app.configure(bg="#ffcc33")
frame = tk.Frame(app, bg="#ffcc33")
frame.pack()

# Input Text
input_label = tk.Label(frame, text="Enter text to translate:", bg="#ffcc33")
input_label.pack()

input_text = tk.Text(frame, height=6, width=50)
input_text.pack()

# Language Selection for Input Text
input_language_label = tk.Label(frame, text="Select Input Language:", bg="#ffcc33")
input_language_label.pack()

input_language_var = tk.StringVar(app)
input_language_dropdown = tk.OptionMenu(frame, input_language_var, *LANGUAGES.values())
input_language_dropdown.pack()

# Target Language Entry
target_language_label = tk.Label(frame, text="Target Language (e.g., 'fr' for French):", bg="#ffcc33")
target_language_label.pack()

target_language_entry = tk.Entry(frame, width=10)
target_language_entry.pack()

# Translate Button
translate_button = tk.Button(frame, text="Translate", command=translate_text, bg="blue", fg="white")
translate_button.pack()

# Output Text
output_label = tk.Label(frame, text="Translation:", bg="#ffcc33")
output_label.pack()

output_text = tk.Text(frame, height=6, width=50)
output_text.pack()

# Button to display supported languages
lang_button = tk.Button(frame, text="Show Supported Languages", command=show_supported_languages, bg="green", fg="white")
lang_button.pack()

app.mainloop()
