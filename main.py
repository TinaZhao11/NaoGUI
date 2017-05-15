from naoqi import ALProxy
import time
import Util
import UpperBody as ub

IP = Util.IP
PORT = Util.PORT


def main():
    motion = ALProxy("ALMotion", IP, PORT)
    memory = ALProxy("ALMemory", IP, PORT)
    posture = ALProxy("ALRobotPosture", IP, PORT)
    aup = ALProxy("ALAudioPlayer", IP, PORT)
    print posture.getPostureList()

    posture.goToPosture("StandInit", 1.0)
    # posture.goToPosture("SitRelax", 1.0)
    # posture.goToPosture("StandZero", 1.0)
    # posture.goToPosture("LyingBelly", 1.0)
    # posture.goToPosture("LyingBack", 1.0)
    # posture.goToPosture("Stand", 1.0)
    # posture.goToPosture("Left", 3.0)
    #posture.goToPosture("Crouch", 1.0)
    # posture.goToPosture("Sit", 1.0)

    motion.setStiffnesses("Body", 1)

    # record data

    path = ub.record_animation1(motion, memory, "C:/Users/zeyu/Desktop/Nao/", 50, "result.csv")
    motion.rest()
    time.sleep(2.0)
    motion.setStiffnesses("Body", 1)

    # Read data
    posture.goToPosture("Crouch", 1.0)
    aup.post.playFile("/home/nao/naoGUI/sugar.wav")
    Util.load_animation(motion, path)
    aup.stopAll()

    posture.goToPosture("Crouch", 1.0)
    motion.rest()
    motion.setStiffnesses("Body", 0.0)


if __name__ == "__main__":
    main()
