#This module contains the clicked button action to control action for robot
from robot import Util as ul
from robot import UpperBody as ub
from robot import footstep as FS
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

def con_record(loop):
    ul.posture.goToPosture("StandInit", 1.0)
    ul.motion.setStiffnesses("Body", 1)
    ub.record_animation1(ul.motion, ul.memory, "C:/Users/zeyu/Desktop/NaoGUI/",  "result.csv")
    ul.motion.rest()

def click_record():
    ul.posture.goToPosture("StandInit", 1.0)
    ul.motion.setStiffnesses("Body", 1)
    ub.record_animation_buttons(ul.motion, ul.memory, "C:/Users/zeyu/Desktop/NaoGUI/", "result.csv")
    ul.motion.rest()

def s1():
    ul.motion.setStiffnesses("Body", 1)

def s0():
    ul.motion.setStiffnesses("Body", 0)


def demo1():
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 0.5)
    ul.tts.say("Hello, my name is joko, ready to see my dance?Come some music!")
    beats_list = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/out.csv")
    speedlist = [1, 1, 1, 1, 1, 1, 1, 1]
    ul.aup.post.playFile("/home/nao/naoGUI/trouble.wav")
    ul.motion.wbEnable(True)
    ul.motion.post.setFootStepsWithSpeed(FS.footStepsLegList, FS.footStepsMoveList, speedlist, False)
    ub.demo1(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/demo1.csv", ul.aup,"/home/nao/naoGUI/trouble.wav",beats_list)
    ul.motion.rest()

def demo2():
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 0.5)
    beats_list1 = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/music_track/moon.csv")
    musicpath1 = "/home/nao/naoGUI/moon.wav"
    ub.load_animation_with_beats(ul.motion, ul.aup, beats_list1, "C:/Users/zeyu/Desktop/NaoGUI/result1.csv",  musicpath1)

    beats_list2 = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/music_track/sky.csv")
    musicpath2 = "/home/nao/naoGUI/sky.wav"
    ub.load_animation_with_beats(ul.motion, ul.aup, beats_list2, "C:/Users/zeyu/Desktop/NaoGUI/result2.csv",
                                 musicpath2)
    ul.aup.stopAll()
    ul.motion.rest()

def replay(music, step, volume):
    print("MUSIC")
    print(music)
    print(type(music))
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 0.5)
    vol = round(volume/100, 2)
    #ul.aup.setMasterVolume(vol)
    if music == 1:
        if step == 2:
            ub.step2(ul.motion)
            ub.load_animation(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/result.csv")
        if step == 3:
            ub.load_animation(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/result.csv")
    if music == 2:
        beats_list1 = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/music_track/moonlight.csv")
        musicpath1 = "/home/nao/naoGUI/moonlight.wav"
        ub.load_animation_with_beats(ul.motion, ul.aup, beats_list1, "C:/Users/zeyu/Desktop/NaoGUI/result.csv", musicpath1)
        #ul.aup.stopAll()
    if music == 3:
        beats_list2 = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/music_track/fullsky.csv")
        musicpath2 = "/home/nao/naoGUI/sky.wav"
        ub.load_animation_with_beats(ul.motion, ul.aup, beats_list2, "C:/Users/zeyu/Desktop/NaoGUI/result.csv",
                                     musicpath2)
        #ul.aup.stopAll()
    #ul.motion.rest()
    #ul.aup.stopAll()
    #ul.posture.goToPosture("Crouch", 1.0)
    #ul.motion.rest()
    #ul.motion.setStiffnesses("Body", 0.0)



def stop_all():
    ul.aup.stopAll()
    ul.motion.rest()




