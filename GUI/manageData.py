'''This project is created by Zeyu Zhao
This package contains all GUI design used for user interface

This manageData is the data manager for the desktop application
This module contains data management like update, insert or select for system module'''

import sqlite3
conn = sqlite3.connect('C:/Users/zeyu/Desktop/NaoGUI/Database/animation.db',timeout= 5)
c = conn.cursor()

# This function used to check record name from animatoin table
# If name exist, return False, else return True
def check_record_name(RecordName):
    flag = 1
    for line in c.execute("select * from animation"):
        print(line[0])
        if line[0] == RecordName:
            flag = 0
            print("False")
            break
        else:
            flag = 1
            print("TRUE")
    if flag == 0:
        return False
    else:
        return True

# This function used to save record result to animation table
# The data include name, record list, and list length
def save_record(RecordName, AnimationResult,Length):
    name = str(RecordName)
    print(name)
    c.execute("insert into animation(name,list,listline) values(?,?,?)", (str(name), AnimationResult,Length))
    conn.commit()

# This function used to send name of recordlist for views
def sendNameList():
    nameList = []
    for line in c.execute("select * from animation"):
        nameList.append(line[0])
    print(nameList)
    return nameList

# This function used to send length of recordlist for views
def sendRecordLengthList():
    lengthlist = []
    for line in c.execute("select * from animation"):
        lengthlist.append(line[2])
    return lengthlist

# This function used to send name of musiclist for views
def sendMusicList():
    musiclist = []
    for line in c.execute("select * from musiclist"):
        musiclist.append(line[0])
    return musiclist

# This function used to send length of musiclist for views
def sendMusicLengthList():
    lengthlist = []
    for line in c.execute("select * from musiclist"):
        lengthlist.append(line[2])
    return lengthlist

# This function used to send name of steplist for views
def sendStepList():
    steplist = []
    for line in c.execute("select * from steplist"):
        steplist.append(line[0])
    return steplist

# This function used to send length of steplist for views
def sendStepLengthList():
    lengthlist = []
    for line in c.execute("select * from steplist"):
        lengthlist.append(line[3])
    return lengthlist

# This function used to get beatlist of music
def getMusicList(name):
    for row in c.execute("select * from musiclist where name = '%s'" % (name)):
        musiclist = str(row[1])
        return musiclist

# This function used to get movement list of animation
def getAnimationList(name):
    for row in c.execute("select * from animation where name = '%s'"%(name)):
        animationlist = str(row[1])
        return animationlist

# This function used to get leg list of step movement
def getLegList(name):
    for line in c.execute("select * from steplist where name = '%s'"%(name)):
        leglist = str(line[1])
        return leglist

# This function used to get step list of step movement
def getStepList(name):
    for line in c.execute("select * from steplist where name = '%s'"%(name)):
        steplist = str(line[2])
        return steplist

# THis function used to get music name
def getMusicName(name):
    return name

# This function used to insert music list to database
def insertMusic(name,beatlist,length):
    c.execute("insert into musiclist(name,beatlist,length) values(?,?,?)", (str(name), beatlist, length))
    conn.commit()

# THis function used to delete recordlist from animation table
def delete_record(RecordName):
    print("RecordName")
    print(RecordName)
    c.execute("delete from animation where name ='%s'"%(RecordName))
    conn.commit()
    print("delete")