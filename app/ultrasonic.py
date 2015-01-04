#ultrasonic sensor control routes

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


@app.route('/ultrasonic/range')
def range():

	TRIG = 23
	ECHO = 24
	CONTROL = 4

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
	GPIO.setup(CONTROL,GPIO.OUT)

	pulse_start = 0
	pulse_end= 0
	distance = 0
	count =0

	while True:
		GPIO.output(TRIG, False)
		print "Waiting For Sensor To Settle"
		time.sleep(0.5)

		#print "Pulse Start"
		GPIO.output(TRIG,True)
		time.sleep(0.00001)
		GPIO.output(TRIG,False)
		#print "Pulse Stop"

		pulse_start = time.time()
		while GPIO.input(ECHO)==0:
			pulse_start = time.time()
			#print "Echo is 0"

		while GPIO.input(ECHO)==1:
			pulse_end = time.time()
			#print "Echo is 1"

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)
		count=count+1
		if count>3 or (distance > 6 and distance <3300):
			print "Distance: ", distance, "cm"
			return jsonify(distance = distance, count= count)