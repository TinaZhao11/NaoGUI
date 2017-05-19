import argparse
import sys
import time

from naoqi import ALProxy

from robot import FilesRW as Frw

robotIP = "192.168.1.100"

footStepsList = []
footStepsLegList = []
footStepsMoveList = []
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("RLeg")
footStepsLegList.append("LLeg")
footStepsLegList.append("RLeg")


footStepsMoveList.append([0.03, 0.1, 0.0])
footStepsMoveList.append([0.00, 0.16, 0.0])
footStepsMoveList.append([0.00, -0.1, 0.0])
footStepsMoveList.append([0.00, 0.16, 0.0])
footStepsMoveList.append([-0.04, -0.1, 0.0])
footStepsMoveList.append([0.00, -0.16, 0.0])
footStepsMoveList.append([0.00, 0.1, 0.0])
footStepsMoveList.append([0.00, -0.16, 0.0])
footStepsMoveList.append([0.03, 0.1, 0.0])
footStepsMoveList.append([0.00, 0.16, 0.0])
footStepsMoveList.append([0.00, -0.1, 0.0])
footStepsMoveList.append([0.00, 0.16, 0.0])
footStepsMoveList.append([-0.04, -0.1, 0.0])
footStepsMoveList.append([0.00, -0.16, 0.0])
footStepsMoveList.append([0.00, 0.1, 0.0])
footStepsMoveList.append([0.00, -0.16, 0.0])

def chachastep_main(robotIP, PORT=9559):
    print(footStepsLegList)
    print(footStepsMoveList)
    motion  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    aup = ALProxy("ALAudioPlayer", "192.168.1.100", 9559)
    tts = ALProxy("ALTextToSpeech", "192.168.1.100", 9559)

    # Wake up robot
    motion.moveInit()
    #aup.playFile("/home/nao/naoGUI/moonlight.wav", 0.9, -1.0)
    motion.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.8)

    timeline = get_music("C:/Users/zeyu/Desktop/NaoGUI/out.csv")
    time = []
    print("timeline")
    print(timeline)
    print("footstepLists")
    print(len(footStepsList))
    for l in range( 4*len(footStepsLegList) +1):
        #print(l)
        if(4*l <= len(timeline)):
            x = float(timeline[l*4])
            timespot = round(x, 1)
            time.append(timespot)
    steptime = time[:len(footStepsLegList)]

    print("steptime")
    print(steptime)
    try:
        animation_lists, length = Frw.load_result("C:/Users/zeyu/Desktop/NaoGUI/result.csv")
    except Exception:
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

        try:
            print("footStepsList")
            print(footStepsLegList)
            print(footStepsMoveList)
            aup.post.playFile("/home/nao/naoGUI/sugar.wav")
            motion.post.setFootSteps(footStepsLegList,footStepsMoveList,steptime, True)
            motion.angleInterpolation(names, angles, times, isAbsolute)
        except Exception, errorMsg:
            print str(errorMsg)
            print "This example is not allowed on this robot."
            motion.rest()
            exit()


        motion.waitUntilMoveIsFinished()

        # Go to rest position
        aup.stopAll()
        motion.rest()
        sys.exit(1)

def get_music(filepath):
    fo = open(filepath, "r")
    time = []
    for line in fo:
        time.append(float(line))
    return time

# File path of the beats
beats = {
    "sugar": get_music("C:/Users/zeyu/Desktop/NaoGUI/out.csv"),
}
# File path of the music
music = {
    "sugar": "/home/nao/naoGUI/sugar.wav",
}

# File path to store the motion records
#PATH = "C:/Users/gkcsj/Desktop"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.100",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    args = parser.parse_args()
    chachastep_main(args.ip, args.port)