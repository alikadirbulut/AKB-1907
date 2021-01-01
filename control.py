import RPi.GPIO as gpio
import sys
import tkinter as tk

# Init pins
gpio.setmode(gpio.BOARD)
gpio.setup(22, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)


def ileri():
    gpio.output(22, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)

def geri():
    gpio.output(22, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    

def sol():
    gpio.output(22, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(11, True)

def sag(): 
    gpio.output(22, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    
def sola_donus():
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(22, True)
    gpio.output(11, False)

def saga_donus():
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(22, False)
    gpio.output(11, True)
 
def fren():
    gpio.output(22, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)

def bosta():
    gpio.output(22, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)

def stop():
    fren()
    gpio.cleanup()