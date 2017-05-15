from naoqi import ALProxy
import math

IP = "192.168.1.101"
PORT = 9559


motion = ALProxy("ALMotion", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)

motion.setStiffnesses("Body", 1.0)
posture.goToPosture("StandInit", 1.0)

isEnabled = True
motion.wbEnable(isEnabled)

stateName = "Fixed"
supportLeg = "Legs"
motion.wbFootState(stateName, supportLeg)

isEnable = True
supportLeg = "Legs"
motion.wbEnableBalanceConstraint(isEnable, supportLeg)

# KneePitch angleInterpolation
# Without Whole Body balancer, foot will fall down
names = ["LKneePitch", "RKneePitch"]
angleLists = [[0.0, 40.0 * math.pi / 180.0], [0.0, 40.0 * math.pi / 180.0]]
timeLists = [[5.0, 10.0], [5.0, 10.0]]
isAbsolute = True
try:
    motion.angleInterpolation(names, angleLists, timeLists, isAbsolute)
except Exception, errorMsg:
    print str(errorMsg)
    print "This example is not allowed on this robot."
    exit()

isEnabled = False
motion.wbEnable(isEnabled)

motion.rest()