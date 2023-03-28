from machine import Pin, ADC
from time import sleep,sleep_ms


IN1 = Pin(2,Pin.OUT)
IN2 = Pin(3,Pin.OUT)
IN3 = Pin(4,Pin.OUT)
IN4 = Pin(5,Pin.OUT)

pins = [IN1, IN2, IN3, IN4]

saat_yonu = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
saat_yonu_tersi = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

def move_forward():
    while True:
        for step in saat_yonu:
            for i in range(len(pins)):           
                pins[i].value(step[i])
                sleep_ms(2)
                
def move_backward():
    while True:
        for step in saat_yonu_tersi:
            for i in range(len(pins)):           
                pins[i].value(step[i])                   
                sleep_ms(5)

def servo_motor():
    
    zaman=.0
    sure=5.0
    
    while zaman<sure:
        servo.duty_u16(2000)
        sleep(0.5)
        servo.duty_u16(8000)
        sleep(0.5)
        zaman=zaman+1
 
 
try:
    move_forward()

except KeyboardInterrupt:
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    led.value(0)

 