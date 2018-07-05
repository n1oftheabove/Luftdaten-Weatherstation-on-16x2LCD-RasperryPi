#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by n1oftheabove, see github.com/n1oftheabove

import time

import Adafruit_CharLCD as LCD
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import json
from pprint import pprint
import datetime

#-------- USER INPUT SECTION ----------------

# URL info for NodeMCU in your local network
# Insert here the IP (LAN) of your NodeMCU running the luftdaten software
ip = '192.168.62.149'

#-------- END OF USER INPUT SECTION ---------

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

#generating url
url = 'http://'+ip+'/data.json'


# create some custom characters
lcd.create_char(1, [2, 3, 2, 2, 14, 30, 12, 0])
lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

lcd.set_color(1.0,0.0,0.0)
lcd.clear()


while True:
	while True:
		try:
			u = urlopen(url)
		except HTTPError as e:
			lcd.message("Server couldn't\n fulfill request")
			time.sleep(2)
			lcd.message("Error code: ", e.code, "\n trying again in 30sec")
			time.sleep(30)
			continue							#retries the while loop
		except URLError as e:
			lcd.message("Failed to reach\n server")
			time.sleep(2)
			lcd.message("Reason: ", e.reason, "\n trying again in 30sec")
			time.sleep(30)
			continue
		except ValueError as e:
			lcd.message("No Value\n to read")
			time.sleep(2)
			lcd.message("Reason: ", e.reason, "\n trying again in 30sec")
			time.sleep(30)
			continue
		break									#breaks the while loop only when try: succeeds

	resp = json.loads(u.read().decode("utf-8"))
	time_now = datetime.datetime.now()
	
	#assign measured values to variables
	sds011_pm10 = float(resp["sensordatavalues"][0]["value"])
	sds011_pm25 = float(resp["sensordatavalues"][1]["value"])
	dht_t = float(resp["sensordatavalues"][2]["value"])
	dht_hum = float(resp["sensordatavalues"][3]["value"])
	bme280_t = float(resp["sensordatavalues"][4]["value"])
	bme280_hum =float(resp["sensordatavalues"][5]["value"])
	bme280_p = float(resp["sensordatavalues"][6]["value"])			#bme280 value in hPa

	av_t = (dht_t+bme280_t)/2		#calculate temperature average from both sensors
	av_hum = (dht_hum + bme280_hum)/2	#calculate humidity average from both sensors
	bme280_p_mbar = bme280_p/100		#convert bme280 pressure value to mbar

	#Make time appear as e.g. "07:03" not "7:3" if minute or hour is smaller than 10
	if time_now.hour < 10:
		str_hour = "0"+str(time_now.hour)
	else:
		str_hour = str(time_now.hour)
	if time_now.minute < 10:
		str_min = "0"+str(time_now.minute)
	else:
		str_min = str(time_now.minute) 

	
	# show values to the LCD
	lcd.message(str(round(av_t,1))+chr(223) + "C " + str(int(round(bme280_p_mbar))) + "mbar \n"+str_hour+":"+str_min + " " + str(time_now.year)+"-"+str(time_now.month)+"-"+str(time_now.day))
	
	#refresh shown information after 60 seconds
	time.sleep(60)
	
	lcd.clear()
	
