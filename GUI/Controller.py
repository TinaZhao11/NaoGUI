#This module contains the clicked button action to control action for robot
from robot import Util as ul
from robot import UpperBody as ub
from robot import footstep as FS
import manageData as mD


from naoqi import ALProxy
IP = ul.RobotIP
PORT = ul.RobotPORT
motion = ALProxy("ALMotion", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)

import time

x = 0.0
y = 0.0
r = 0.0

def stand_motion():
    ul.posture.goToPosture("StandInit", 1.0)

def sit_motion():
    ul.posture.post.goToPosture("Sit", 1.0)

def crouch_motion():
    ul.posture.post.goToPosture("Crouch", 1.0)

def lyback_motion():
    ul.posture.post.goToPosture("LyingBack", 1.0)

def lybelly_motion():
    ul.posture.post.goToPosture("LyingBelly", 1.0)

def rest_motion():
    ul.aup.stopAll()
    ul.motion.rest()

def walk_motion(x, y, r):
    ul.posture.goToPosture("StandInit", 1.0)
    ul.motion.post.moveTo(x/10, y/10, r/10)

def talk_motion(text, volume):
    ul.tts.setVolume(volume/100)
    ul.tts.say(text)

def con_record(name):
    ul.posture.goToPosture("StandInit", 1.0)
    ul.motion.setStiffnesses("Body", 1)
    ub.record_animation1(ul.motion, ul.memory, "C:/Users/zeyu/Desktop/NaoGUI/",  "result.csv",name)
    ul.motion.rest()

def click_record(name):
    ul.posture.goToPosture("StandInit", 1.0)
    ul.motion.setStiffnesses("Body", 1)
    ub.record_animation_buttons(ul.motion, ul.memory, "C:/Users/zeyu/Desktop/NaoGUI/",  "result.csv",name)
    ul.motion.rest()

def s1():
    ul.motion.setStiffnesses("Body", 1)

def s0():
    ul.motion.setStiffnesses("Body", 0)


def demo1():
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 0.5)
    #ul.tts.say("Hello, my name is joko, ready to see my dance?Come some music!")
    beats_list = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/out.csv")
    speedlist = [1, 1, 1, 1, 1, 1, 1, 1]
    leglist = eval(mD.getLegList("Box Step"))
    leg = leglist[0:8]
    steplist = eval(mD.getStepList("Box Step"))
    step = steplist[0:8]
    ul.aup.post.playFile("/home/nao/naoGUI/trouble.wav")
    ul.motion.wbEnable(True)
    print leg
    print step
    ul.motion.post.setFootStepsWithSpeed(leg, step, speedlist, False)
    ub.demo1(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/demo1.csv", ul.aup,"/home/nao/naoGUI/trouble.wav",beats_list)
    ul.motion.rest()

def demo2():
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 0.5)
    beats_list1 = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/music_track/moon.csv")
    musicpath1 = "/home/nao/naoGUI/moon.wav"
    ub.load_animation_for_demo(ul.motion, ul.aup, beats_list1, "C:/Users/zeyu/Desktop/NaoGUI/result1.csv",  musicpath1)

    beats_list2 = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/music_track/sky.csv")
    musicpath2 = "/home/nao/naoGUI/sky.wav"
    ub.load_animation_for_demo(ul.motion, ul.aup, beats_list2, "C:/Users/zeyu/Desktop/NaoGUI/result2.csv",
                                 musicpath2)


def replay(music, step, animataion,volume):
    print("MUSIC")
    print(music)
    print(type(music))
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 0.5)

    if mD.getAnimationList(animataion) != None:
        animationList = eval(mD.getAnimationList(animataion))
    if mD.getMusicList(music) != None:
        musicList = eval(mD.getMusicList(music))
    if mD.getLegList(step) != None:
        stepleglist = eval(mD.getLegList(step))
    if mD.getStepList(step) != None:
        steplist = eval(mD.getStepList(step))
        vol = round(volume/100, 2)
    if music == "None":
        if step == "None" and animataion != "None":
            ub.load_animation(ul.motion, animationList)
        if step == "None" and animataion == "None":
            ul.motion.rest()
        if step != "None" and animataion == "None":
            ub.step(ul.motion, stepleglist, steplist)
        if step != "None" and animataion != "None":
            ub.load_animation(ul.motion, animationList)
            ub.step(ul.motion, stepleglist, steplist)
    if step == "None":
        if music == "None" and animataion != "None":
            ub.load_animation(ul.motion, animationList)
        if music == "None" and animataion == "None":
            ul.motion.rest()
        if music != "None" and animataion == "None":
            if music == "Sky":
                ul.aup.post.playFile('/home/nao/naoGUI/sky.wav')
            if music == "Moonlight Sonata":
                ul.aup.post.playFile('/home/nao/naoGUI/Moonlight Sonata.wav')
        if music != "None" and animataion != "None":
            if music == "Sky":
                ul.aup.post.playFile('/home/nao/naoGUI/sky.wav')
                ub.load_animation_with_beats(ul.motion,animationList, musicList)
            if music == "Moonlight Sonata":
                ul.aup.post.playFile('/home/nao/naoGUI/Moonlight Sonata.wav')
                ub.load_animation_with_beats(ul.motion,animationList, musicList)

    if animataion == "None":
        if music == "None" and step != "None":
            ub.step(ul.motion, stepleglist, steplist)
        if music == "None" and step == "None":
            ul.motion.rest()
        if music != "None" and step == "None":
            if music == "Sky":
                ul.aup.post.playFile('/home/nao/naoGUI/sky.wav')
            if music == "Moonlight Sonata":
                ul.aup.post.playFile('/home/nao/naoGUI/Moonlight Sonata.wav')
        if music != "None" and step != "None":
            if music == "Sky":
                ul.aup.post.playFile('/home/nao/naoGUI/sky.wav')
                ub.step(ul.motion, stepleglist, steplist)
            if music == "Moonlight Sonata":
                ul.aup.post.playFile('/home/nao/naoGUI/Moonlight Sonata.wav')
                ub.step(ul.motion, stepleglist, steplist)
    if animataion != "None" and music != "None" and step != "None":
            if music == "Sky":
                ul.aup.post.playFile('/home/nao/naoGUI/sky.wav')
                ub.load_animation_with_beats(ul.motion, animationList, musicList)
                ub.step(ul.motion, stepleglist, steplist)
            if music == "Moonlight Sonata":
                ul.aup.post.playFile('/home/nao/naoGUI/Moonlight Sonata.wav')
                ub.load_animation_with_beats(ul.motion, animationList, musicList)
                ub.step(ul.motion, stepleglist, steplist)


def stop_all():
    ul.aup.stopAll()
    ul.stopmotion.rest()




