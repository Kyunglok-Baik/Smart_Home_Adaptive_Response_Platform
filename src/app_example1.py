#!/usr/bin/env python3
import sensors

print('What do you want to know?')
print('1:temperature, 2:brightness')

while True:
    select=int(input())
    
    try:
        if select==1:
            print(sensors.temp_c)
        else:
            print(sensors.bright)
    except:
        pass

