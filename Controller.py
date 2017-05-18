#This module contains the clicked button action to control action for robot
import Util as ul

x = 0.0
y = 0.0
r = 0.0

def stand_motion():
    ul.posture.goToPosture("StandInit", 1.0)

def sit_motion():
    ul.posture.goToPosture("Sit", 1.0)

def crouch_motion():
    ul.posture.goToPosture("Crouch", 1.0)

def lyback_motion():
    ul.posture.goToPosture("LyingBack", 1.0)

def lybelly_motion():
    ul.posture.goToPosture("LyingBelly", 1.0)

def rest_motion():
    ul.motion.rest()

def walk_motion():
    ul.motion.moveTo(x/10, y/10, r/10)




