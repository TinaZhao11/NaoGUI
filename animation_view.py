from PyQt4 import QtGui, QtCore

from naoqi import ALProxy
import time
import Util
import UpperBody as ub

IP = Util.IP
PORT = Util.PORT
from mainMenu import MainMenu

motion = ALProxy("ALMotion", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)

class Animation_View(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Animation_View, self).__init__(parent)
        self.initUI()
        self.tabWidget = QtGui.QTabWidget()
        self.tabWidget2 = QtGui.QTabWidget()

    def initUI(self):
        self.resize(1000, 600)
        self.setCenter()
        self.setWindowTitle('Animation')
        self.setWindowIcon(QtGui.QIcon('image/Icon.png'))

        SM_button = QtGui.QPushButton("Standard Motion", self)
        SM_button.move(200, 200)

        RM_button = QtGui.QPushButton("Record Motion", self)
        RM_button.move(200, 350)

        BM_button = QtGui.QPushButton("Back to Main", self)
        BM_button.move(200, 500)


        self.connect(SM_button, QtCore.SIGNAL('clicked()'),
                     self.SM_ButtonClicked)

        self.connect(RM_button, QtCore.SIGNAL('clicked()'),
            self.RM_ButtonClicked)

        self.connect(BM_button, QtCore.SIGNAL('clicked()'),
                     self.BM_ButtonClicked)



    def setCenter(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


    def SM_ButtonClicked(self):
        print(" SM_ButtonClicked(self):")
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(480, 80,400, 400))
        tab1 = QtGui.QWidget(self)
        stand_button = QtGui.QPushButton("Stand", tab1)
        stand_button.move(100, 100)
        sit_button = QtGui.QPushButton("Sit", tab1)
        sit_button.move(200, 100)
        crouch_button = QtGui.QPushButton("Crouch", tab1)
        crouch_button.move(100, 200)
        lyingBack_button = QtGui.QPushButton("Lying Back", tab1)
        lyingBack_button.move(200, 200)
        lyingBelly_button = QtGui.QPushButton("Lying Belly", tab1)
        lyingBelly_button.move(300, 100)
        rest_button = QtGui.QPushButton("Rest", tab1)
        rest_button.move(300, 200)


        tab2 = QtGui.QWidget(self)

        horizontal_walk_label = QtGui.QLabel("Horizontal Vector", tab2)
        vertical_walk_label = QtGui.QLabel("Vertical Vector", tab2)
        radian_walk_label = QtGui.QLabel("Radian Vector", tab2)
        horizontal_walk_label.move(100, 100)
        vertical_walk_label.move(100, 200)
        radian_walk_label.move(100, 300)


        hSlider = QtGui.QSlider(tab2)
        hSlider.setGeometry(QtCore.QRect(200, 100, 160, 22))
        hSlider.setOrientation(QtCore.Qt.Horizontal)
        vSlider = QtGui.QSlider(tab2)
        vSlider.setGeometry(QtCore.QRect(200, 200, 160, 22))
        vSlider.setOrientation(QtCore.Qt.Horizontal)
        rSlider = QtGui.QSlider(tab2)
        rSlider.setGeometry(QtCore.QRect(200, 300, 160, 22))
        rSlider.setOrientation(QtCore.Qt.Horizontal)

        lcd = QtGui.QLCDNumber(tab2)
        hSlider.valueChanged.connect(lcd.display)


        self.tabWidget.addTab(tab1,"Whole Body Motion")
        self.tabWidget.addTab(tab2,"Walking Motion")


        self.tabWidget.show()





    def RM_ButtonClicked(self):
        self.tabWidget2 = QtGui.QTabWidget(self)
        self.tabWidget2.setGeometry(QtCore.QRect(480, 80, 500, 400))
        tab1 = QtGui.QWidget(self)
        tab2 = QtGui.QWidget(self)

        self.tabWidget2.addTab(tab1, "Continuous Recording")
        self.tabWidget2.addTab(tab2, "Click Button Recording")

        con_record_button = QtGui.QPushButton("Start Continuous Record", tab1)
        con_record_button.move(100, 200)

        con_replay_button = QtGui.QPushButton("Start Replay", tab1)
        con_replay_button.move(100, 300)

        set_time_label = QtGui.QLabel("Set Time", tab1)
        set_time_label.move(100, 100)

        click_record_button = QtGui.QPushButton("Start Click Button Record", tab2)
        click_record_button.move(100, 100)

        replay_button = QtGui.QPushButton("Start Replay", tab2)
        replay_button.move(100, 200)

        self.tabWidget2.show()

        self.connect(con_record_button, QtCore.SIGNAL('clicked()'),
                     self.Con_Record_Clicked)
        self.connect(replay_button, QtCore.SIGNAL('clicked()'),
                     self.Replay_Clicked)
        self.connect(click_record_button, QtCore.SIGNAL('clicked()'),
                     self.Click_Record_Clicked)

    def Con_Record_Clicked(self):
        posture.goToPosture("StandInit", 1.0)
        motion.setStiffnesses("Body", 1)
        ub.record_animation1(motion, memory, "C:/Users/zeyu/Desktop/Nao/", 50, "result.csv")
        motion.rest()

    def Click_Record_Clicked(self):
        posture.goToPosture("StandInit", 1.0)
        motion.setStiffnesses("Body", 1)
        ub.record_animation_buttons(motion, memory, "C:/Users/zeyu/Desktop/Nao/", "result.csv")
        motion.rest()

    def Replay_Clicked(self):
        motion.setStiffnesses("Body", 1)
        posture.goToPosture("StandInit", 1.0)
        aup.post.playFile("/home/nao/naoGUI/sugar.wav")
        Util.load_animation(motion, "C:/Users/zeyu/Desktop/Nao/result.csv")
        aup.stopAll()
        posture.goToPosture("Crouch", 1.0)
        motion.rest()

    def BM_ButtonClicked(self):
        self.close()
        self.tabWidget.close()
        self.tabWidget2.close()