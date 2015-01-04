# Writing to the marbles database

import sqlite3 as lite
import sys

     

def write_marble( marble_launch_time, event_type, grp,seq, tot):


    con = lite.connect('marbles.db')

    with con:
        
        cur = con.cursor()    

        cur.execute("CREATE TABLE IF NOT EXISTS Launches( LaunchDate DATE, Type TEXT, Grouping TEXT, Sequence INT, Total INT)")
        print "INSERT INTO Launches VALUES ('", marble_launch_time, "','", event_type, "','", grp, "'," , seq, ",", tot, ")"

        cur.execute("INSERT INTO Launches VALUES(?,?,?,?,?);",(marble_launch_time, event_type, grp, seq, tot))


     