from flask import Flask, request
import pyttsx

app = Flask(__name__)
engine = None

highscores = []

def say(text):
    engine = pyttsx.init()
    engine.say(text)
    a = engine.runAndWait()

@app.route('/tts/', methods=['POST'])
def tts():
    print(request.form['text'])
    say(request.form['text'])
    return 'GOT IT!'

@app.route('/score/', methods=['POST'])
def postScore():
    print("Got score: %s" % request.form['points'])
    highscores.append(request.form['points'])
    highscores.sort()
    highscores.reverse()
    return 'GOT IT!'

@app.route('/leaderboard/', methods=['GET'])
def getLeaderboard():
    return """
    <html><body>
    <h1>Fruit Smash Leaderboard</h1>
    <ol><li>%s</li></ol>
    </html></body>
    """ % "</li><li>".join(highscores)
    

say('FRUIT SMASH SERVER INITIALIZED')