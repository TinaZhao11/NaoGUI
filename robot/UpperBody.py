'''This file is created by Kecheng Guo and modified by Zeyu Zhao
This file contains all function module for recording process
'''

import time
from GUI import manageData as mD

from robot import ALMemoryKey, FilesRW as Frw, footstep as FS, Util as ul

# This function show the button mode recording
def record_animation_buttons(motion, memory,name):
    print "operate the robot..."
    animation_list = []
    finished = False
    while 1:
        if finished:
            break
        for joint in ALMemoryKey.UPPERBODY_TORQUE_KEY.keys():
            # check the torque and set relevant parts' stiffnesses to 0
            value = memory.getData(ALMemoryKey.UPPERBODY_TORQUE_KEY[joint])
            if value > ALMemoryKey.ALMEMORY_TORQUE_THRESHOLD[joint]:
                motion.setStiffnesses(joint, 0)
        flag = {}
        for key in ALMemoryKey.HEAD_TACTIL_TOUCHED.keys():
            value = memory.getData(ALMemoryKey.HEAD_TACTIL_TOUCHED[key])
            print key, value
            flag[key] = value
        if flag["RearTactil"] == 1.0:
            motion.setStiffnesses('Body', 1)
            finished = True
        elif flag["MiddleTactil"] == 1.0:
            save_data(memory, animation_list)
        elif flag["FrontTactil"] == 1.0:
            motion.setStiffnesses('Body', 1)
    print "Finish recording..."
    print "saving data..."
    result = str(animation_list)
    mD.save_record(name, result, len(animation_list))

# This function show the free mode recording
def record_animation1(motion, memory,name):
    print "operate the robot..."
    animation_list = []
    start = time.time()
    motion.setStiffnesses('Head', 0)
    motion.setStiffnesses('LArm', 0)
    motion.setStiffnesses('RArm', 0)
    while 1:
        value = memory.getData(ALMemoryKey.HEAD_TACTIL_TOUCHED['RearTactil'])
        if value == 1.0:
            break
        save_data(memory, animation_list)
        time.sleep(0.25)
    end = time.time()
    print "recording time: {} seconds.".format(end - start)
    result = str(animation_list)
    print(type(name))
    mD.save_record(name, result, len(animation_list))

# THis function show the torque mode recording
def record_animation(motion, memory, path, loop, filename):
    """
    Record the motions of upper body for LOOP times
    :param loop: Recording times 
    :param path: path of directory to create csv file
    :param motion: ALMotion instance
    :param memory: ALMemory instance
    :return: Path of csv file
    """
    print "operate the robot..."
    l = 0
    csv_path = Frw.create_csv(path, filename)
    animation_list = []
    start = time.time()
    while l < loop:
        l += 1
        print "loop:"
        print l
        record = 0
        for joint in ALMemoryKey.UPPERBODY_TORQUE_KEY.keys():
            value = memory.getData(ALMemoryKey.UPPERBODY_TORQUE_KEY[joint])
            if value <= ALMemoryKey.ALMEMORY_TORQUE_THRESHOLD[joint]:
                motion.setStiffnesses(joint, 1)
            else:
                motion.setStiffnesses(joint, 0)
                record = 1
        time.sleep(0.2)
        if record != 1:
            print "recording data..."
            save_data(memory, animation_list)
    end = time.time()
    print "recoding time: {} seconds.".format(end - start)
    Frw.save_result(animation_list, csv_path)
    return csv_path

# This function used to load the animation for the replaying process
def load_animation(motion, animationlist):
    """
    Load animation from csv file
    :param motion: motion ALProxy
    :param path: csv file path
    """
    print "Start loading animation recorded..."
    try:
        animation_lists, length = Frw.load_result(animationlist)
    except Exception:
        motion.rest()
        return False
    else:
        names = Frw.fieldnames
        angles = []
        times = []
        single_time = []
        duration = 0.0
        for i in range(1, length+1):
            t = round(0.5*i, 2)
            single_time.append(t)
        duration = single_time[-1]
        isAbsolute = True
        print("Duration")
        print(duration)
        for name in names:
            print(name)
            print(type(name))
            print(type(animation_lists))
            angles.append(animation_lists[name])
            times.append(single_time)
        motion.wbEnable(True)
        try:
            start = time.time()
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            print("is times")
            print(times)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception :
            print "Nothing recorded!"
        motion.waitUntilMoveIsFinished()
        motion.wbEnable(False)
        print "finished"
        return True


