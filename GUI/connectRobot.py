import sys
from naoqi import ALProxy

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QFont
from PyQt4.QtCore import Qt
import sqlite3

conn = sqlite3.connect('C:/Users/zeyu/Desktop/NaoGUI/Database/animation.db')
c = conn.cursor()

RobotIP = ""
RobotPORT = 0

class Connection(QtGui.QWidget):
    def __init__(self):
        super(Connection, self).__init__()

    def setConnectionWindow(self):
        # Draw the connection windows and set window Icon
        self.resize(700, 500)
        self.setWindowTitle('Naopy')
        self.setWindowIcon(QtGui.QIcon('C:/Users/zeyu/Desktop/NaoGUI/image/Icon.png'))

        # Set background for connection window
        connectBG_image = QtGui.QPixmap()
        connectBG_image.load('C:/Users/zeyu/Desktop/NaoGUI/image/connectBG.png')
        connectBG = QtGui.QPalette()
        connectBG.setBrush(self.backgroundRole(), QtGui.QBrush(connectBG_image))
        self.setPalette(connectBG)
        self.setAutoFillBackground(True)

        # Draw the label and input widget for user to enter IP and Port number
        self.Title = QtGui.QLabel("Welcome to Connect Nao's World!", self)
        self.Title.move(150, 90)
        self.Title.setFont(QFont("Consolas", 18))

        self.labelIP = QtGui.QLabel("Robot IP", self)
        self.labelIP.move(180, 150)
        self.labelIP.setFont(QFont("Consolas",12))
        self.labelPORT = QtGui.QLabel("Robot PORT", self)
        self.labelPORT.move(180, 200)
        self.labelPORT.setFont(QFont("Consolas", 12))

        self.inputIP = QtGui.QPlainTextEdit(self)
        self.inputIP.resize(200, 30)
        self.inputIP.move(300, 145)
        self.inputIP.setFont(QFont("Consolas", 12))

        self.inputPORT = QtGui.QPlainTextEdit(self)
        self.inputPORT.resize(200, 30)
        self.inputPORT.move(300, 195)
        self.inputPORT.setFont(QFont("Consolas", 12))


        # Draw the button for the connection winsow, contains conect and enter mainmenu
        # Connect button will check the robot IP and Port, show the user valid result
        self.connect_button = QtGui.QPushButton("Connect", self)
        self.connect_button.resize(100, 40)
        self.connect_button.move(300, 240)
        self.connect_button.setFont(QFont("Consolas",12))

        self.enter_button = QtGui.QPushButton("Enter MainMenu", self)
        self.enter_button.resize(150, 40)
        self.enter_button.move(300, 320)
        self.enter_button.setFont(QFont("Consolas", 12))
        self.enter_button.setDisabled(True)

        self.invalidlabel = QtGui.QLabel("", self)
        self.invalidlabel.setFont(QFont("Consolas", 12))
        self.invalidlabel.move(200, 285)
        self.invalidlabel.resize(300, 30)
        pe = QtGui.QPalette()
        pe.setColor(QtGui.QPalette.WindowText, Qt.red)
        self.invalidlabel.setPalette(pe)

        self.validlabel = QtGui.QLabel("", self)
        self.validlabel.setFont(QFont("Consolas", 12))
        self.validlabel.move(200, 285)
        self.validlabel.resize(400, 30)
        pe1 = QtGui.QPalette()
        pe1.setColor(QtGui.QPalette.WindowText, Qt.black)
        self.validlabel.setPalette(pe1)

        self.connect(self.connect_button, QtCore.SIGNAL('clicked()'),
                     self.check_Connect)
        self.connect(self.enter_button, QtCore.SIGNAL('clicked()'),
                     self.showMainMenu)


    def check_Connect(self):
        IP = str(self.inputIP.toPlainText())
        PORT = int(self.inputPORT.toPlainText())
        try:
            ALProxy("ALMotion", IP, PORT)
        except Exception:
            self.invalidlabel.setText("Invalid Robot IP and PORT Number!")
            self.enter_button.setDisabled(True)
        else:
            self.RobotIP = IP
            self.RobotPORT = PORT
            self.updateRobotInfo()
            self.invalidlabel.setText("")
            self.validlabel.setText("Connected! Click Enter MainMenu to Continue!")
            self.enter_button.setDisabled(False)

    def updateRobotInfo(self):
        #c.execute("uodate robotinfo(id,ip,port) values (%d,'%s','%d')"%(1,RobotIP,RobotPORT))
        print(self.RobotIP)
        print(self.RobotPORT)
        c.execute("update robotinfo set ip='%s' where id = 1"%(self.RobotIP))
        c.execute("update robotinfo set port='%d' where id = 1" % (self.RobotPORT))
        conn.commit()
        for row in c.execute("SELECT * FROM robotinfo "):
            print row

    def showMainMenu(self):
        self.close()
        print("showMainMenu")
        import mainMenu as mM
        self.mainM = mM.MainMenu()
        self.mainM.show()


