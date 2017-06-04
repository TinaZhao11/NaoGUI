from naoqi import ALProxy
import sqlite3

conn = sqlite3.connect('C:/Users/zeyu/Desktop/NaoGUI/Database/animation.db')
c = conn.cursor()
c2 = conn.cursor()

for row in c.execute("select * from robotinfo where id = 1"):
    print row[0]
    ip = str(row[1])
    port = int(row[2])

RobotIP = ip
RobotPORT = port
    #str(c.execute("select port from robotinfo where id = 1"))


LOOP = 50
PI = 3.1415926
motion = ALProxy("ALMotion", RobotIP, RobotPORT)
motion1 = ALProxy("ALMotion", RobotIP, RobotPORT)
stopmotion = ALProxy("ALMotion", RobotIP, RobotPORT)
memory = ALProxy("ALMemory", RobotIP, RobotPORT)
posture = ALProxy("ALRobotPosture", RobotIP, RobotPORT)
aup = ALProxy("ALAudioPlayer", RobotIP, RobotPORT)
aup1 = ALProxy("ALAudioPlayer", RobotIP, RobotPORT)
tts = ALProxy("ALTextToSpeech", RobotIP, RobotPORT)

# From CSV file to list
def get_music(filepath):
    fo = open(filepath, "r")
    time = []
    for line in fo:
        time.append(float(line))
    return time

# File path of the beats
'''beats = {
    "sugar": get_music("out.csv"),
}
# File path of the music
music = {
    "sugar": "/home/nao/naoGUI/sugar.wav",
}'''''

# File path to store the motion records
PATH = "C:/Users/zeyu/Desktop/NaoGUI"