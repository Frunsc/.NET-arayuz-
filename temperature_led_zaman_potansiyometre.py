from machine import Pin, I2C, ADC, PWM
from ssd1306 import SSD1306_I2C
import framebuf
import time

potent = ADC(26)
led = PWM(Pin(13))
led.freq(1000)



WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

# display.invert(1)
#display.contrast(100)

def read_temp():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    formatted_temperature = "{:.1f}".format(temperature)
    string_temperature = str("Sicaklik: " + formatted_temperature)
    print(string_temperature)
    return string_temperature
    


def start():
    zaman=0
    while True:
        zaman=zaman+1
        print(zaman)
        display.text("Efran's:",0,0)
        temperature = read_temp()
        display.text(temperature,0,15)
        display.text(str(f"zaman:{zaman} saniye"),0,30)
        display.text(str(f"Led Yuzde:{ptled()}"),0,45)
        display.show()
        display.fill(0)
        
        time.sleep(1)

def ptled():
    
    yuzde= round(potent.read_u16()/65247*100)
    led.duty_u16(potent.read_u16())
    time.sleep(0.1)
    return yuzde
        
    
try:

    start()
except KeyboardInterrupt:
    display.show()
    led.duty_u16(0)
    
    

    

  
    
