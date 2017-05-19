from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from naoqi import ALProxy

import Controller as con
from robot import Util

IP = Util.IP
PORT = Util.PORT

motion = ALProxy("ALMotion", IP, PORT)
motion1 = ALProxy("ALMotion", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)

class Animation_View(QtGui.QWidget):

    def __init__(self,parent=None):
        super(Animation_View, self).__init__(parent)
        self.initUI()
        self.tabWidget1 = QtGui.QTabWidget()
        self.tabWidget2 = QtGui.QTabWidget()
        self.lcd1 = QtGui.QLCDNumber()
        self.lcd2 = QtGui.QLCDNumber()
        self.lcd3 = QtGui.QLCDNumber()
        self.lcd4 = QtGui.QLCDNumber()
        self.music = QtGui.QRadioButton()
        self.leg = QtGui.QRadioButton()
        self.con_sub = QtGui.QGraphicsView()
        self.click_label = QtGui.QLabel()
        self.volSlider = QtGui.QSlider()



    def initUI(self):
        self.resize(1000, 600)
        self.setWindowTitle('Animation')
        self.setWindowIcon(QtGui.QIcon('image/Icon.png'))

        animationBG_image = QtGui.QPixmap()
        animationBG_image.load('image/subBG.png')
        animationBG = QtGui.QPalette()
        animationBG.setBrush(self.backgroundRole(), QtGui.QBrush(animationBG_image))
        self.setPalette(animationBG)
        self.setAutoFillBackground(True)

        volume_label = QtGui.QLabel(self)
        volume_label.setPixmap(QtGui.QPixmap('image/volume.png'))
        volume_label.move(70, 50)

        Animation_View.volSlider = QtGui.QSlider(self)
        Animation_View.volSlider.setGeometry(QtCore.QRect(130, 50, 210, 30))
        Animation_View.volSlider.setOrientation(QtCore.Qt.Horizontal)
        Animation_View.volSlider.setRange(0, 100)

        SM_button = QtGui.QPushButton("Standard Motion", self)
        SM_button.resize(180, 80)
        SM_button.move(140, 100)
        SM_button.setFont(QFont("Consolas", 15))

        RM_button = QtGui.QPushButton("Record Motion", self)
        RM_button.resize(180, 80)
        RM_button.move(140, 260)
        RM_button.setFont(QFont("Consolas", 15))

        BM_button = QtGui.QPushButton("Back to Main", self)
        BM_button.resize(180, 80)
        BM_button.move(140, 420)
        BM_button.setFont(QFont("Consolas", 15))

        MR_button = QtGui.QPushButton("Rest", self)
        MR_button.resize(80, 80)
        MR_button.move(900, 20)
        MR_button.setFont(QFont("Consolas", 14))


        self.connect(SM_button, QtCore.SIGNAL('clicked()'),
                     self.set_SM_view)

        self.connect(RM_button, QtCore.SIGNAL('clicked()'),
            self.set_RM_view)

        self.connect(BM_button, QtCore.SIGNAL('clicked()'),
                     self.BM_ButtonClicked)

        self.connect(MR_button, QtCore.SIGNAL('clicked()'),
                     con.rest_motion)


    def set_SM_view(self):
        print(" set_SM_view:")
        self.tabWidget2.close()

        self.tabWidget1 = QtGui.QTabWidget(self)
        self.tabWidget1.setGeometry(QtCore.QRect(420, 100, 480, 400))

        tab1 = QtGui.QWidget()

        stand_button = QtGui.QPushButton("Stand", tab1)
        stand_button.resize(100, 50)
        stand_button.move(40, 80)
        self.connect(stand_button, QtCore.SIGNAL('clicked()'),
                     con.stand_motion)

        sit_button = QtGui.QPushButton("Sit", tab1)
        sit_button.move(160, 80)
        sit_button.resize(100, 50)
        self.connect(sit_button, QtCore.SIGNAL('clicked()'),
                     con.sit_motion)

        rest_button = QtGui.QPushButton("Rest", tab1)
        rest_button.move(40, 200)
        rest_button.resize(100, 50)
        self.connect(rest_button, QtCore.SIGNAL('clicked()'),
                     con.rest_motion)

        crouch_button = QtGui.QPushButton("Crouch", tab1)
        crouch_button.resize(100, 50)
        crouch_button.move(160, 200)
        self.connect(crouch_button, QtCore.SIGNAL('clicked()'),
                     con.crouch_motion)

        lyingBack_button = QtGui.QPushButton("Lying Back", tab1)
        lyingBack_button.move(285, 200)
        lyingBack_button.resize(150, 50)
        self.connect(lyingBack_button, QtCore.SIGNAL('clicked()'),
                     con.lyback_motion)

        lyingBelly_button = QtGui.QPushButton("Lying Belly", tab1)
        lyingBelly_button.move(285, 80)
        lyingBelly_button.resize(150, 50)
        self.connect(lyingBelly_button, QtCore.SIGNAL('clicked()'),
                     con.lyback_motion)

       # self.connect(rest_button, QtCore.SIGNAL('clicked()'),
        #             con.rest_motion())

        tab2 = QtGui.QWidget(self)

        horizontal_walk_label = QtGui.QLabel("Horizontal", tab2)
        vertical_walk_label = QtGui.QLabel("Vertical", tab2)
        radian_walk_label = QtGui.QLabel("Radian", tab2)
        horizontal_walk_label.move(50, 100)
        vertical_walk_label.move(50, 170)
        radian_walk_label.move(50, 240)


        hSlider = QtGui.QSlider(tab2)
        hSlider.setGeometry(QtCore.QRect(200, 100, 160, 22))
        hSlider.setOrientation(QtCore.Qt.Horizontal)
        hSlider.setRange(-20, 20)
        vSlider = QtGui.QSlider(tab2)
        vSlider.setGeometry(QtCore.QRect(200, 170, 160, 22))
        vSlider.setOrientation(QtCore.Qt.Horizontal)
        vSlider.setRange(-20, 20)
        rSlider = QtGui.QSlider(tab2)
        rSlider.setGeometry(QtCore.QRect(200, 240, 160, 22))
        rSlider.setOrientation(QtCore.Qt.Horizontal)
        rSlider.setRange(0, 20)

        self.lcd1 = QtGui.QLCDNumber(tab2)
        self.lcd1.resize(100, 50)
        self.lcd1.move(50, 10)
        hSlider.valueChanged.connect(self.lcd1.display)

        self.lcd2 = QtGui.QLCDNumber(tab2)
        self.lcd2.resize(100, 50)
        self.lcd2.move(180, 10)
        vSlider.valueChanged.connect(self.lcd2.display)


        self.lcd3 = QtGui.QLCDNumber(tab2)
        self.lcd3.resize(100, 50)
        self.lcd3.move(310, 10)
        rSlider.valueChanged.connect(self.lcd3.display)



        walk_button = QtGui.QPushButton("Walk", tab2)
        walk_button.move(310, 280)
        walk_button.resize(100, 50)
        self.connect(walk_button, QtCore.SIGNAL('clicked()'),
                     self.get_walk_value)


        self.tabWidget1.addTab(tab1,"Whole Body Motion")
        self.tabWidget1.addTab(tab2,"Walking Motion")
        self.tabWidget1.setFont(QFont("Consolas", 16))

        self.tabWidget1.show()

    def get_walk_value(self):
        con.x = self.lcd1.value()
        con.y = self.lcd2.value()
        con.r = self.lcd3.value()
        con.walk_motion(con.x, con.y, con.r)


    def set_RM_view(self):
        self.tabWidget1.close()
        self.tabWidget2 = QtGui.QTabWidget(self)
        self.tabWidget2.setGeometry(QtCore.QRect(420, 100, 480, 400))
        tab1 = QtGui.QWidget()
        tab2 = QtGui.QWidget()

        self.tabWidget2.addTab(tab1, "Continuous Record")
        self.tabWidget2.addTab(tab2, "Intermittent Record")
        self.tabWidget2.setFont(QFont("Consolas", 16))

        set_time_label = QtGui.QLabel("Set Record Time", tab1)
        set_time_label.move(20, 30)

        tSlider = QtGui.QSlider(tab1)
        tSlider.setGeometry(QtCore.QRect(220, 70, 160, 22))
        tSlider.setOrientation(QtCore.Qt.Horizontal)
        tSlider.setRange(0, 100)

        self.lcd4 = QtGui.QLCDNumber(tab1)
        self.lcd4.resize(100, 50)
        self.lcd4.move(250, 10)
        tSlider.valueChanged.connect(self.lcd4.display)

        con_record_button = QtGui.QPushButton("StartRecord", tab1)
        con_record_button.move(130, 100)
        con_record_button.resize(200, 50)

        '''whitebg = QPalette()
        whitebg.setColor(QPalette.Background, QtGui.QColor(200,100,100))
        self.con_sub = QtGui.QGraphicsView(tab1)
        self.con_sub.move(130,  150)
        self.con_sub.resize(480, 200)
        self.con_sub.setPalette(whitebg)'''

        music_label = QtGui.QLabel("Music", tab1)
        music_label.move(20, 170)

        self.music1 = QtGui.QRadioButton("None" , tab1)
        self.music1.move(150, 170)
        self.music1.resize(100, 30)


        self.music2 = QtGui.QRadioButton("Music1", tab1)
        self.music2.move(230, 170)
        self.music2.resize(100, 30)

        self.music3 = QtGui.QRadioButton("Music2", tab1)
        self.music3.move(330, 170)
        self.music3.resize(100, 30)

        self.music_group1 = QtGui.QButtonGroup(tab1)
        self.music_group1.addButton(self.music1, 1)
        self.music_group1.addButton(self.music2, 2)
        self.music_group1.addButton(self.music3, 3)

        leg_label = QtGui.QLabel("Step", tab1)
        leg_label.move(20, 250)

        self.leg1 = QtGui.QRadioButton("None", tab1)
        self.leg1.move(150, 250)
        self.leg1.resize(100, 30)

        self.leg2 = QtGui.QRadioButton("Step1", tab1)
        self.leg2.move(230, 250)
        self.leg2.resize(100, 30)

        self.leg3 = QtGui.QRadioButton("Step2", tab1)
        self.leg3.move(330, 250)
        self.leg3.resize(100, 30)

        self.leg_group1 = QtGui.QButtonGroup(tab1)
        self.leg_group1.addButton(self.leg1, 1)
        self.leg_group1.addButton(self.leg2, 2)
        self.leg_group1.addButton(self.leg3, 3)

        con_replay_button = QtGui.QPushButton("Start Replay", tab1)
        con_replay_button.move(130, 300)
        con_replay_button.resize(200, 50)


        click_record_button = QtGui.QPushButton("Start Record", tab2)
        click_record_button.move(150, 30)
        click_record_button.resize(200, 50)

        music_label = QtGui.QLabel("Music", tab2)
        music_label.move(20, 130)

        self.music1 = QtGui.QRadioButton("None", tab2)
        self.music1.move(150, 130)
        self.music1.resize(100, 30)

        self.music2 = QtGui.QRadioButton("Music1", tab2)
        self.music2.move(230, 130)
        self.music2.resize(100, 30)

        self.music3 = QtGui.QRadioButton("Music2", tab2)
        self.music3.move(330, 130)
        self.music3.resize(100, 30)

        self.music_group2 = QtGui.QButtonGroup(tab2)
        self.music_group2.addButton(self.music1, 1)
        self.music_group2.addButton(self.music2, 2)
        self.music_group2.addButton(self.music3, 3)

        leg_label = QtGui.QLabel("Step", tab2)
        leg_label.move(20, 210)

        self.leg1 = QtGui.QRadioButton("None", tab2)
        self.leg1.move(150, 210)
        self.leg1.resize(100, 30)

        self.leg2 = QtGui.QRadioButton("Step1", tab2)
        self.leg2.move(230, 210)
        self.leg2.resize(100, 30)

        self.leg3 = QtGui.QRadioButton("Step2", tab2)
        self.leg3.move(330, 210)
        self.leg3.resize(100, 30)

        self.leg_group2 = QtGui.QButtonGroup(tab2)
        self.leg_group2.addButton(self.leg1, 1)
        self.leg_group2.addButton(self.leg2, 2)
        self.leg_group2.addButton(self.leg3, 3)

        click_replay_button = QtGui.QPushButton("Start Replay", tab2)
        click_replay_button.move(150, 280)
        click_replay_button.resize(200, 50)

        self.tabWidget2.show()

        self.connect(con_record_button, QtCore.SIGNAL('clicked()'),
                     self.Con_Record_Clicked)
        self.connect(con_replay_button, QtCore.SIGNAL('clicked()'),
                     self.Con_Replay_Clicked)
        self.connect(click_replay_button, QtCore.SIGNAL('clicked()'),
                     self.Click_Replay_Clicked)
        self.connect(click_record_button, QtCore.SIGNAL('clicked()'),
                     self.Click_Record_Clicked)

    def Con_Record_Clicked(self):
        print(self.lcd4.value())
        loop = int(self.lcd4.value())
        con.con_record(loop)

    def Click_Record_Clicked(self):
        con.click_record()

    def Con_Replay_Clicked(self):
        print("Volume")
        print(Animation_View.volSlider.value())
        volume = Animation_View.volSlider.value()
        print(self.music_group1.checkedId())
        music = self.music_group1.checkedId()
        print(self.leg_group1.checkedId())
        step = self.leg_group1.checkedId()
        con.replay(music, step, volume)

    def Click_Replay_Clicked(self):
        music = self.music_group2.checkedId()
        print(self.leg_group2.checkedId())
        step = self.leg_group2.checkedId()
        con.replay(music, step)

    def BM_ButtonClicked(self):
        self.tabWidget1.close()
        self.tabWidget2.close()
        self.close()