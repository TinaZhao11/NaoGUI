from naoqi import ALProxy
import math

IP = "127.0.0.1"
PORT = 56419


motion = ALProxy("ALMotion", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)

#posture.goToPosture("StandInit", 1.0)
text = "Hello"
tts.setVolume(0.5)
motion.rest()
aup.stopAll()