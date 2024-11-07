import os
import numpy as np
import whisper
import torch
import speech_recognition as sr
from flask import Flask, jsonify
from flask_cors import CORS

# Initialize transcription list and frames
transcriptions = []
frames = []
transcription_active = False
listener = None

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

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS if React frontend is served separately

def record_callback(_, audio):
    """Callback to capture audio frames in the background."""
    frames.append(audio.get_raw_data())

def start_transcription():
    """Start or stop transcription based on the current state."""
    global transcription_active, listener
    if not transcription_active:
        listener = recorder.listen_in_background(source, record_callback, phrase_time_limit=2)
        transcription_active = True
    else:
        if listener:
            listener(wait_for_stop=False)
            listener = None
        transcription_active = False

@app.route('/transcription', methods=['GET'])
def get_transcription():
    """Endpoint for React to retrieve the latest transcription."""
    if frames:
        audio_data = b''.join(frames)
        frames.clear()
        audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0
        result = audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
        transcription = result['text'].strip()
        transcriptions.append(transcription)
        return jsonify({"transcription": transcription})
    else:
        return jsonify({"transcription": ""})

# This is the entry point when deployed on Vercel.
# This function is automatically executed when a request hits the endpoint.
def handler(request):
    """Vercel serverless handler for Flask"""
    with app.test_request_context(request.path, method=request.method):
        return app.full_dispatch_request()

