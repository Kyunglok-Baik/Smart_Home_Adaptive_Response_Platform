#GPIO 17
import RPi.GPIO as GPIO
import time

#first, read the GPIO
#while, if GPIO true, print detacted
channel = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print('detected')

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
    time.sleep(0.1)
