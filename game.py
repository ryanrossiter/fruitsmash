import random
import speech_test.py import callFruit
import touch_test.py import #insert function of using the touch sensor

#game structure

def main():
    points = 0
    gameOn = True
    timeToHit = 3
    while (gameOn):
        fruit = random.randint(0,2)
        if fruit == 0:
            callFruit("lime")
        elif fruit == 1:
            callFruit("lemon")
        else:
            callFruit("orange")
        
        

        fruitTouched = #function using touch sensor
        if fruitTouched == "lime" and fruit == 0:
            points++
        elif fruitTouched == "lemon" and fruit == 1:
            points++
        elif fruitTouched == "orange" and fruit == 2:
            points++
main()

