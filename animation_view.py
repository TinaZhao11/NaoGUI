from PyQt4.QtGui import *
from PyQt4.QtCore import QString
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import (QMainWindow)


class Animation_View(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Animation_View, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(1000, 800)
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
        tabWidget = QtGui.QTabWidget(self)
        tabWidget.setGeometry(QtCore.QRect(480, 80,400, 400))
        tab1 = QtGui.QWidget(self)

        tab2 = QtGui.QWidget(self)

        horizontalSlider = QtGui.QSlider(tab2)
        horizontalSlider.setGeometry(QtCore.QRect(70, 150, 160, 22))
        horizontalSlider.set
        horizontalSlider.setOrientation(QtCore.Qt.Horizontal)


        tabWidget.addTab(tab1,"Whole Body Motion")
        tabWidget.addTab(tab2,"Walking Motion")


        tabWidget.show()





    def RM_ButtonClicked(self):
        tabWidget = QtGui.QTabWidget(self)
        tabWidget.setGeometry(QtCore.QRect(480, 80, 500, 400))
        tabWidget.show()

    def BM_ButtonClicked(self):
        self.close()

