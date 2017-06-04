from robot import footstep as fs
import sqlite3

conn = sqlite3.connect('C:/Users/zeyu/Desktop/NaoGUI/Database/animation.db',timeout= 5)
c = conn.cursor()

c.execute("insert into steplist(name,leglist,steplist,length) values(?,?,?,?)", ("Box Step", str(fs.footStepsLegList),str(fs.footStepsMoveList), len(fs.footStepsLegList)))
conn.commit()