# THis function used to load animation with music beat for replaying process
def load_animation_with_beats(motion,animationList, musicList):

    print "Start loading animation records and music beats"
    timeline = musicList
    print("timeline")
    print(timeline)
    print("footstepLists")
    print(len(FS.footStepsLegList))
    try:
        animation_lists, length = Frw.load_result(animationList)
    except Exception:
        motion.rest()
        return False
    else:
        names = Frw.fieldnames
        angles = []
        times = []
        single_time = musicList
        single_time_len = len(single_time)
        isAbsolute = True
        for name in names:
            animation_lenth = len(animation_lists[name])
            if animation_lenth<single_time_len:
                r = single_time_len%animation_lenth
                n = single_time_len/animation_lenth
                animation_lists[name] = n*animation_lists[name] + animation_lists[name][0:r]
            angles.append(animation_lists[name])
            times.append(single_time)
        try:
            start = time.time()
            print len(angles)
            print len(times)
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception,errorMsg:
            print "Nothing recorded!"
            print str(errorMsg)
            print "This example is not allowed on this robot."
        motion.post.waitUntilMoveIsFinished()
        print "finished"
        return True

# This function load animation for demos
# The movement list and music list will get from the file from DemoFile
def load_animation_for_demo(motion, aup, beats, path, musicpath):
    print "Start loading animation records and music beats"
    timeline = beats
    print("timeline")
    print(timeline)
    print("footstepLists")
    print(len(FS.footStepsLegList))
    try:
        animation_lists, length = Frw.load_result_demo(path)
    except Exception:
        motion.rest()
        return False
    else:
        names = Frw.fieldnames
        angles = []
        times = []
        single_time = beats
        single_time_len = len(single_time)
        isAbsolute = True
        for name in names:
            animation_lenth = len(animation_lists[name])
            if animation_lenth<single_time_len:
                r = single_time_len%animation_lenth
                n = single_time_len/animation_lenth
                animation_lists[name] = n*animation_lists[name] + animation_lists[name][0:r]
            angles.append(animation_lists[name])
            times.append(single_time)
        try:
            start = time.time()
            print len(angles)
            print len(times)
            aup.post.playFile(musicpath)
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            time.sleep(18)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception,errorMsg:
            print "Nothing recorded!"
            print str(errorMsg)
            print "This example is not allowed on this robot."
        motion.waitUntilMoveIsFinished()
        aup.stopAll()
        print "finished"
        return True

# This function used to show the demo1
def demo1(motion, path, aup, musicpath, beats):
    timeline = beats
    timestep = []
    for l in range(4 * len(FS.footStepsLegList) + 1):
        if (4 * l <= len(timeline)):
            x = float(timeline[l * 4])
            timespot = round(x, 1)
            timestep.append(timespot)
    steptime = timestep[:len(FS.chaStepsLegList)]

    print "Start loading animation recorded..."
    try:
        animation_lists, length = Frw.load_result_demo(path)
    except Exception:
        motion.rest()
        return False
    else:
        names = Frw.fieldnames
        angles = []
        times = []
        single_time = []
        for i in range(1, length+1):
            t = round(0.5*i, 2)
            single_time.append(t)
        isAbsolute = True

        for name in names:
            angles.append(animation_lists[name])
            times.append(single_time)
        try:
            start = time.time()
            print(steptime)
            speedlist = [1, 1, 1,1, 1, 1, 1,1]
            motion.wbEnable(True)
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            motion.wbGoToBalance("LLeg", 5)
            motion.wbGoToBalance("LLeg", 6)
            motion.wbGoToBalance("RLeg", 6)
            motion.wbGoToBalance("Legs", 5)
            motion.wbGoToBalance("Legs", 11)
            ul.posture.goToPosture("StandInit", 0.5)
            print("is times")
            print(times)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception :
            print "Nothing recorded!"
        print "finished"
        motion.waitUntilMoveIsFinished()
        aup.stopAll()
        motion.rest()
        return True

# THis function show the step movement
def step(motion,leglist, steplist):
    speedlist = []
    for line in leglist:
        speedlist.append(1)
    print("Start leg motion")
    print(speedlist)
    print(leglist)
    print(type(leglist))
    print(steplist)
    print(type(steplist))
    motion.post.wbEnable(True)
    try:
        motion.post.setFootStepsWithSpeed(leglist, steplist, speedlist, False)
    except Exception, errorMsg:
        print str(errorMsg)
        print "This example is not allowed on this robot."
    print("Finish")

def save_data(memory, data_list):
    """
    Save data from ALMemory as a dictionary to list
    :param memory: ALMemory instance
    :param data_list: list of data dictionaries
    """
    results = {}
    for joint in ALMemoryKey.UPPERBODY_POSITION_KEY.keys():
        results[joint] = memory.getData(ALMemoryKey.UPPERBODY_POSITION_KEY[joint])
    data_list.append(results)