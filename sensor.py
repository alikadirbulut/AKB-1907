import RPi.GPIO as gpio
import time

def distance (measure = 'cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(32, gpio.OUT)
    gpio.setup(16, gpio.IN)
    
    gpio.output(32, False)
    while gpio.input(16) == 0:
        nosig  =  time.time()
        
    while gpio.input(16)== 1:
        sig = time.time()
        
    t1 = sig-nosig
    
    if measure == 'cm':
        distance = t1 / 0.000058
    elif measure == 'in':
        distance = t1 / 0.000148
    else:
        print('yaklasik olcum inc ya da cm')
        distance = None
    gpio.cleanup()
    return distance

print (distance('cm'))