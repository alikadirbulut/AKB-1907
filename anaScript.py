import RPi.GPIO as gpio
import time
import sys
import tkinter as tk

def init():
    gpio.cleanup()
    gpio.setmode(gpio.BOARD)
    gpio.setup(22, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    

def ileri(tf):
    init()
    gpio.output(22, True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()
 
    
    
def geri(tf):
    init()
    gpio.output(22, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def sol(tf):
    init()
    gpio.output(22, False)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def sag(tf): 
    init()
    gpio.output(22, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

    
def key_input(event):
    init()
    print ('Key:', event.char)
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        ileri(sleep_time)
    elif key_press.lower() == 's':
        geri(sleep_time)
    elif key_press.lower() == 'a':
        sol(sleep_time)
    elif key_press.lower() == 'd':
        sag(sleep_time)
    else:
        gpio.cleanup()

root = tk.Tk()
root.bind('<KeyPress>', key_input)
root.mainloop()


