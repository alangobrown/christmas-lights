#Christmas Tree Lights Route

from flask import render_template
from flask import jsonify
import platform as platform

if platform.platform()[0:5] == 'Linux':
	import RPi.GPIO as GPIO
else:
	#import RPi.GPIO as GPIO
	import mockGPIO as GPIO 
	#TODO: Create a mock GPIO library
import time


from app import app

@app.route('/lights/on')
def on():


	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.OUT)
	GPIO.output(4,False)
	return jsonify(lights="On")



@app.route('/lights/off')
def off():

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.OUT)
	GPIO.output(4,True)
	return jsonify(lights="Off")