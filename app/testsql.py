# Writing to the marbles database

import sqlite3 as lite
import sys


con = lite.connect('marbles.db')

with con:
    
    cur = con.cursor()    

    #cur.execute("CREATE TABLE Launches(Id INT, LauchDate DATE, Type TEXT, Grouping TEXT, Sequence INT, Total INT)")
    marble_id = 23
    marble_launch_time = '2015-01-04 21:55:58.066121'
    event_type = 'Launched Marble'
    grp = 'Single'
    seq = 1
    tot = 1

    #print "INSERT INTO Launches VALUES (",marble_id, ",'", marble_launch_time, "','", event_type, "','", grp, "'," , seq, ",", tot, ")"

    cur.execute("INSERT INTO Launches VALUES(?,?,?,?,?,?);",(marble_id, marble_launch_time, event_type, grp, seq, tot))


 