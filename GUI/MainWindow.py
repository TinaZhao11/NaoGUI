import connectRobot as CR
import sys
from naoqi import ALProxy

from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QFont
from PyQt4.QtCore import Qt
import sqlite3

app = QtGui.QApplication(sys.argv)
connect = CR.Connection()
connect.setConnectionWindow()
connect.show()
sys.exit(app.exec_())