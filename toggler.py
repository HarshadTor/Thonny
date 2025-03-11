from machine import Pin
from time import sleep
while True:
    myLED=Pin(2,Pin.OUT)
    myLED.value(1)
    sleep(1)
    