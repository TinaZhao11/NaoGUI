'''This project is created by Zeyu Zhao
This package contains all GUI design used for user interface

This audio_view is the audio view for the desktop application
This file will open the audio module of the GUI Part'''


from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QFont
from naoqi import ALProxy

import Controller as con
from robot import Util as ul

IP = ul.RobotIP
PORT = ul.RobotPORT


class Audio_View(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Audio_View, self).__init__(parent)
        self.initUI()
        self.tabWidget1 = QtGui.QTabWidget()
        self.tabWidget2 = QtGui.QTabWidget()
        self.textEdit = QtGui.QTextEdit()
        self.volSlider = QtGui.QSlider()
        self.musicList = QtGui.QComboBox()

    # Draw the audio view for the application
    def initUI(self):
        # Set the window size and layout with background image and Icon
        self.resize(1000, 600)
        self.setWindowTitle('Audio')
        self.setWindowIcon(QtGui.QIcon('C:/Users/zeyu/Desktop/NaoGUI/image/Icon.png'))
        audioBG_image = QtGui.QPixmap()
        audioBG_image.load('C:/Users/zeyu/Desktop/NaoGUI/image/subBG.png')
        audioBG = QtGui.QPalette()
        audioBG.setBrush(self.backgroundRole(), QtGui.QBrush(audioBG_image))
        self.setPalette(audioBG)
        self.setAutoFillBackground(True)

    # Draw the components for audio, like button, label, slider
        volume_label = QtGui.QLabel(self)
        volume_label.setPixmap(QtGui.QPixmap('C:/Users/zeyu/Desktop/NaoGUI/image/volume.png'))
        volume_label.move(70, 50)

        Audio_View.volSlider = QtGui.QSlider(self)
        Audio_View.volSlider.setGeometry(QtCore.QRect(130, 50, 210, 30))
        Audio_View.volSlider.setOrientation(QtCore.Qt.Horizontal)
        Audio_View.volSlider.setRange(0, 100)

        Talk_button = QtGui.QPushButton("Text to Speech", self)
        Talk_button.resize(180, 80)
        Talk_button.move(140, 150)
        Talk_button.setFont(QFont("Consolas", 15))

        BM_button = QtGui.QPushButton("Back to Main", self)
        BM_button.resize(180, 80)
        BM_button.move(140, 320)
        BM_button.setFont(QFont("Consolas", 15))

    # Set the connection event for each button
        self.connect(Talk_button, QtCore.SIGNAL('clicked()'),
                     self.set_Talk_view)
        self.connect(BM_button, QtCore.SIGNAL('clicked()'),
                     self.BM_ButtonClicked)

# Set the subview for audio
# Show the text to speech module
    def set_Talk_view(self):
        self.tabWidget2.close()

        self.tabWidget1 = QtGui.QTabWidget(self)
        self.tabWidget1.setGeometry(QtCore.QRect(420, 100, 480, 400))
        self.tabWidget1.setFont(QFont("Consolas", 16))

        input_label = QtGui.QLabel("Input", self.tabWidget1)
        input_label.move(20, 60)
        self.textEdit = QtGui.QTextEdit(self.tabWidget1)
        self.textEdit.resize(300, 170)
        self.textEdit.move(100, 60)

        talk_button = QtGui.QPushButton("Talk", self.tabWidget1)
        talk_button.resize(150, 50)
        talk_button.move(180, 280)

        self.tabWidget1.show()

        self.connect(talk_button, QtCore.SIGNAL('clicked()'),
                     self.talk_ButtonClicked)

# This function used to send the text to speech for robot
    def talk_ButtonClicked(self):
        print(self.textEdit.toPlainText())
        text = str(self.textEdit.toPlainText())
        print(Audio_View.volSlider.value())
        volume = float(Audio_View.volSlider.value())
        print(volume)
        con.talk_motion(text,volume)
        self.textEdit.clear()

# This function used to back to mainMenu
    def BM_ButtonClicked(self):
        self.tabWidget1.close()
        self.tabWidget2.close()
        self.close()