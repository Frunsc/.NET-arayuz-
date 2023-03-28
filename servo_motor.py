from machine import Pin,PWM,ADC
from time import sleep




servo = PWM(Pin(0))
servo.freq(50)

def servo_motor(sure):
    
    zaman=.0
    
    
    
    while zaman<sure:
        servo.duty_u16(2000)
        sleep(0.5)
        servo.duty_u16(8000)
        sleep(0.5)
        zaman=zaman+1
        
    print("stopped")

try:
    servo_motor(5)
    
except KeyboardInterrupt:
    print("machine stopped")
    GPIO.cleanup()