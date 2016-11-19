christmas-lights
================

Python RPi project to control Christmas Lights

Uses [flask webserver](http://flask.pocoo.org/) and [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


### Initial RPi Install

1 - Update packages

`sudo apt-get update`

2 - install PIP
`sudo apt-get install python-pip`

3 - install venv

`sudo pip install virtualenv`

4 - create a virtual environment

virtualenv <venvname>    e.g. `virtualenv lightsvenv`

5 - Clone the repository

`git clone https://github.com/alangobrown/christmas-lights.git <venvname>`

6 - Initiate git
`cd <venvname>`
`git init`
`cd ../`

7 - Create the virtual environment

`virtualenv <venvname>`

8 - Activate it

`$	. <venvname>/bin/activate`

9 - Install Flask

`cd <venvname>`
`$ sudo pip install flask`
cd `../`

10 - Run the app
`$	sudo python <venvname>/run.py`
