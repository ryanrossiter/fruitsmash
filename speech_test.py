import requests
r = requests.post("http://10.42.0.1:5000/", data={'text': 'woooo'})
r = requests.post("http://10.42.0.1:5000/", data={'text': 'this is a test'})
r = requests.post("http://10.42.0.1:5000/", data={'text': 'multiple test phrases'})
r = requests.post("http://10.42.0.1:5000/", data={'text': 'ORANGE APPLE PEAR BANANA'})
