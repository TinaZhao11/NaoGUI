from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from naoqi import ALProxy
import sys
import manageData as mD
from PyQt4.QtCore import Qt

import Controller as con
from robot import Util as ul

IP = ul.RobotIP
PORT = ul.RobotPORT

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
        self.tabWidget3 = QtGui.QTabWidget()
        self.inputName = QtGui.QPlainTextEdit()
        self.inputName2 = QtGui.QPlainTextEdit()
        self.lcd1 = QtGui.QLCDNumber()
        self.lcd2 = QtGui.QLCDNumber()
        self.lcd3 = QtGui.QLCDNumber()
        self.lcd4 = QtGui.QLCDNumber()
        self.music = QtGui.QRadioButton()
        self.leg = QtGui.QRadioButton()
        self.con_sub = QtGui.QGraphicsView()
        self.click_label = QtGui.QLabel()
        self.volSlider = QtGui.QSlider()
        self.animationList = QtGui.QComboBox()
        self.animationList1 = QtGui.QComboBox()



    def initUI(self):
        self.resize(1000, 600)
        self.setWindowTitle('Animation')
        self.setWindowIcon(QtGui.QIcon('C:/Users/zeyu/Desktop/NaoGUI/image/Icon.png'))

        animationBG_image = QtGui.QPixmap()
        animationBG_image.load('C:/Users/zeyu/Desktop/NaoGUI/image/subBG.png')
        animationBG = QtGui.QPalette()
        animationBG.setBrush(self.backgroundRole(), QtGui.QBrush(animationBG_image))
        self.setPalette(animationBG)
        self.setAutoFillBackground(True)

        volume_label = QtGui.QLabel(self)
        volume_label.setPixmap(QtGui.QPixmap('C:/Users/zeyu/Desktop/NaoGUI/image/volume.png'))
        volume_label.move(70, 50)

        Animation_View.volSlider = QtGui.QSlider(self)
        Animation_View.volSlider.setGeometry(QtCore.QRect(130, 50, 210, 30))
        Animation_View.volSlider.setOrientation(QtCore.Qt.Horizontal)
        Animation_View.volSlider.setRange(0, 100)

        SM_button = QtGui.QPushButton("Standard Module", self)
        SM_button.resize(180, 80)
        SM_button.move(140, 100)
        SM_button.setFont(QFont("Consolas", 15))

        RM_button = QtGui.QPushButton("Record Module", self)
        RM_button.resize(180, 80)
        RM_button.move(140, 220)
        RM_button.setFont(QFont("Consolas", 15))

        BM_button = QtGui.QPushButton("Back to Main", self)
        BM_button.resize(180, 80)
        BM_button.move(140, 460)
        BM_button.setFont(QFont("Consolas", 15))

        RPM_button = QtGui.QPushButton("Replay Module", self)
        RPM_button.resize(180, 80)
        RPM_button.move(140, 340)
        RPM_button.setFont(QFont("Consolas", 15))

        MR_button = QtGui.QPushButton("Rest", self)
        MR_button.resize(80, 80)
        MR_button.move(900, 20)
        MR_button.setFont(QFont("Consolas", 14))

        S1_button = QtGui.QPushButton("Fixed", self)
        S1_button.resize(80, 80)
        S1_button.move(800, 20)
        S1_button.setFont(QFont("Consolas", 14))

        S0_button = QtGui.QPushButton("Relax", self)
        S0_button.resize(80, 80)
        S0_button.move(700, 20)
        S0_button.setFont(QFont("Consolas", 14))


        self.connect(SM_button, QtCore.SIGNAL('clicked()'),
                     self.set_SM_view)

        self.connect(RM_button, QtCore.SIGNAL('clicked()'),
            self.set_RM_view)

        self.connect(RPM_button, QtCore.SIGNAL('clicked()'),
                     self.set_RPM_view)

        self.connect(BM_button, QtCore.SIGNAL('clicked()'),
                     self.BM_ButtonClicked)
        self.connect(MR_button, QtCore.SIGNAL('clicked()'),
                     con.stop_all)

        self.connect(S1_button, QtCore.SIGNAL('clicked()'),
                     con.s1)

        self.connect(S0_button, QtCore.SIGNAL('clicked()'),
                     con.s0)


    def set_SM_view(self):
        print(" set_SM_view:")
        self.tabWidget2.close()
        self.tabWidget3.close()

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

    def set_RM_view(self):
        self.tabWidget1.close()
        self.tabWidget3.close()
        self.tabWidget2 = QtGui.QTabWidget(self)
        self.tabWidget2.setGeometry(QtCore.QRect(420, 100, 480, 400))
        tab1 = QtGui.QWidget()
        tab2 = QtGui.QWidget()

        self.tabWidget2.addTab(tab1, "Free Mode")
        self.tabWidget2.addTab(tab2, "Button Mode")
        self.tabWidget2.setFont(QFont("Consolas", 16))

        set_name_label = QtGui.QLabel("Set RecordName", tab1)
        set_name_label.move(20, 30)

        self.inputName = QtGui.QPlainTextEdit(tab1)
        self.inputName.resize(250, 40)
        self.inputName.move(200, 25)

        check_button = QtGui.QPushButton("Check Name", tab1)
        check_button.move(40, 75)
        check_button.resize(150, 40)

        self.invalidlabel = QtGui.QLabel("", tab1)
        self.invalidlabel.setFont(QFont("Consolas", 14))
        self.invalidlabel.move(230, 80)
        self.invalidlabel.resize(200, 30)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, Qt.red)
        self.invalidlabel.setPalette(pe)

        self.validlabel = QtGui.QLabel("", tab1)
        self.validlabel.setFont(QFont("Consolas", 14))
        self.validlabel.move(230, 80)
        self.validlabel.resize(200, 30)
        pe1 = QtGui.QPalette()
        pe1.setColor(QtGui.QPalette.WindowText, Qt.black)
        self.validlabel.setPalette(pe1)

        self.con_record_button = QtGui.QPushButton("Start Record", tab1)
        self.con_record_button.move(200, 150)
        self.con_record_button.resize(200, 50)

        delete_button = QtGui.QPushButton("Delete", tab1)
        delete_button.move(230, 280)
        delete_button.resize(150, 50)

        list_label = QtGui.QLabel("RecordList", tab1)
        list_label.setFont(QFont("Consolas", 16))
        list_label.move(20,220)
        self.animationList = QtGui.QComboBox(tab1)
        self.animationList.insertItem(1, "")
        self.animationList.resize(300, 40)
        self.animationList.move(150, 215)


        set_time_label = QtGui.QLabel("Set RecordName", tab2)
        set_time_label.move(20, 30)

        self.inputName1 = QtGui.QPlainTextEdit(tab2)
        self.inputName1.resize(250, 40)
        self.inputName1.move(200, 25)

        check_button1 = QtGui.QPushButton("Check Name", tab2)
        check_button1.move(40, 75)
        check_button1.resize(150, 40)

        self.invalidlabel1 = QtGui.QLabel("", tab2)
        self.invalidlabel1.setFont(QFont("Consolas", 14))
        self.invalidlabel1.move(230, 80)
        self.invalidlabel1.resize(200, 30)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, Qt.red)
        self.invalidlabel1.setPalette(pe)

        self.validlabel1 = QtGui.QLabel("", tab2)
        self.validlabel1.setFont(QFont("Consolas", 14))
        self.validlabel1.move(230, 80)
        self.validlabel1.resize(200, 30)
        pe1 = QtGui.QPalette()
        pe1.setColor(QtGui.QPalette.WindowText, Qt.black)
        self.validlabel1.setPalette(pe1)

        self.click_record_button = QtGui.QPushButton("Start Record", tab2)
        self.click_record_button.move(200, 150)
        self.click_record_button.resize(200, 50)

        list_label1 = QtGui.QLabel("RecordList", tab2)
        list_label1.setFont(QFont("Consolas", 16))
        list_label1.move(20, 220)
        self.animationList1 = QtGui.QComboBox(tab2)
        self.animationList1.insertItem(1, "")
        self.animationList1.resize(300, 40)
        self.animationList1.move(150, 215)

        delete_button1 = QtGui.QPushButton("Delete", tab2)
        delete_button1.move(230, 280)
        delete_button1.resize(150, 50)


        self.tabWidget2.show()

        self.con_record_button.setDisabled(True)
        self.click_record_button.setDisabled(True)

        self.connect(self.con_record_button, QtCore.SIGNAL('clicked()'),
                     self.Con_Record_Clicked)
        self.connect(self.click_record_button, QtCore.SIGNAL('clicked()'),
                     self.Click_Record_Clicked)
        self.connect(delete_button, QtCore.SIGNAL('clicked()'),
                     self.delete_animation)
        self.connect(delete_button1, QtCore.SIGNAL('clicked()'),
                     self.delete_animation1)
        self.connect(check_button, QtCore.SIGNAL('clicked()'),
                     self.check_name)
        self.connect(check_button1, QtCore.SIGNAL('clicked()'),
                     self.check_name1)

    def set_RPM_view(self):
        print(" set_RPM_view:")
        self.tabWidget2.close()
        self.tabWidget1.close()

        self.tabWidget3 = QtGui.QTabWidget(self)
        self.tabWidget3.setGeometry(QtCore.QRect(420, 100, 480, 400))

        tab1 = QtGui.QWidget()

        self.tabWidget3.addTab(tab1, "Replay Module")
        self.tabWidget3.setFont(QFont("Consolas", 16))

        self.recrodlabel = QtGui.QLabel("RecordList", tab1)
        self.recrodlabel.setFont(QFont("Consolas", 16))
        self.recrodlabel.move(10, 20)
        self.animationList = QtGui.QComboBox(tab1)
        self.animationList.insertItem(0, "RecordList")
        self.animationList.insertItem(1, "None")
        self.animationList.resize(300, 40)
        self.animationList.move(150, 15)

        self.musiclabel = QtGui.QLabel("MusicList", tab1)
        self.musiclabel.setFont(QFont("Consolas", 16))
        self.musiclabel.move(10, 80)
        self.musicList = QtGui.QComboBox(tab1)
        self.musicList.insertItem(0, "MusicList")
        self.musicList.insertItem(1, "None")
        self.musicList.resize(300, 40)
        self.musicList.move(150, 75)

        self.steplabel = QtGui.QLabel("StepList", tab1)
        self.steplabel.setFont(QFont("Consolas", 16))
        self.steplabel.move(10, 140)
        self.stepList = QtGui.QComboBox(tab1)
        self.stepList.insertItem(0, "StepList")
        self.stepList.insertItem(1, "None")
        self.stepList.resize(300, 40)
        self.stepList.move(150, 135)

        replay_button = QtGui.QPushButton("Start Replay", tab1)
        replay_button.move(140, 280)
        replay_button.resize(200, 50)

        self.set_recordList()
        self.set_musicList()
        self.set_stepList()
        self.tabWidget3.show()

        self.connect(replay_button, QtCore.SIGNAL('clicked()'),
                     self.replay_clicked)

    def get_walk_value(self):
        con.x = self.lcd1.value()
        con.y = self.lcd2.value()
        con.r = self.lcd3.value()
        con.walk_motion(con.x, con.y, con.r)


    def Con_Record_Clicked(self):
        print("Con_Record_Clicked")
        print(self.inputName.toPlainText())
        #print(mD.check_record_name(self.inputName.toPlainText()))
        if(mD.check_record_name(self.inputName.toPlainText()) == True):
            con.con_record(self.inputName.toPlainText())
        self.set_animationList()

    def Click_Record_Clicked(self):
        print("Con_Record_Clicked")
        print(self.inputName1.toPlainText())
        #print(mD.check_record_name(self.inputName.toPlainText()))
        if(mD.check_record_name(self.inputName1.toPlainText()) == True):
            con.click_record(self.inputName1.toPlainText())
        self.set_animationList()

    def delete_animation(self):
        listname = str(self.animationList.currentText())
        index = self.animationList.currentIndex()
        mD.delete_record(listname)
        print("listname")
        print listname
        self.animationList.removeItem(index)

    def delete_animation1(self):
        listname = str(self.animationList1.currentText())
        index = self.animationList1.currentIndex()
        mD.delete_record(listname)
        print("listname")
        print listname
        self.animationList1.removeItem(index)

    def set_animationList(self):
        index = 2
        nameList = mD.sendNameList()
        print(nameList)
        for line in nameList:
            self.animationList.insertItem(index, line)
            self.animationList1.insertItem(index, line)
            index = index + 1

    def set_recordList(self):
        index = 2
        nameList = mD.sendNameList()
        lengthlist = mD.sendRecordLengthList()
        print(nameList)
        for line in nameList:
            insert = line
            self.animationList.insertItem(index, insert)
            index = index + 1

    def set_musicList(self):
        index = 2
        nameList = mD.sendMusicList()
        lengthlist = mD.sendMusicLengthList()
        print(nameList)
        for line in nameList:
            insert = line
            self.musicList.insertItem(index, insert)
            index = index + 1

    def set_stepList(self):
        index = 2
        nameList = mD.sendStepList()
        lengthlist = mD.sendStepLengthList()
        print(nameList)
        for line in nameList:
            insert = line
            self.stepList.insertItem(index, insert)
            index = index + 1


    def check_name(self):
        print"Checkname"
        if (mD.check_record_name(self.inputName.toPlainText())):
            print("Set Name")
            self.invalidlabel.setText("")
            self.validlabel.setText("Valid Name!")
            self.con_record_button.setDisabled(False)
        else:
            self.validlabel.setText("")
            self.invalidlabel.setText("Name Already Exist!")

    def check_name1(self):
        print"Checkname"
        if (mD.check_record_name(self.inputName1.toPlainText())):
            print("Set Name")
            self.invalidlabel1.setText("")
            self.validlabel1.setText("Valid Name!")
            self.click_record_button.setDisabled(False)
        else:
            self.validlabel1.setText("")
            self.invalidlabel1.setText("Name Already Exist!")


    def replay_clicked(self):
        print("Volume")
        print(Animation_View.volSlider.value())
        volume = Animation_View.volSlider.value()
        animation = self.animationList.currentText()
        music = self.musicList.currentText()
        step = self.stepList.currentText()
        print(animation)
        print(music)
        print(step)
        con.replay(music, step, animation, volume)

    def BM_ButtonClicked(self):
        self.tabWidget1.close()
        self.tabWidget2.close()
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    connect = Animation_View()
    connect.show()
    sys.exit(app.exec_())

