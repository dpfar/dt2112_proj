from flask import Flask, redirect, request, jsonify
import speech_recognition as sr
import soundfile as sf
import librosa
import numpy as np
from os import system

app = Flask(__name__, static_url_path='/', static_folder='static')

@app.route('/')
def display_page():
  print('alsdjfalsdkjfasldkfjasdf')
  return redirect('index.html', code=302)

@app.route('/thing', methods=['POST'])
def thing():
  f = request.files['file']
  f.save(f.filename) # Saves the file
  wav_filename = 'tmp.wav'
  # Convert to wav (file is in ogg format, so thing don't work with sf or sr)
  system('ffmpeg -i {} {}'.format(f.filename, wav_filename))
  data, samplerate = sf.read(f)

  #sf.write('tmp.wav', data, samplerate) # convert to wav
  recognizer = sr.Recognizer()
  audiofile = sr.AudioFile(wav_filename)
  with audiofile as source:
    data = recognizer.record(source)
  transcript = recognizer.recognize_google(data, key=None)
  return jsonify({'asr_result': transcript})

if __name__ == '__main__':
  app.run()
