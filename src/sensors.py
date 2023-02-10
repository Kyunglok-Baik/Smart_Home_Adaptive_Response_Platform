#!/usr/bin/env python3
import threading
import time

#import sensor.temperature as temperature
#import sensor.light as light
from sensor import temperature
from sensor import light

global temp_c,temp_f
global bright

def get_temp(rate):
    global temp_c,temp_f
    print("get temp")
    
    while True:
        temp_c,temp_f=temperature.read_temp()
        #print(temp_c)
        time.sleep(rate)
        
def get_light(rate):
    print("get light")
    light.init()
    global bright
    
    while True:
        bright=light.read_light()
        #print(bright)
        time.sleep(rate)
        



temperature_sensor=threading.Thread(target=get_temp,args=(2,))
temperature_sensor.start()

#photon_sensor=threading.Thread(target=get_light,args=(1,))
#photon_sensor.start()


    