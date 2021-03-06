# dt2112_proj

Dependencies:
* flask
* librosa
* soundfile
* SpeechRecognition
* [speechmetrics](https://github.com/aliutkus/speechmetrics)
* ...probably a few more

The `get_stats.py` script also requires:
* pandas
* tqdm

How to run:
```
$ export FLASK_ENV=development
$ export FLASK_APP=server.py
$ flask run
```
The website should be accessible on `http://localhost:5000`.
