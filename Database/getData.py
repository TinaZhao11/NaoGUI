import sqlite3
conn = sqlite3.connect('animation.db')

c = conn.cursor()

for row in c.execute("SELECT name FROM sqlite_master WHERE type='table'"):
        print row

for row in c.execute("SELECT * FROM musiclist "):
        print row

for row in c.execute("SELECT * FROM animation "):
        print row
for row in c.execute("SELECT * FROM steplist "):
        print row
