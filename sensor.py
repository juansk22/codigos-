from dht import DHT11
from machine import Pin
from utime import sleep

sensorDHT = DHT11(Pin(15))

while True:
    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    kelvin = temp + 273
    
    print("T={:02d}°c, H={:02d}% k={:02d}k".format(temp,hum,kelvin))
   