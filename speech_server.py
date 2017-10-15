from flask import Flask, request
import pyttsx

app = Flask(__name__)
engine = None

def say(text):
    engine = pyttsx.init()
    engine.say(text)
    a = engine.runAndWait()

@app.route('/', methods=['POST'])
def result():
    print(request.form['text'])
    say(request.form['text'])
    return 'GOT IT!'

say('BEGIN.')

def callFruit(fruit):
    if fruit.lower() == "lemon":
        say(request.form['lemon'])
    if fruit.lower() == "lime":
        say(request.form['lime'])
    if fruit.lower() == "orange":
        say(request.form['orange'])