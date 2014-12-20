from flask import render_template
import RPi.GPIO as GPIO

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/on')
def on():


	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)
	GPIO.output(7,False)
	pin7 = str(GPIO.input(7))
	return 'Switched the lights on.  Current status is ' + pin7


@app.route('/off')
def off():

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)
	GPIO.output(7,True)
	pin7 = str(GPIO.input(7))
	return 'Switched the lights off.  Current status is ' + pin7