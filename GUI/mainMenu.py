'''This GUI project is created by Zeyu Zhao
This mainMenu is a part of GUI  project, aim to show the GUI'''

#!/usr/bin/python

# Draw the mainMenu for the Naopy App
import sys

from PyQt4 import QtGui
from PyQt4.QtGui import QFont

from GUI import animation_view
from GUI import audio_view
from GUI import suprise_view


class MainMenu(QtGui.QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setMainWindow()
        self.Animation = animation_view.Animation_View()
        self.Audio = audio_view.Audio_View()
        self.Suprise = suprise_view.Suprise_View()

    def setMainWindow(self):
        #Draw the main windows
        self.resize(1000, 600)
        self.setWindowTitle('Naopy')
        self.setWindowIcon(QtGui.QIcon('C:/Users/zeyu/Desktop/NaoGUI/image/Icon.png'))

        mainBG_image = QtGui.QPixmap()
        mainBG_image.load('C:/Users/zeyu/Desktop/NaoGUI/image/mainBG.png')
        mainBG = QtGui.QPalette()
        mainBG.setBrush(self.backgroundRole(), QtGui.QBrush(mainBG_image))
        self.setPalette(mainBG)
        self.setAutoFillBackground(True)


        #Draw the button for the mainMenu
        self.button1 = QtGui.QPushButton("Animation", self)
        self.button1.resize(180, 80)
        self.button1.move(200, 60)
        self.button1.setFont(QFont("Consolas",20))

        self.button2 = QtGui.QPushButton("Audio", self)
        self.button2.resize(180, 80)
        self.button2.move(200, 190)
        self.button2.setFont(QFont("Consolas", 20))

        self.button3 = QtGui.QPushButton("Surprise", self)
        self.button3.resize(180, 80)
        self.button3.move(200, 320)
        self.button3.setFont(QFont("Consolas", 20))

        self.button4 = QtGui.QPushButton("Exit", self)
        self.button4.resize(180, 80)
        self.button4.move(200, 450)
        self.button4.setFont(QFont("Consolas", 20))

        self.button1.clicked.connect(self.button1_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
    # Set the window into Center

    def button1_clicked(self):
        # self.hide()
        # Form1 = QtGui.QDialog()
        self.Animation.show()
        print("button1_clicked")

    def button2_clicked(self):
        # self.hide()
        # Form1 = QtGui.QDialog()
        self.Audio.show()
        print("button2_clicked")

    def button3_clicked(self):
        # self.hide()
        # Form1 = QtGui.QDialog()
        self.Suprise.show()
        print("button3_clicked")

    def button4_clicked(self):
        # self.hide()
        # Form1 = QtGui.QDialog()
        # self.hide()
        self.close()
        print("button4_clicked")
