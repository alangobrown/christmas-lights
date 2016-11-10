christmas-lights
================

Python RPi project to control Christmas Lights

Uses [flask webserver](http://flask.pocoo.org/) and [virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


`$	. venv/bin/activate`

`$ pip install flask`

`$	sudo ./run.py`

Needs to run as root to use the GPIO pins

### Troubleshooting

`$	sudo python ./run.py`    uses the general python interpreter (not the virtualenv one) and will complain of a missing flask module


To install PIP
`sudo apt-get install python-pip`


To install venv

`sudo pip install virtualenv`

Create a virtual environment

virtualenv <venvname>    e.g. `virtualenv lightsenv`
