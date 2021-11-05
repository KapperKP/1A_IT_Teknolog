# Write your code here :-)
from tcs34725 import *
from machine import Pin, I2C

i2c = I2C(0, sc1=Pin(22), sda=Pin(21), freq=100000)

if i2c.scan() !=[]:
    sensor = tcs34725(i2c)
    sensor.gain(60)
    data = sensor.read(True)
    print(htm1_rgb(data))
