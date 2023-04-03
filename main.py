import machine
import secrets #arquivo contendo credenciais do WIFI
import network
import time
import utime
from umqtt.simple import MQTTClient

#Iniciando sensor de temperatura
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)
led = machine.Pin("LED", machine.Pin.OUT)
led.off()

#Conectando na rede WIFI
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)
max_wait = 10

while max_wait > 0:
 if wlan.status() < 0 or wlan.status() >= 3:
  break
  max_wait -= 1
  print('waiting for connection...')
  time.sleep(1)
print(wlan.ifconfig())

#https://learn.microsoft.com/pt-br/azure/iot-hub/iot-hub-mqtt-support
#https://learn.microsoft.com/pt-br/cli/azure/iot/hub?view=azure-cli-latest#az-iot-hub-generate-sas-token
CLIENTID_DEVICEID = "<DEVICE ID>"
MQTTSERVER = "<URL DO Azure IoT Hub>"
USERNAME = "<URL DO Azure IoT Hub>/<DEVICE ID>/?api-version=2021-04-12"
PASSWORD = "<SAS TOKEN>"
c = MQTTClient(CLIENTID_DEVICEID,MQTTSERVER,user=USERNAME,password=PASSWORD,ssl=True)

c.connect()
led.on()

#Enviando dados
while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    c.publish(b"devices/raspberrypipicow/messages/events/", f"{{\"temp\": {temperature} }}".encode())
    print(temperature)
    utime.sleep(2)
    
c.disconnect()

