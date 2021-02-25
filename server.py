from flask import Flask, redirect, request, jsonify
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
  system('ffmpeg -y -i {} -ac 1 {}'.format(f.filename, wav_filename))
  data, sr = librosa.load(wav_filename)
  spectrogram = librosa.feature.melspectrogram(y=data, sr=sr)
  f0, _, _ = librosa.pyin(data, sr=sr, fmin=65, fmax=2093)

  recognizer = Recognizer()
  #audiofile = AudioFile(wav_filename)
  #with audiofile as source:
    #data = recognizer.record(source)
  #transcript = recognizer.recognize_google(data, key=None)
  return jsonify({'asr_result': 'asdfbasldfjaskldfjlasdf', "f0": np.nanmean(f0)})

if __name__ == '__main__':
  app.run()
