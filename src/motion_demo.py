#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

M_pin = 12 #Select the pin for motionsensor

def init():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(M_pin,GPIO.IN)
	pass

def detct():
    for i in range(101):
        if GPIO.input(M_pin):
            print ("Someone is coming!")
        else:
            print ("Nothing")
        time.sleep(0.5)
def detect2():		
    if GPIO.input(M_pin):
        print ("Someone is coming!")
    else:
        print ("Nothing")
    time.sleep(2)

def start():
    time.sleep(0.5)
    init()
    detct()
    GPIO.cleanup()
    
    
def start2():
    while True:
        init()
        detect2()
        GPIO.cleanup()



    

