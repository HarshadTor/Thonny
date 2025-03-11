from machine import Pin
from time import sleep
from dht import DHT11


dataPin=16
myPin= Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor=DHT11(myPin)
while True:
    sensor.measure()
    hum=str(sensor.humidity())
    tempc=str(sensor.temperature)
    print(tempc)
    print(hum)





    

