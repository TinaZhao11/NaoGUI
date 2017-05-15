from naoqi import ALProxy
import math

IP = "192.168.1.101"
PORT = 9559


motion = ALProxy("ALMotion", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)
motion.rest()
aup.stopAll()