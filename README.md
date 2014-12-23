christmas-lights
================

Python RPi project to control Christmas Lights

Uses [flask webserver](http://flask.pocoo.org/) and virtual environments


`$	. venv/bin/activate`

`$	sudo ./run.py`

Needs to run as root to use the GPIO pins

### Troubleshooting

`$	sudo python ./run.py`    uses the general python interpreter (not the virtualenv one) and will complain of a missing flask module