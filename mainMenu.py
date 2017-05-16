#!/usr/bin/python

# Draw the mainMenu for the Naopy App

import sys
from PyQt4 import QtGui, QtCore
import animation_view


class MainMenu(QtGui.QWidget):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.Animation = animation_view.Animation_View()

    def setMainWindow(self):
        #Draw the main windows
        self.resize(1000, 600)
        self.setCenter()
        self.setWindowTitle('Naopy')
        self.setWindowIcon(QtGui.QIcon('image/Icon.png'))

        #Draw the button for the mainMenu
        self.button1 = QtGui.QPushButton("Animation", self)
        self.button1.resize(150, 80)
        self.button1.move(200, 50)

        self.button2 = QtGui.QPushButton("Audio", self)
        self.button2.resize(150, 80)
        self.button2.move(200, 200)

        self.button3 = QtGui.QPushButton("Suprise", self)
        self.button3.resize(150, 80)
        self.button3.move(200, 350)

        self.button4 = QtGui.QPushButton("Exit", self)
        self.button4.resize(150, 80)
        self.button4.move(200, 500)

        self.button1.clicked.connect(self.button1_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        #self.button2.clicked.connect(self.button2_clicked)
        #self.button3.clicked.connect(self.button3_clicked)
    # Set the window into Center
    def setCenter(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def button1_clicked(self):
        #self.hide()
        #Form1 = QtGui.QDialog()

        self.Animation.show()
        print("button1_clicked")

    def button4_clicked(self):
        # self.hide()
        # Form1 = QtGui.QDialog()
        # self.hide()
        self.close()
        print("button4_clicked")


        #Form1.exec_()
        #self.form.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainMenu = MainMenu()
    mainMenu.setMainWindow()
    mainMenu.show()
    sys.exit(app.exec_())