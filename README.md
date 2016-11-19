christmas-lights
================

Python RPi project to control Christmas Lights

Uses [flask webserver](http://flask.pocoo.org/) and [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


`$	. <venvname>/bin/activate`

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

5 - Initiate git

`git init`

6 - Clone the repository

