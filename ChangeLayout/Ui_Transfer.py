# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\黄翰林\Desktop\数据库大作业\前端制作\GaoKao\Transfer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_CentralTest2 import Ui_Formson
from PyQt5.QtWidgets import QWidget
from ConnectDB import*
from functools import partial

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 1000)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 100, 111, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showCentralTest)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 100, 111, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(partial(self.Adddata, 1005, "hj", "100"))
        
        
        
        
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def Adddata(self, v1, v2, v3):
        print(str(v1)+v2+v3)
        db=connectDB('127.0.0.1', 'hhlschema', 'HHL', '12345' )
        query=QtSql.QSqlQuery(db)
        query.prepare("insert into %s values('%d','%s','%s') "%("new_table2", v1, v2, v3))
        if(query.exec()):
            db.close()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "查看收藏夹"))
        self.pushButton_2.setText(_translate("MainWindow", "添加到收藏夹"))
    
    def showCentralTest(self):
        #child= QtWidgets.QMainWindow()
        child = Children()
        #ui.setupUi(child)
        child.show()
class Children(QWidget, Ui_Formson):
     def __init__(self):
        super(Children, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

