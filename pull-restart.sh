#!/bin/bash

#Fetch the code from bitbucket repo

cd /home/pi/lightsvenv/
sudo git checkout .
sudo git pull origin master


#Restart the service

HOME=/home/pi
VENVDIR=$HOME/lightsvenv

cd $VENDIR
. $VENVDIR/bin/activate
sudo python $VENVDIR/run.py
