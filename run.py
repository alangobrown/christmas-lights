#!venv/bin/python
from app import app



import csv
import datetime
import time


#Write to the marble log file


#Write it to the log file
#with open('app/logs/marbles.csv', 'a') as csvfile:
#	marblewriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
#	marblewriter.writerow([datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'),'App Started'])




app.run(host='0.0.0.0',debug=True)


