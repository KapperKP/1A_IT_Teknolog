# Write your code here :-)
from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(14))
while True:
    try:
        sleep(2)
        sensor.measure()
        temp = sensor.temperature()
        print('Temperatur: %3.1f C' %temp)

    except OSError as e:
            print('Failed to read sensor.')

