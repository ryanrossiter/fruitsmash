import requests

def say(text):
    try:
        requests.post("http://10.42.0.1:5000/tts/", data={'text': text})
    except Exception:
        print("Failed to communicate with api server")

def postHighscore(points):
    try:
        requests.post("http://10.42.0.1:5000/score/", data={'points': points})
    except Exception:
        print("Failed to communicate with api server")