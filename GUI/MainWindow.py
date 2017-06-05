'''This project is created by Zeyu Zhao
This package contains all GUI design used for user interface

This MainWindow is the main entrance to open the GUI
This file will open the connectRobot view and start the GUI part'''

import connectRobot as CR
import sys
from PyQt4 import QtGui,QtCore

app = QtGui.QApplication(sys.argv)
connect = CR.Connection()
connect.setConnectionWindow()
connect.show()
sys.exit(app.exec_())