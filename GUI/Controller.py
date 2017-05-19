#This module contains the clicked button action to control action for robot
from robot import Util as ul
from robot import UpperBody as ub

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
    ub.record_animation1(ul.motion, ul.memory, "C:/Users/zeyu/Desktop/NaoGUI/", loop, "result.csv")
    ul.motion.rest()

def click_record():
    ul.posture.goToPosture("StandInit", 1.0)
    ul.motion.setStiffnesses("Body", 1)
    ub.record_animation_buttons(ul.motion, ul.memory, "C:/Users/zeyu/Desktop/NaoGUI/", "result.csv")
    ul.motion.rest()

def replay(music, step, volume):
    print("MUSIC")
    print(music)
    print(type(music))
    ul.motion.setStiffnesses("Body", 1)
    ul.posture.goToPosture("StandInit", 1.0)
    vol = round(volume/10, 2)
    ul.aup.setMasterVolume(vol)
    if music == 1:
        ub.load_animation(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/result.csv")
    if music == 2:
        beats_list = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/out.csv")
        musicpath = "/home/nao/naoGUI/sugar.wav"
        ub.load_animation_with_beats(ul.motion, ul.aup, beats_list, "C:/Users/zeyu/Desktop/NaoGUI/result.csv",musicpath)
    if music == 3:
        beats_list = ul.get_music("C:/Users/zeyu/Desktop/NaoGUI/out.csv")
        musicpath = "/home/nao/naoGUI/trouble.wav"
        ub.load_animation_with_leg(ul.motion, ul.aup, beats_list, "C:/Users/zeyu/Desktop/NaoGUI/result.csv", musicpath)

    ul.aup.stopAll()
    ul.posture.goToPosture("Crouch", 1.0)
    ul.motion.rest()
    ul.motion.setStiffnesses("Body", 0.0)



def stop_all():
    ul.motion1.stop()
    ul.aup1.stopAll()
    ul.motion1.rest()




