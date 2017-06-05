'''This project is created by Zeyu Zhao
This package contains the Database and some Initial Operation for Databse
This getData file used to visulize the Database result in the output'''

#!/usr/bin/python
import sqlite3

# Connect to database and create a cursor for operation
conn = sqlite3.connect('animation.db')
c = conn.cursor()

tablelist = []
for row in c.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        tablelist.append(row)
        print("All table in database:")
        print row


for table in tablelist:
        print("The line in table")
        print(table)
        for row in c.execute("SELECT * FROM '%s'"%(table)):
                print row
