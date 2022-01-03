import RPi.GPIO as gpio
import time
import sys
import tkinter as tk
from threading import *
from sensor import distance


def init():
    gpio.cleanup()
    gpio.setmode(gpio.BOARD)
    gpio.setup(29, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    

def ileri(tf):
    init()
    gpio.output(29, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()
   
def geri(tf):
    init()
    gpio.output(29, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(29, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


def sag(tf): 
    init()
    gpio.output(29, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()
    
def fren(tf):
    gpio.output(29, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    gpio.cleanup()
    
def stop(tf):
    fren()
    gpio.cleanup()
    


def key_input(event):
    init()
    print ('Key:', event.char)
    key_press = event.char
    sleep_time = 0.030
    

    if key_press.lower() == 'w':
        ileri(sleep_time)
        
    if key_press.lower() == 's':
        geri(sleep_time)
        
    if key_press.lower() == 'a':
        sol(sleep_time)        
    if key_press.lower() == 'd':
        sag(sleep_time)
        
    if key_press.lower() == 'd':
        sag(sleep_time)
        
    else:
        gpio.cleanup()
        
#     curDis = distance('cm')
#     print('anlikMesafe', curDis)
#     if curDis <12:
#         sys.exit()

root = tk.Tk()
root.bind('<KeyPress>', key_input)
root.mainloop()


