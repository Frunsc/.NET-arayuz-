import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import _thread

ssid = 'SUPERONLINE_WiFi_5521'
password = 'ZcCkeNHY2eAC'

def connect():
    #baglan WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Baglanti bekleniyor...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Baglanti kuruldu ip --> {ip}')
    return ip
    
    
    
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(sicaklik, durum):
    #HTML kodu
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Wifi kontrolcusu</title>
            <meta http-equiv= "refresh" content="5">
            </head>
            <body>
            <form action="./ac">
            <input type="submit" value="Isigi ac" />
            </form>
            <form action="./kapat">
            <input type="submit" value="Isigi kapat" />
            </form>
            <p>LED {durum}</p>
            <p>Hava sicakligi {sicaklik}</p>
            </body>
            </html>
            """
    return str(html)


def serve(connection):
    durum = 'KAPALI'
    pico_led.off()
    sicaklik = 0
    while True:
        client = connection.accept()[0]

        
        request = client.recv(1024).decode()
        request = str(request)
        print(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        #komutlar
        if request == '/ac?':
            pico_led.on()
            durum = 'ACIK'
        elif request =='/kapat?':
            pico_led.off()
            durum = 'KAPALI'
        sicaklik = pico_temp_sensor.temp
        
        
        html = webpage(sicaklik, durum)
        client.send(html)
        
        
        client.close()

        
        

    
    


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()