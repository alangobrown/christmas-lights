#!/bin/bash



#Fetch the code from bitbucket repo
cd /home/pi/lightsvenv/
git checkout .
git pull origin master


#Restart the service

sudo systemctl restart lights.service


