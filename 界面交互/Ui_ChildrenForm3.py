# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\黄翰林\Desktop\数据库大作业\前端制作\GaoKao\ChildrenForm3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import(QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from ConnectDB import *

class Ui_ChildrenFrom3(object):
    def setupUi(self, ChildrenFrom3):
        ChildrenFrom3.setObjectName("ChildrenFrom3")
        ChildrenFrom3.resize(1200, 1000)
        self.tableWidget = QtWidgets.QTableWidget(ChildrenFrom3)
        self.tableWidget.setGeometry(QtCore.QRect(80, 300, 1100, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        
        self.label = QtWidgets.QLabel(ChildrenFrom3)
        self.label.setGeometry(QtCore.QRect(400, 40, 500, 80))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("lineEdit")


        self.retranslateUi(ChildrenFrom3)
        QtCore.QMetaObject.connectSlotsByName(ChildrenFrom3)

    def retranslateUi(self, ChildrenFrom3):
        _translate = QtCore.QCoreApplication.translate
        ChildrenFrom3.setWindowTitle(_translate("ChildrenFrom3", "Form"))
        
        # _translate = QtCore.QCoreApplication.translate
        #ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        
        self.label.setText(_translate("ChildrenFrom3", "对应录取的考生信息如下"))
        
    def FindStuInformation(self, str1):
        db=connectDB('127.0.0.1', 'hhlschema', 'HHL', '12345' )
        a, col, row=Alldataset("section", db, str1)
        db.close()
        
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setHorizontalHeaderLabels(['course_id','sec_id', 'semester','year', 'building','room_number', 'time_solt_id'])
        for i in range(row):
            for j in range(col):
                if j==3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(repr(int(a[i][j]))))
                    
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(a[i][j]))
        self.tableWidget.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    palette=QPalette()
    palette.setColor(QPalette.Background, QColor(202, 216, 235))
    ChildrenFrom3 = QtWidgets.QWidget()
    ChildrenFrom3.setPalette(palette)
    ui = Ui_ChildrenFrom3()
    ui.setupUi(ChildrenFrom3)
    ChildrenFrom3.show()
    sys.exit(app.exec_())

