# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *
import sys
from robot import footstep

def createConnection():
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("animation.db")
    db.open()

def createTable():
    q = QSqlQuery()
    q.exec_("create table if not exists RobotConnection (IP varchar(20), PORT integer primary key,)")
    q.exec_("delete from RobotConnection")
    q.exec_(u"insert into RobotConnection values('127.0.0.1',9559)")
    q.exec_("commit")


class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        self.setTable("RobotConnection")
        self.select()
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)


class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        vbox = QVBoxLayout(self)
        self.view = QTableView()
        self.model = Model(self.view)
        self.view.setModel(self.model)
        vbox.addWidget(self.view)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    createConnection()
    createTable()
    w = TestWidget()
    w.show()
    sys.exit(a.exec_())  