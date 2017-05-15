import FilesRW as Frw
import ALMemoryKey

IP = "192.168.1.101"
PORT = 9559
PATH = "C:/Users/zeyu/Desktop/Nao/result.csv"
LOOP = 100


def load_animation(motion, path):
    print "Start loading animation recorded..."
    animation_lists, length = Frw.load_result(path)
    names = Frw.fieldnames
    angles = []
    times = []
    single_time = []
    for i in range(1, length+1):
        single_time.append(i)
    isAbsolute = True
    for name in names:
        angles.append(animation_lists[name])
        times.append(single_time)
    print angles
    try:
        motion.angleInterpolation(names, angles, times, isAbsolute)
    except Exception:
        print "Nothing recorded!"
    print "finished"


def save_data(memory, data_list):
    results = {}
    for joint in ALMemoryKey.UPPERBODY_POSITION_KEY.keys():
        results[joint] = memory.getData(ALMemoryKey.UPPERBODY_POSITION_KEY[joint])
    for joint in ALMemoryKey.LEG_POSITION_KEY.keys():
        results[joint] = memory.getData(ALMemoryKey.LEG_POSITION_KEY[joint])
    print results
    data_list.append(results)
