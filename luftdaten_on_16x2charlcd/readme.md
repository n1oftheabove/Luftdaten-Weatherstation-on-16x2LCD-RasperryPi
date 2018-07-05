## luftdaten_to_charlcd

[luftdaten_to_charlcd.py](luftdaten_to_charlcd.py) is a script that lets your weather data - which you collect with your NodeMCU - display on an [Adafruit 16x2 CharLCD](https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/overview) which runs on a RaspberryPi.

In order to make it all work follow the following steps:

1. Equip your NodeMCU / ESP8266 with a few weather sensors, e.g. a fine dust sensor SDS011 or temperature and pressure sensors (like the BME280).
2. Flash the NodeMCU properly with the luftdaten script and ultimately integrate it into your LAN. Make sure it recognizes all the sensors you have connected. The instructions can be found on the lufdaten.info website (https://luftdaten.info/en/construction-manual/).
3. find out the IP address that your ESP8266 was given by your router, either via the router settings or an IP mapping tool. In linux terminal ```nmap -sP 192.168.62.1/24 | grep ESP```should do the trick.

4. Have your Adafruit 16x2 CharLCD correctly installed on your Raspberry Pi move the script to it and customize the values in it as you like. It is necessary that your provide your NodeMCU's IP address.

5. Run the script
```
python3 luftdaten_to_charlcd.py
```
By default, in the first line of your charLCD you will see the temperature in Celcsius as well as the air pressure in mbar. The second line shows the time (in 24h format) and date (in yyyy-mm-dd).

# Possible future functionality

* Toggling between Fahrenheit/Celsius, mbar/Pa, as well as 24h / 12h time format, background lighting color, refresh rate
* make use of the cursor buttons on the 16x2 plate, maybe for toggling
