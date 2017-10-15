import random
from speech_test.py import callFruit
from touch_test.py import touchedFruit

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
        
        

        fruitTouched = touchedFruit()
        if fruitTouched == "lime" and fruit == 0:
            points += 1
        elif fruitTouched == "lemon" and fruit == 1:
            points += 1
        elif fruitTouched == "orange" and fruit == 2:
            points += 1

main()

