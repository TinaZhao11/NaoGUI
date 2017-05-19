from naoqi import ALProxy
IP = "192.168.1.100"
PORT = 9559
LOOP = 50
PI = 3.1415926

motion = ALProxy("ALMotion", IP, PORT)
motion1 = ALProxy("ALMotion", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)
aup1 = ALProxy("ALAudioPlayer", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)
print posture.getPostureList()

# From CSV file to list
def get_music(filepath):
    fo = open(filepath, "r")
    time = []
    for line in fo:
        time.append(float(line))
    return time

# File path of the beats
beats = {
    "sugar": get_music("out.csv"),
}
# File path of the music
music = {
    "sugar": "/home/nao/naoGUI/sugar.wav",
}

# File path to store the motion records
PATH = "C:/Users/zeyu/Desktop/NaoGUI"