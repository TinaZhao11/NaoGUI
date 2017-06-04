from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from naoqi import ALProxy

import Controller as con
from robot import Util as ul

IP = ul.RobotIP
PORT = ul.RobotPORT

class Suprise_View(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Suprise_View, self).__init__(parent)
        self.initUI()
        self.volSlider = QtGui.QSlider()

    def initUI(self):
        self.resize(1000, 600)
        self.setWindowTitle('Surprise Demo')
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

        Suprise_View.volSlider = QtGui.QSlider(self)
        Suprise_View.volSlider.setGeometry(QtCore.QRect(130, 50, 210, 30))
        Suprise_View.volSlider.setOrientation(QtCore.Qt.Horizontal)
        Suprise_View.volSlider.setRange(0, 100)

        SM_button = QtGui.QPushButton("Dance Demo1", self)
        SM_button.resize(180, 80)
        SM_button.move(140, 100)
        SM_button.setFont(QFont("Consolas", 15))

        RM_button = QtGui.QPushButton("Dance Demo2", self)
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


        self.connect(BM_button, QtCore.SIGNAL('clicked()'),
                     self.BM_ButtonClicked)
        self.connect(MR_button, QtCore.SIGNAL('clicked()'),
                     con.stop_all)

        self.connect(SM_button, QtCore.SIGNAL('clicked()'),
                     con.demo1)
        self.connect(RM_button, QtCore.SIGNAL('clicked()'),
                     con.demo2)

    def BM_ButtonClicked(self):
        self.close()