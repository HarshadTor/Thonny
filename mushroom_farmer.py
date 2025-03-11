from machine import Pin, ADC
import utime as time
from dht import DHT11
import math


motorPin=6
motorPin2=7
enablePin=8
dataPin=16
switch=18
switch2=10
switch3=11
switch4=12
heatPin=26
lightPin=28

a= 0.001129148
b= 0.000234125
c= 0.0000000876741

thermistor= ADC(heatPin)
heat= thermistor.read_u16()

ldr=ADC(lightPin)
intensity=ldr.read_u16()

myPin= Pin(dataPin,Pin.OUT,Pin.PULL_DOWN)
sensor=DHT11(myPin)



relay = Pin(switch, Pin.OUT)
relay2 = Pin(switch2, Pin.OUT)
relay3 = Pin(switch3, Pin.OUT)
relay4 = Pin(switch4, Pin.OUT)
rotor= Pin(motorPin,Pin.OUT)
rotor2= Pin(motorPin2,Pin.OUT)
enable= Pin(enablePin,Pin.OUT)

Vin= 3.3
Ro=10000
Vout=(3.3/65535)*heat
Rt=(Vout*Ro)/(Vin-Vout)

tempK = 1 / (a + (b * math.log(Rt)) + c * math.pow(math.log(Rt), 3))

tempW=tempK-273.15
print("my sensor data")

enable.high()

while True:
    sensor.measure
    hum=sensor.humidity()
    tempC=sensor.temperature()
    print(hum, tempC, tempW, intensity, Vout)
    
while tempC>26:
    while tempW>26:
        relay2.value(1)
        while hum<80:
            relay3.value(1)
        while hum>90:
            relay3.value(0)
            relay4.value(1)

while tempC<=21:
    while tempW<=21:
        relay2.value(1)
        while hum<80:
            relay3.value(0)
        while hum>90:
            relay3.value(0)
    
relay.value(0)
relay2.value(0)
relay3.value(0)
relay4.value(0)

if x==0:
    rotor.value(1)
    time.sleep(1)
    rotor.value(0)
    time.sleep(1)
    rotor.value(1)
    time.sleep(1)
    rotor.value(0)
    
if x==1:
    rotor.value(1)
    time.sleep(5)
    rotor.value(0)


