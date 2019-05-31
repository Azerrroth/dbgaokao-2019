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
        ChildrenFrom3.resize(2000, 1000)
        self.tableWidget = QtWidgets.QTableWidget(ChildrenFrom3)
        self.tableWidget.setGeometry(QtCore.QRect(250, 150, 1400, 80))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(1)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['准考证号','姓名', '性别','民族', '考生状态','录取院校', '总分', '加分条件', '特征分'])
        
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive | QHeaderView.Stretch)
        
        self.tableWidget_2 = QtWidgets.QTableWidget(ChildrenFrom3)
        self.tableWidget_2.setGeometry(QtCore.QRect(600, 400, 800, 80))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.setHorizontalHeaderLabels(['录取层次','录取院校','录取专业', '录取方式','录取时间'])
        
        
        self.tableWidget_3 = QtWidgets.QTableWidget(ChildrenFrom3)
        self.tableWidget_3.setGeometry(QtCore.QRect(250, 650, 1400, 80))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(9)
        self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.setHorizontalHeaderLabels(['科目','语文', '数学','综合', '外语','外语听力', '外语口语', '总分一', '总分'])
        
        
        self.label = QtWidgets.QLabel(ChildrenFrom3)
        self.label.setGeometry(QtCore.QRect(750, 40, 500, 80))
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
        db=connectDB('youggls.top', 'test', 'abcdefg', '123456')
        a, col, row=Alldataset( db, str1)
        #db.close()
        self.tableWidget.setItem(0, 0, QTableWidgetItem(a[0][0]))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(a[0][1]))
        self.tableWidget.setItem(0, 2, QTableWidgetItem(a[0][2]))
        self.tableWidget.setItem(0, 3, QTableWidgetItem(a[0][3]))
        self.tableWidget.setItem(0, 4, QTableWidgetItem(a[0][4]))
        self.tableWidget.setItem(0, 5, QTableWidgetItem(a[0][6]))
        self.tableWidget.setItem(0, 6, QTableWidgetItem(str(a[0][7])))
        self.tableWidget.setItem(0, 7, QTableWidgetItem(a[0][8]))
        self.tableWidget.setItem(0, 8, QTableWidgetItem(str(a[0][9])))
        
        self.tableWidget_2.setItem(0, 0, QTableWidgetItem(a[0][10]))
        self.tableWidget_2.setItem(0, 1, QTableWidgetItem(a[0][5]))
        self.tableWidget_2.setItem(0, 2, QTableWidgetItem(a[0][11]))
        self.tableWidget_2.setItem(0, 3, QTableWidgetItem(a[0][12])) 
        self.tableWidget_2.setItem(0, 4, QTableWidgetItem("2018-7-15 09:12:03"))
        
        self.tableWidget_3.setItem(0, 0, QTableWidgetItem("成绩"))
        self.tableWidget_3.setItem(0, 1, QTableWidgetItem(str(a[0][14])))
        self.tableWidget_3.setItem(0, 2, QTableWidgetItem(str(a[0][15])))
        self.tableWidget_3.setItem(0, 3, QTableWidgetItem(str(a[0][16])))
        self.tableWidget_3.setItem(0, 4, QTableWidgetItem(str(a[0][18])))
        self.tableWidget_3.setItem(0, 5, QTableWidgetItem(str(a[0][19])))
        self.tableWidget_3.setItem(0, 6, QTableWidgetItem(str(a[0][20])))
        self.tableWidget_3.setItem(0, 7, QTableWidgetItem(str(a[0][7])))
        self.tableWidget_3.setItem(0, 8, QTableWidgetItem(str(a[0][9])))
        self.tableWidget.show()
        self.tableWidget_2.show()
        self.tableWidget_3.show()
        


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

