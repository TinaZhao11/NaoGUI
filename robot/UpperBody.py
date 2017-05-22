import time

from robot import ALMemoryKey, FilesRW as Frw, footstep as FS, Util as ul


def record_animation_buttons(motion, memory, path, filename):
    print "operate the robot..."
    csv_path = Frw.create_csv(path, filename)
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
    Frw.save_result(animation_list, csv_path)
    return csv_path


def record_animation1(motion, memory, path, filename):
    print "operate the robot..."
    csv_path = Frw.create_csv(path, filename)
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
    Frw.save_result(animation_list, csv_path)
    return csv_path


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

def load_animation(motion, path):
    """
    Load animation from csv file
    :param motion: motion ALProxy
    :param path: csv file path
    """
    print "Start loading animation recorded..."
    try:
        animation_lists, length = Frw.load_result(path)
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
            angles.append(animation_lists[name])
            times.append(single_time)
        try:
            start = time.time()
           # motion.wbEnable(True)
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            #motion.wbGoToBalance("LLeg", 3)
           # motion.wbGoToBalance("Legs", 3)
           # motion.wbGoToBalance("RLeg", 3)
           # motion.wbGoToBalance("Legs", 3)
            print("is times")
            print(times)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception :
            print "Nothing recorded!"
        motion.waitUntilMoveIsFinished()
        print "finished"
        return True


def load_animation_with_beats(motion, aup, beats, path, musicpath):

    print "Start loading animation records and music beats"
    timeline = beats
    timestep = []
    print("timeline")
    print(timeline)
    print("footstepLists")
    print(len(FS.footStepsLegList))
    for l in range(4 * len(FS.footStepsLegList) + 1):
        # print(l)
        if (4 * l <= len(timeline)):
            x = float(timeline[l * 4])
            timespot = round(x, 1)
            timestep.append(timespot)
    steptime = timestep[:len(FS.footStepsLegList)]
    print("steptime")
    print(steptime)
    try:
        animation_lists, length = Frw.load_result(path)
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

        for l in range(4 * len(FS.footStepsLegList) + 1):
            # print(l)
            if (4 * l <= len(timeline)):
                x = float(timeline[l * 4])
                timespot = round(x, 1)
                timestep.append(timespot)
        steptime = timestep[:len(FS.footStepsLegList)]

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
            print angles
            print times
            print(FS.footStepsLegList)
            print(FS.footStepsMoveList)
            print(times[:len(FS.chaStepsLegList)])
            aup.post.playFile(musicpath)
            #motion.post.setFootSteps(FS.footStepsLegList, FS.footStepsMoveList, steptime, False)
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            #motion.setFootSteps(FS.footStepsLegList, FS.footStepsMoveList, steptime, False)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception,errorMsg:
           # print "Nothing recorded!"
            print str(errorMsg)
            print "This example is not allowed on this robot."
        motion.post.waitUntilMoveIsFinished()
        #aup.stopAll()
       # motion.rest()
        print "finished"
        return True

def demo1(motion, path, aup, musicpath, beats):
    timeline = beats
    timestep = []
    for l in range(4 * len(FS.footStepsLegList) + 1):
        # print(l)
        if (4 * l <= len(timeline)):
            x = float(timeline[l * 4])
            timespot = round(x, 1)
            timestep.append(timespot)
    steptime = timestep[:len(FS.chaStepsLegList)]

    print "Start loading animation recorded..."
    try:
        animation_lists, length = Frw.load_result(path)
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
            #aup.post.playFile(musicpath)
            print(steptime)
            speedlist = [1, 1, 1,1, 1, 1, 1,1]
            motion.wbEnable(True)
            motion.post.angleInterpolation(names, angles, times, isAbsolute)
            motion.wbGoToBalance("LLeg", 5)
            #motion.wbGoToBalance("Legs", 5)
            motion.wbGoToBalance("LLeg", 6)
            motion.wbGoToBalance("RLeg", 6)
            motion.wbGoToBalance("Legs", 5)
            motion.wbGoToBalance("Legs", 11)
            ul.posture.goToPosture("StandInit", 0.5)
           # motion.setStiffnesses("Body", 1)
           # motion.setFootStepsWithSpeed(FS.footStepsLegList, FS.footStepsMoveList, speedlist, False)
            #time.sleep(2)
            #motion.setFootStepsWithSpeed(FS.footStepsLegList, FS.footStepsMoveList, speedlist, False)
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

def demo2(motion, path, aup, musicpath, beats):
    timeline = beats
    timestep = []
    motion.wbEnable(True)
    for l in range(4 * len(FS.chaStepsLegList) + 1):
        # print(l)
        if (4 * l <= len(timeline)):
            x = float(timeline[l * 4])
            timespot = round(x, 1)
            timestep.append(timespot)
    steptime = timestep[:len(FS.chaStepsLegList)]

    print "Start loading animation recorded..."
    try:
        animation_lists, length = Frw.load_result(path)
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
            aup.post.playFile(musicpath)
            print(steptime)
            speedlist = [1, 1, 1,1, 1, 1, 1,1]
            '''supportLeg = "LLeg"
            duration = 3.0
            motion.post.wbGoToBalance(supportLeg, duration)
            supportLeg = "RLeg"
            duration = 3.0
            motion.wbGoToBalance(supportLeg, duration)'''
            motion.angleInterpolation(names, angles, times, isAbsolute)
            time.sleep(20)
            #motion.wbEnable(False)
            supportLeg = "LLeg"
            duration = 3.0
            motion.post.wbGoToBalance(supportLeg, duration)
            motion.wbEnable(False)
            motion.wbEnable(True)
            supportLeg = "RLeg"
            duration = 3.0
            motion.wbGoToBalance(supportLeg, duration)
            motion.wbEnable(False)
            motion.setFootStepsWithSpeed(FS.chaStepsLegList, FS.chaStepsMoveList, speedlist, False)
            time.sleep(2)
            motion.setFootStepsWithSpeed(FS.chaStepsLegList, FS.chaStepsMoveList, speedlist, False)
            print("is times")
            print(times)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception :
            print "Nothing recorded!"
        print "finished"
       # motion.waitUntilMoveIsFinished()
        aup.stopAll()
        motion.rest()
        return True


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