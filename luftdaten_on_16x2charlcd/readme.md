luftdaten_to_charlcd.py is a script that lets your weather data which you collect with your NodeMCU display on an Adafruit 16x2 CharLCD.

In order to make it all work follow the following steps:

*1. Equip your NodeMCU / ESP8266 with a few weather sensors, e.g. a fine dust sensor SDS011 or temperature and pressure sensors (like the BME280).
*2. Flash the NodeMCU properly with the luftdaten script and ultimately integrate it into your LAN. Make sure it recognizes all the sensors you have connected. The instructions can be found on the lufdaten.info website (https://luftdaten.info/en/construction-manual/).
*3. find out the IP address that your ESP8266 was given by your router, either via the router settings or an IP mapping tool. On linux terminal '''nmap -sP 192.168.62.1/24''' should do the trick

