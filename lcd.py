import time

import Adafruit_CharLCD as LCD

def displayScore(points):
    lcd.message('POINTS')
    lcd.message(points)
    
def displayFruit(fruit):
    if fruit.lower() == "lemon":
        lcd.message('LEMON')
    if fruit.lower() == "lime":
        lcd.message('LIME')
    if fruit.lower() == "orange":
        lcd.message('ORANGE')
        
def displayTimesUp():
    lcd.message('GAME OVER')