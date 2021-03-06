#Christmas Tree Lights Route

from flask import render_template
from flask import jsonify
import platform as platform

if platform.platform()[0:5] == 'Linux':
	import RPi.GPIO as GPIO
else:
	import mockGPIO as GPIO 
import time


from app import app

@app.route('/lights/<state>/<channel>')
def on(state,channel):

#Check the channel and lookup the correct RPi GPI Pin
	if(channel == "1"):
		pin = 4
	elif(channel == "2"):
		pin = 17
	elif(channel == "3"):
		pin = 27
	elif(channel =="4"):
		pin = 22
	else:
		pin = -1

	app.logger.info('Channel ' + channel + ' has been set to ' + state)
	app.logger.info('Channel ' + channel + ' corresponds to pin ' + str(pin))

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	
	if(state == 'on'):
		GPIO.output(pin,False)
		app.logger.info('Pin ' + str(pin) + ' has been set to False (On)')
		return jsonify(lights="On", channel = channel)
	elif (state =='off'):
		GPIO.output(pin,True)
		app.logger.info('Pin ' + str(pin) + ' has been set to True (Off)')
		return jsonify(lights="Off", channel = channel)
	else:
		return jsonify(error="No state passed")
