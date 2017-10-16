import random
from fs_api import say, postHighscore
#from touch_test.py import touchedFruit
from touch import waitForTouch
import signal
from lcd import displayScore, displayText, displayTimesUp, displayConfigFruit

import time
import thread
import threading

#idk if works
def waitForFruitTouch(timeout):  
    timer = threading.Timer(timeout, thread.interrupt_main)
    pin = None
    try:
        timer.start()
        pin = waitForTouch()
    except KeyboardInterrupt:
        displayTimesUp()
        say("TIME'S UP")
    timer.cancel()

    if pin in pins:
        return pins[pin]
    
    return None

fruits = [
    "lime",
    "lemon",
    "orange"
]
pins = {}

def getNextFruit():
    return fruits[random.randint(0, len(fruits) - 1)]

# Tells user to touch fruits in order
def configureFruits():
    displayText("BEGIN\nCONFIGURATION")
    say("BEGIN CONFIGURATION")
    time.sleep(1) # sleep for 2 seconds

    for f in fruits:
        pin = None
        while pin is None or pin in pins:
            displayConfigFruit(f)
            say("Touch " + f)
            pin = waitForTouch()

            if pin in pins:
                displayText("Fruit already\nconfigured")
                say("Fruit already configured")

        pins[pin] = f

#game structure
def main():
    
    pointsToWin = 10
    mainLoop = True
    timeToHit = 2

    configureFruits()
    time.sleep(0.5)

    while mainLoop:
        points = 0
        gameOn = True

        displayText("TOUCH ANY FRUIT\nTO BEGIN")
        say("TOUCH ANY FRUIT TO BEGIN")
        waitForTouch()
        time.sleep(0.5)

        while (gameOn):
            #if points % 5 == 0 and 5 < points < 50:
            #    timeToHit -= 0.3

            currentFruit = getNextFruit()
            displayText("TOUCH FRUIT:\n" + currentFruit)
            say(currentFruit)
            
            #somehow link touchedFruit() function to the interrupting function.

            fruitTouched = waitForFruitTouch(timeToHit)
            
            if fruitTouched == currentFruit:
                # did it
                say("GREAT JOB")
                points += 1

                if points >= pointsToWin:
                    say("CONGRATULATIONS YOU HAVE TOUCHED %d FRUITS" % pointsToWin)
                    say("YOU ARE A WINNER")
                    gameOn = False
            else:
                say("YOU SUCK")
                gameOn = False

            time.sleep(0.2)
        
        say("GAME OVER")
        say("YOU SCORED %d POINTS" % points)
        displayScore(points)
        postHighscore(points) # post to highscore server
        time.sleep(3)
    
main()

