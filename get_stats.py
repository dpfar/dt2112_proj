# This script gathers metrics from the CSRT CVTK corpus
# https://www.kaggle.com/mfekadu/english-multispeaker-corpus-for-voice-cloning
# The corpus is assumed to be unzipped in the ./data/ directory

from server import get_metrics
from os import listdir, walk
from tqdm import tqdm
import pandas as pd


def write_to_file(output_filename):
  n_sentences = 10
  metrics = {}
  path = './data/VCTK-Corpus/VCTK-Corpus/wav48/'
  for directory, _, filenames in tqdm(walk(path), total=109):
    if not directory.split('/')[-1].startswith('p'):#Only include speaker directories
      continue

    for i in range(n_sentences):
      wav_filename = directory + '/' + filenames[i]
      m = get_metrics(wav_filename)
      for k, v in m.items():
        if not k in metrics:
          metrics[k] = []
        metrics[k].append(v)
  
  df = pd.DataFrame(metrics)
  df.to_csv(output_filename, header=True, index=False)
    
if __name__ == '__main__':
  write_to_file('output.csv')


