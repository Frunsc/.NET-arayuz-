import time 
import machine
from picozero import pico_temp_sensor, pico_led
i=0
while True:
    i=i+1
    pico_led.on()
    time.sleep(1)
    pico_led.off()
    time.sleep(1)
    print(i)
    