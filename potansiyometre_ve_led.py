from machine import ADC, Pin, PWM
import time

potent = ADC(26)
led = PWM(Pin(13))
led.freq(1000)


def ptled():
    while True:
        yuzde= round(potent.read_u16()/652470*100)
        print(f"potansiyometrenin degeri --> {potent.read_u16()}\n\nyuzdelik deger\t\t -->{round(yuzde)}")
        led.duty_u16(potent.read_u16())
        time.sleep(0.1)
        
try:
    ptled()
except KeyboardInterrupt:
    led.duty_u16(0)
    
