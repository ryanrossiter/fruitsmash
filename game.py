import random
from speech_test.py import sayFruit, sayTimesUp
from touch_test.py import touchedFruit
import signal
from lcd_test.py import displayScore, displayFruit, displayTimesUp

import thread
import threading

#idk if works
def input_with_timeout(timeout):  
    timer = threading.Timer(timeout, thread.interrupt_main)
    astring = None
    try:
        timer.start()
        astring = touchedFruit()
    except KeyboardInterrupt:
        displayTimesUp()
        sayTimesUp()
    timer.cancel()
    return astring

#game structure
def main():
    points = 0
    gameOn = True
    timeToHit = 4
    while (gameOn):
        fruit = random.randint(0,2)
        if fruit == 0:
            callFruit("lime")
        elif fruit == 1:
            callFruit("lemon")
        else:
            callFruit("orange")
        
        #somehow link touchedFruit() function to the interrupting function.

        fruitTouched = input_with_timeout(timeToHit)
        if fruitTouched == "lime" and fruit == 0:
            points += 1
        elif fruitTouched == "lemon" and fruit == 1:
            points += 1
        elif fruitTouched == "orange" and fruit == 2:
            points += 1
    
    displayScore(points)
    
    
main()

