#!/usr/bin/env python3

#import RPi.GPIO as GPIO
#import motion_demo
import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat
import aiy.i18n

import os
import glob
import time

from gtts import gTTS
import tempfile

##M_pin = 12 #Select the pin for motionsensor
##
##def init():
##    GPIO.setwarnings(False)
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(M_pin,GPIO.IN)
##    pass
##
##def detct():
##    if GPIO.input(M_pin):
##        print("Detected")
##        aiy.audio.say("Detected")
##        time.sleep(2)
##    time.sleep(0.1)
#recognizer = aiy.assistant.grpc.get_recognizer()
assistant = aiy.assistant.grpc.get_assistant()

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

print('ready')

with aiy.audio.get_recorder():
    while True:
        print('Speak out loud')
##        init()
##        detct()
##        GPIO.cleanup()
        #motion_demo.start2()
        transcript, audio = assistant.recognize()
        if transcript is not None:
            if 'Ivana' in transcript:
                print('Assistant said', transcript)
                if "temperature" in transcript:
                    t_c,t_f=read_temp()
                    print('C =%3.3f F = %3.3f'% read_temp())
                    
                    cel="{:3.1f}".format(t_c)
                    message='Currently the temperature inside the house is'+cel+' celsius'
                    #aiy.audio.say(message, lang='en-US', pitch=125)
                    
                    tts=gTTS(text=message, lang='en')
                    tts.save("./hello.mp3")
                    f = tempfile.TemporaryFile()
                    tts.write_to_fp(f)
                    f.close()
                    os.startfile("./hello.mp3")
                    

            
