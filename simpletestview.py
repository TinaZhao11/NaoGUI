#!/usr/bin/python
# -*- coding: utf-8 -*-
# sender.py

import time

from naoqi import ALProxy

from robot import Util, UpperBody as ub

IP = Util.IP
PORT = Util.PORT
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QMainWindow)


motion = ALProxy("ALMotion", IP, PORT)
motion1 = ALProxy("ALMotion", IP, PORT)
memory = ALProxy("ALMemory", IP, PORT)
posture = ALProxy("ALRobotPosture", IP, PORT)
aup = ALProxy("ALAudioPlayer", IP, PORT)

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def initUI(self):

        self.resize(1000, 800)
        self.setCenter()
        self.setWindowTitle('Animation')
        self.setWindowIcon(QtGui.QIcon('image/Icon.png'))

        button1 = QtGui.QPushButton("Record", self)
        button1.move(200, 200)

        button2 = QtGui.QPushButton("Replay", self)
        button2.move(400, 200)

        button3 = QtGui.QPushButton("RecordbyButton", self)
        button3.move(200, 400)

        button4 = QtGui.QPushButton("Back to Main", self)
        button4.move(200, 500)

        self.connect(button1, QtCore.SIGNAL('clicked()'),
            self.button1Clicked)

        self.connect(button2, QtCore.SIGNAL('clicked()'),
            self.button2Clicked)

        self.connect(button3, QtCore.SIGNAL('clicked()'),
                     self.button3Clicked)
        self.connect(button4, QtCore.SIGNAL('clicked()'),
                     self.button4Clicked)


    def setCenter(self):
        # type: () -> object
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def button1Clicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' is start')
        posture.goToPosture("StandInit", 1.0)
        motion.setStiffnesses("Body", 1)
        ub.record_animation1(motion, memory, "C:/Users/zeyu/Desktop/Nao/", 50, "result.csv")
        motion.rest()
        time.sleep(2.0)

    def button2Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' is start')
        motion.setStiffnesses("Body", 1)
        posture.goToPosture("StandInit", 1.0)
        #aup.post.playFile("/home/nao/naoGUI/sugar.wav")
       # up.load_animation(motion, "C:/Users/zeyu/Desktop/Nao/result.csv")

        #ub.load_animation_with_beats(motion, aup,beats_list, "C:/Users/zeyu/Desktop/NaoGUI/result.csv")
        aup.stopAll()
        posture.goToPosture("Crouch", 1.0)
        motion.rest()
        motion.setStiffnesses("Body", 0.0)

    def button3Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' is start')
        posture.goToPosture("StandInit", 1.0)
        motion.setStiffnesses("Body", 1)
        ub.record_animation_buttons(motion, memory, "C:/Users/zeyu/Desktop/Nao/", "result.csv")
        motion.rest()
        time.sleep(2.0)

    def button4Clicked(self):
        self.close()



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainMenu = Example()
    mainMenu.initUI()
    mainMenu.show()
    sys.exit(app.exec_())
