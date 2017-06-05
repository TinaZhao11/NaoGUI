'''This file contain the step design and evaluation
In this file, the footstep will synchronized with music beat, meanwhile adding the upperbody motion
This function is not applied to GUI because the balance issue need to be improved'''
import argparse
import sys
import sqlite3

conn = sqlite3.connect('animation.db')
c = conn.cursor()

from naoqi import ALProxy
from robot import FilesRW as Frw

# Pre-setting two footstep, the footsteplist is box step
# THe chasteplist is the cha cha step
footStepsList = []
footStepsLegList = []
footStepsMoveList = []
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")

footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])
footStepsMoveList.append([0.06, 0.0, 0.0])
footStepsMoveList.append([0.0, 0.0, 0.0])


chaStepsLegList = []
chaStepsMoveList = []
chaStepsLegList.append("LLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("RLeg")
chaStepsLegList.append("LLeg")
chaStepsLegList.append("RLeg")

chaStepsMoveList.append([0.16, 0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([0.00, -0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([-0.04, -0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])
chaStepsMoveList.append([0.00, 0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])
chaStepsMoveList.append([0.16, 0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([0.00, -0.1, 0.0])
chaStepsMoveList.append([0.00, 0.16, 0.0])
chaStepsMoveList.append([-0.04, -0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])
chaStepsMoveList.append([0.00, 0.1, 0.0])
chaStepsMoveList.append([0.00, -0.16, 0.0])





def chachastep_main(robotIP, PORT=9559):
    motion  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    aup = ALProxy("ALAudioPlayer", robotIP, PORT)

    leg = chaStepsLegList
    step =  chaStepsMoveList
    # Wake up robot
    motion.moveInit()
    motion.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.8)

    timeline = get_music("C:/Users/zeyu/Desktop/NaoGUI/DemoFile/trouble.csv")
    time = []
    print("timeline")
    print(timeline)
    print("footstepLists")
    print(len(footStepsList))

    # This part generate the timeline according to the steplist
    # The timeline should has same length of steplist
    for l in range( 4*len(footStepsLegList) +1):
        if(4*l <= len(timeline)):
            x = float(timeline[l*4])
            timespot = round(x, 1)
            time.append(timespot)
    steptime = time[:len(footStepsLegList)]

    # This part load the animation for upperbody
    try:
        animation_lists, length = Frw.load_result_demo("C:/Users/zeyu/Desktop/NaoGUI/DemoFile/result1.csv")
    except Exception,errorMsg:
        print errorMsg
        motion.rest()
        return False
    else:
        names = Frw.fieldnames
        angles = []
        times = []
        single_time = []
        for i in range(1, length + 1):
            t = round(0.5 * i, 2)
            single_time.append(t)
        isAbsolute = True
        for name in names:
            angles.append(animation_lists[name])
            times.append(single_time)
        # THis part play the music and show step and animation
        try:
            aup.post.playFile("/home/nao/naoGUI/trouble.wav")
            motion.post.setFootSteps(footStepsLegList,footStepsMoveList,steptime, True)
            motion.angleInterpolation(names, angles, times, isAbsolute)
        except Exception, errorMsg:
            print str(errorMsg)
            print "This example is not allowed on this robot."
            motion.rest()
            exit()

        motion.waitUntilMoveIsFinished()
        aup.stopAll()
        motion.rest()

def get_music(filepath):
    fo = open(filepath, "r")
    time = []
    for line in fo:
        time.append(float(line))
    return time

# File path of the beats
beats = {
    "sugar": get_music("C:/Users/zeyu/Desktop/NaoGUI/DemoFile/trouble.csv"),
}
# File path of the music
music = {
    "sugar": "/home/nao/naoGUI/trouble.wav",
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.102",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    args = parser.parse_args()
    chachastep_main(args.ip, args.port)