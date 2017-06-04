import sqlite3

conn = sqlite3.connect('C:/Users/zeyu/Desktop/NaoGUI/Database/animation.db',timeout= 5)
c = conn.cursor()

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


def save_record(RecordName, AnimationResult,Length):
    name = str(RecordName)
    print(name)
    c.execute("insert into animation(name,list,listline) values(?,?,?)", (str(name), AnimationResult,Length))
    conn.commit()

def sendNameList():
    nameList = []
    for line in c.execute("select * from animation"):
        nameList.append(line[0])
    print(nameList)
    return nameList

def sendRecordLengthList():
    lengthlist = []
    for line in c.execute("select * from animation"):
        lengthlist.append(line[2])
    return lengthlist

def sendMusicList():
    musiclist = []
    for line in c.execute("select * from musiclist"):
        musiclist.append(line[0])
    return musiclist
def sendMusicLengthList():
    lengthlist = []
    for line in c.execute("select * from musiclist"):
        lengthlist.append(line[2])
    return lengthlist

def sendStepList():
    steplist = []
    for line in c.execute("select * from steplist"):
        steplist.append(line[0])
    return steplist
def sendStepLengthList():
    lengthlist = []
    for line in c.execute("select * from steplist"):
        lengthlist.append(line[3])
    return lengthlist

def getMusicList(name):
    for row in c.execute("select * from musiclist where name = '%s'" % (name)):
        musiclist = str(row[1])
        return musiclist

def getAnimationList(name):
    for row in c.execute("select * from animation where name = '%s'"%(name)):
        animationlist = str(row[1])
        return animationlist

def getLegList(name):
    for line in c.execute("select * from steplist where name = '%s'"%(name)):
        leglist = str(line[1])
        return leglist

def getStepList(name):
    for line in c.execute("select * from steplist where name = '%s'"%(name)):
        steplist = str(line[2])
        return steplist

def getMusicName(name):
    return name

def insertMusic(name,beatlist,length):
    c.execute("insert into musiclist(name,beatlist,length) values(?,?,?)", (str(name), beatlist, length))
    conn.commit()

def delete_record(RecordName):
    print("RecordName")
    print(RecordName)
    c.execute("delete from animation where name ='%s'"%(RecordName))
    conn.commit()
    print("delete")