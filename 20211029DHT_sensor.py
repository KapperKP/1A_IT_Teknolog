# Write your code here :-)
from machine import Pin
import dht
from time import sleep

sensor = dht.DHT11(Pin(14))

sensor.measure()
sleep(2)
temp = sensor.temperature()
hum = sensor.humidity()
print(hum, temp)
