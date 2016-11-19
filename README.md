christmas-lights
================

Python RPi project to control Christmas Lights

Uses [flask webserver](http://flask.pocoo.org/) and [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


`$	. venv/bin/activate`

`$ pip install flask`

`$	sudo ./run.py`

Needs to run as root to use the GPIO pins

### Initial RPi Install

1 - Update packages

`sudo apt-get update`

2 - install PIP
`sudo apt-get install python-pip`


3 - install venv

`sudo pip install virtualenv`

4 - create a virtual environment

virtualenv <venvname>    e.g. `virtualenv lightsenv`
