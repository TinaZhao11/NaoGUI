from naoqi import ALProxy
import math

IP = "192.168.1.100"
PORT = 9559


motion = ALProxy("ALMotion", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)

motion.rest()