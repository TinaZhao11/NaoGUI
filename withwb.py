'''''This part use to play two process of animation
the first come with arm1.csv
the second come woth arm2.csv'''

ub.load_animation(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/arm1.csv", "RLeg")
ul.motion.stop
ub.load_animation(ul.motion, "C:/Users/zeyu/Desktop/NaoGUI/arm2.csv", "LLeg")
ul.motion.wbEnable(True)
ul.motion.post.wbGoToBalance("Legs", 2)





def load_animation(motion, path,leg):
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
            motion.wbEnable(True)
            motion.post.wbGoToBalance(leg, duration - 1)
            motion.angleInterpolation(names, angles, times, isAbsolute)
            print("is times")
            print(times)
            end = time.time()
            print "playing time: {} seconds.".format(end - start)
        except Exception :
            print "Nothing recorded!"
        motion.waitUntilMoveIsFinished()
        print "finished"
        return True