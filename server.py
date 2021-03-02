from flask import Flask, redirect, request, jsonify
import soundfile as sf
import librosa
import numpy as np
from os import system

import math

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
  f0, _, prob = librosa.pyin(data, sr=sr, fmin=65, fmax=2093, frame_length=512)

  return jsonify({'voiced_prob': np.nanmean(prob),
                  "f0": np.nanmean(f0),
                  "stddev": np.nanstd(f0),
                  'syllable_estimate': count_syllables(f0)})


def count_syllables(f0):
  n = 0
  br  = False
  for i in f0:
    if math.isnan(i):
      if br:
        n += 1
      br = False
    else:
      br = True

  return n

if __name__ == '__main__':
  app.run()
