# Raspberry Pi Pico W conectado ao Azure IoT

- Protocolo MQTT
- Linguagem Python
- Biblioteca umqtt.simple MQTTClient
  - https://mpython.readthedocs.io/en/master/library/mPython/umqtt.simple.html
- Suporte ao protocolo MQTT pelo IoT Hub (https://learn.microsoft.com/pt-br/azure/iot-hub/iot-hub-mqtt-support)

## Processo
1. Registro do dispositivo no IoT Hub
2. Geração do SAS Token pelo Azure CLI para autenticação do dispositivo
3. Detalhamento do código fonte
