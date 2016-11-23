from flask import render_template
import platform as platform

if platform.platform()[0:5] == 'Linux':
	import RPi.GPIO as GPIO
else:
	import mockGPIO as GPIO 

from app import app

import socket
print(socket.gethostname())

@app.route('/')
@app.route('/index')
def index():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.OUT)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(22,GPIO.OUT)
	GPIO.setup(27,GPIO.OUT)
	#Check the status of the 4 pins
	states = [GPIO.input(4), GPIO.input(17), GPIO.input(22), GPIO.input(27)]

	return render_template('index.html', title='Home', host=socket.gethostname(), states=states)