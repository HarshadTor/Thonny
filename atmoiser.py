from machine import Pin
import utime as time
from dht import DHT11

dataPin=16

myPin= Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor=DHT11(myPin)
print("my sensor data")
while True:
    sensor.measure
    hum=sensor.humidity()
    tempC=sensor.temperature()
    print("\r",hum,tempC, end='')
    time.sleep(2)