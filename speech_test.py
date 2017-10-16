import requests
r = requests.post("http://10.42.0.1:5000/tts/", data={'text': 'woooo'})
r = requests.post("http://10.42.0.1:5000/tts/", data={'text': 'this is a test'})
r = requests.post("http://10.42.0.1:5000/tts/", data={'text': 'multiple test phrases'})
r = requests.post("http://10.42.0.1:5000/tts/", data={'text': 'ORANGE APPLE PEAR BANANA'})
