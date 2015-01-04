# solenoid control routes

from flask import render_template
from flask import jsonify
import platform as platform
if platform.platform()[0:5] == 'Linux':
	import RPi.GPIO as GPIO
else:
	#import RPi.GPIO as GPIO
	import mockGPIO as GPIO 
	#TODO: Create a mock GPIO library
import csv
import datetime
import time
import sqlwrite



from app import app

@app.route('/solenoid/short')
def solenoid_on():

	short_pulse = float(175)/1000

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25,GPIO.OUT)
	GPIO.output(25,False)
	time.sleep(short_pulse)
	GPIO.output(25,True)
	print "Sending short pulse of ",short_pulse, "s to solenoid"

	marble_launch_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')

	#Write to the SQL Database
	sqlwrite.write_marble(marble_launch_time,'Marble launched','Single',1,1)

	return jsonify(solenoid="Pulsed")


@app.route('/solenoid/long')
def solenoid_long():

	short_pulse = float(175)/1000
	delay = float(1500)/1000
	multiple = 10

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25,GPIO.OUT)
	for x in range(0, multiple):
		GPIO.output(25,False)
		time.sleep(short_pulse)
		GPIO.output(25,True)
		print "Sending pulse of ",short_pulse,"s to solenoid to release marble #", x+1, " of ", multiple

		marble_launch_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')

		#Write to the SQL Database
		sqlwrite.write_marble(marble_launch_time,'Marble launched','Multiple',x+1,multiple)

		time.sleep(delay)

		#TODO: Check if the marble has passed the infrared detector
		#		Otherwise there must be a jam or the funnel is empty of marbles

		print "Waiting for ",delay,"s before sending marble #",x+2
	return jsonify(solenoid="Pulsed")



def pulse_solenoid(count):
	short_pulse = float(175)/1000
	delay = float(1500)/1000
	multiple = 10
