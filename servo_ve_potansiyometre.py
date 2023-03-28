from machine import Pin,PWM,ADC
from time import sleep

servo = PWM(Pin(0))
potentiometer = ADC(28)
servo.freq(50)


in_min = 0
in_max = 65535

out_min = 1000
out_max = 9000


while True:

    value = potentiometer.read_u16()
    Servo = value/65535*8000+1000
    servo.duty_u16(int(Servo))
    print(f"{value}\n\n")
    print(f"{Servo}\n\n")
    sleep(0.08)