#GPIO 17
import RPi.GPIO as GPIO
import time

#first, read the GPIO
#while, if GPIO true, print detacted
#channel = 33

GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel,GPIO.IN)

SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

def init():
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    pass

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)
    
    GPIO.output(clockpin, False)
    GPIO.output(cspin, False)
    
    commandout = adcnum
    commandout |= 0x18
    commandout <<= 3
    for i in range(5):
        if(commandout & 0x88):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<=1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
    
    adcout = 0
    
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1
            
    GPIO.output(cspin, True)
    
    adcout >>= 1
    return adcout

photo_ch = 4

def main():
    init()
    
    while True:
        photo_value= readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
        if photo_value >= 650:
            print ("Over 650")
            time.sleep(1)
        
        print ("The light intensity is : ")
        #print (str(((1024-photo_value)/1024.*100)))
        print(photo_value)
        time.sleep(1)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    
    
GPIO.cleanup()