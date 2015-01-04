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

import sqlite3 as lite
import sys


from app import app

#############################################
# Releases one or more marbles
#############################################
@app.route('/solenoid/short')
def solenoid_on():

	#Call the function to pulse the solenoid and release a marble
	solenoid_pulse(1)

	return jsonify(solenoid="Pulsed")


#############################################
# Releases one or more marbles
#############################################
@app.route('/solenoid/long')
def solenoid_long():

	#Call the function to pulse the solenoid and release a lot of marbles
	solenoid_pulse(4)

	return jsonify(solenoid="Pulsed")


#############################################
# Display Log of Marble Launches
#############################################
@app.route('/solenoid/log')
def solenoid_log():


	con = lite.connect('marbles.db')

	with con:    
	    
	    cur = con.cursor()    
	    cur.execute("SELECT * FROM Launches order by LaunchDate desc")

	    marbles = cur.fetchall()

	    for marble in marbles:
	        print marble

	return render_template('log.html', title='Marbles Log', marbles = marbles)




#############################################
# Releases one or more marbles
#############################################
def solenoid_pulse(count):

	short_pulse = float(175)/1000
	delay = float(1500)/1000

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25,GPIO.OUT)
	for x in range(0, count):
		GPIO.output(25,False)
		time.sleep(short_pulse)
		GPIO.output(25,True)
		print "Sending pulse of ",short_pulse, "s to solenoid to release marble #", x+1, " of ", count

		marble_launch_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f')

		group = 'Single'
		if count>1:
			group = 'Multiple'
			time.sleep(delay)
			print "Waiting for ",delay,"s before sending marble #",x+2

		#Write to the SQL Database
		sqlwrite.write_marble(marble_launch_time,'Marble launched',group,x+1,count)