#writes to a csv file

import csv
import datetime
import time



with open('logs/marbles.csv', 'a') as csvfile:
    marblewriter = csv.writer(csvfile, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    marblewriter.writerow([datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'),'Marble detected', 2452356])