import sys

import Adafruit_MPR121.MPR121 as MPR121

print('Initializing touch sensor...')

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

def waitForTouch():
    touched = cap.touched()
    while touched == 0:
        touched = cap.touched()

    for i in range(12):
        pin_bit = 1 << i
        if touched & pin_bit:
            return touched

    return -1
