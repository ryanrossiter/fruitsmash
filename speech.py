import requests

def say(text):
    try:
        requests.post("http://10.42.0.1:5000/", data={'text': text})
    except Exception:
        print("Failed to communicate with tts server")