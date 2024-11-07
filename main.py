import os
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk  # Use ttk for modern UI elements
import numpy as np
import whisper
import torch
import speech_recognition as sr
from datetime import datetime, timedelta, timezone
import re

# Import Flask and CORS for API mode
from flask import Flask, request, jsonify
from flask_cors import CORS


react_ui = True

# Initialize transcription list and frames
transcriptions = []
frames = []
phrase_time = None
transcription_active = False  # Keeps track of whether transcription is active
listener = None  # To hold the background listener instance

# Initialize speech recognition
recorder = sr.Recognizer()
recorder.energy_threshold = 1000
recorder.dynamic_energy_threshold = False

# Microphone initialization
source = sr.Microphone(sample_rate=16000)

# Adjust for ambient noise
with source:
    recorder.adjust_for_ambient_noise(source)

# Load Whisper model
audio_model = whisper.load_model('small.en')



### REACT UI
# Record audio callback
# Flask setup for API mode
app = Flask(__name__)
CORS(app)  # Enable CORS if React frontend is served separately

def record_callback(_, audio):
    """Callback to capture audio frames in the background."""
    print("Recording callback invoked")
    frames.append(audio.get_raw_data())

def start_transcription():
    """Start or stop transcription based on the current state."""
    global transcription_active, listener, phrase_time

    if not transcription_active:
        # Start background listening with a 2-second phrase time limit
        listener = recorder.listen_in_background(source, record_callback, phrase_time_limit=2)
        transcription_active = True
    else:
        # Pause the transcription (stop background listening)
        if listener:
            listener(wait_for_stop=False)  # Stop the background listener
            listener = None
        transcription_active = False

@app.route('/transcription', methods=['GET'])
def get_transcription():
    """Endpoint for React to retrieve the latest transcription."""
    print("GET request received at /transcription")
    if frames:
        print("frames exist")
        # Combine frames and process with Whisper
        audio_data = b''.join(frames)
        frames.clear()
        audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
        result = audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
        transcription = result['text'].strip()

        # Add to transcriptions list
        transcriptions.append(transcription)

        # Send the latest transcription
        return jsonify({"transcription": transcription})
    else:
        return jsonify({"transcription": ""})  

if react_ui:
    start_transcription()  # Start transcription before running the Flask server
    # Only run Flask server if React UI is enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
    exit()

### TKINTER UI

# Define the function to capture audio and transcribe
def record_callback(_, audio):
    frames.append(audio.get_raw_data())

def start_transcription():
    global transcription_active, listener, phrase_time

    if not transcription_active:
        # Start background listening
        listener = recorder.listen_in_background(source, record_callback, phrase_time_limit=2)
        toggle_button.config(text="Pause Transcription")  # Change to "Pause"
        transcription_active = True
        window.after(100, update_transcription)  # Start updating the transcription
    else:
        # Pause the transcription (stop background listening)
        if listener:
            listener(wait_for_stop=False)  # Stop the background listener
            listener = None
        toggle_button.config(text="Start Transcription")  # Change to "Start"
        transcription_active = False

# Function to update transcription results in real-time
def update_transcription():
    global phrase_time, transcription_active

    if not transcription_active:
        return  # Stop updating if transcription is paused

    now = datetime.now(timezone.utc)
    
    if not frames:
        window.after(100, update_transcription)  # Retry after 100ms
        return

    phrase_complete = False
    if phrase_time and now - phrase_time > timedelta(seconds=3):
        phrase_complete = True
    phrase_time = now

    # Combine frames and transcribe
    audio_data = b''.join(frames)
    frames.clear()

    # Convert to Whisper-compatible format
    audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
    result = audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
    text = result['text'].strip()

    if phrase_complete or not transcriptions:
        transcriptions.append(text)
    else:
        transcriptions[-1] = re.sub(r'\.$', '', transcriptions[-1])
        transcriptions[-1] += f' {re.sub(r"^[A-Z]", lambda x: x.group(0).lower(), text)}'

    # Update UI
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, "\n".join(transcriptions))

    # Continue updating if transcription is active
    if transcription_active:
        window.after(100, update_transcription)

# Save transcriptions to file when done
def save_transcriptions():
    with open('transcriptions.txt', 'w') as f:
        for line in transcriptions:
            f.write(line + '\n')
    text_box.insert(tk.END, "\nTranscriptions saved to transcriptions.txt")


# Create UI using Tkinter and ttk for modern elements
window = tk.Tk()
window.title("Whisper Speech-to-Text Transcription")

# Set minimum window size and make it resizable
window.minsize(600, 400)
window.geometry('700x500')  # Starting size

# Configure grid to handle dynamic resizing
window.columnconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

# Create a frame for content with padding
content_frame = ttk.Frame(window, padding="10 10 10 10")
content_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Add styling options
text_box_font = ("Arial", 12)
button_font = ("Arial", 12, "bold")

# Create transcription text box with scrollable view, using `ttk` for modern styling
text_box = scrolledtext.ScrolledText(content_frame, width=60, height=15, wrap=tk.WORD, font=text_box_font)
text_box.grid(column=0, row=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create toggle button for start/pause transcription using ttk
toggle_button = ttk.Button(content_frame, text="Start Transcription", command=start_transcription)
toggle_button.grid(column=0, row=1, pady=10, sticky=tk.EW)

# Create save button using ttk
save_button = ttk.Button(content_frame, text="Save Transcriptions", command=save_transcriptions)
save_button.grid(column=0, row=2, pady=10, sticky=tk.EW)

# Make sure the text box expands with window resizing
content_frame.rowconfigure(0, weight=1)
content_frame.columnconfigure(0, weight=1)

window.mainloop()
