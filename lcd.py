import time

import Adafruit_CharLCD as LCD

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

def displayScore(points):
    lcd.clear()
    lcd.message('POINTS\n')
    lcd.message(str(points))
    
def displayText(text):
    lcd.clear()
    lcd.message(text)
        
def displayTimesUp():
    lcd.clear()
    lcd.message('GAME OVER')

def displayConfigFruit(fruit):
    lcd.clear()
    lcd.message('TOUCH FRUIT:\n')
    lcd.message(fruit)