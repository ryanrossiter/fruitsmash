import requests
r = requests.post("http://10.42.0.1:5000/", data={'text': 'woooo'})
r = requests.post("http://10.42.0.1:5000/", data={'text': 'this is a test'})
r = requests.post("http://10.42.0.1:5000/", data={'text': 'multiple test phrases'})
r = requests.post("http://10.42.0.1:5000/", data={'text': 'ORANGE APPLE PEAR BANANA'})

def callFruit(fruit):
    if fruit.lower() == "lime":
        r = requests.post("http://10.42.0.1:5000/", data={'text':'lime'})
    if fruit.lower() == "orange":
        r = requests.post("http://10.42.0.1:5000/", data={'text':'orange'})
    if fruit.lower() == "lemon":
        r = requests.post("http://10.42.0.1:5000/", data={'text':'lemon'})
