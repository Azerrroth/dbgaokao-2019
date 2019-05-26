# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\黄翰林\Desktop\数据库大作业\前端制作\GaoKao\CentralTest2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import(QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtWidgets import*
from functools import partial
from ConnectDB import*

class Ui_Formson(object):
    def setupUi(self, FormsonIn):
        FormsonIn.setObjectName("FormsonIn")
        FormsonIn.resize(800, 600)
        self.tableWidget = QtWidgets.QTableWidget(FormsonIn)
        self.tableWidget.setGeometry(QtCore.QRect(70, 30, 500, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.OperateDB()

        self.retranslateUi(FormsonIn)
        QtCore.QMetaObject.connectSlotsByName(FormsonIn)

    def retranslateUi(self, FormsonIn):
        _translate = QtCore.QCoreApplication.translate
        FormsonIn.setWindowTitle(_translate("FormsonIn", "Form"))
    
    def OperateDB(self):
        db=connectDB('127.0.0.1', 'hhlschema', 'HHL', '12345' )
        a, col, row=datasetNew1("new_table2", db, "100")
        db.close()
        self.tableWidget.setColumnCount(col+1)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'name',  'delete'])
        for i in range(row):
            for j in range(col+1):
                if j==col:
                    searchBtn=QPushButton("X")
                    searchBtn.setObjectName("pushButtonx")
                    searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    searchBtn.setStyleSheet('''background-color:QColor(192,192,192);''')
                    searchBtn.clicked.connect(partial(self.Deldata, a[i][0]))
                    self.tableWidget.setCellWidget(i, j, searchBtn)
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(a[i][j])))
    
    #添加确定删除
    def Deldata(self, value):
        reply = QMessageBox.question(self ,"警告", "确定删除吗？", QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
        print(reply)
        if reply==16384:
            self.tableWidget.setHidden(True)
            db=connectDB('127.0.0.1', 'hhlschema', 'HHL', '12345' )
            query=QtSql.QSqlQuery(db)
            query.prepare("delete from %s where  ID='%d' "%("new_table2", value))
            if(query.exec()):
                db.close()
                self.OperateDB()
                self.tableWidget.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormsonIn = QtWidgets.QWidget()
    ui = Ui_Formson()
    ui.setupUi(FormsonIn)
    FormsonIn.show()
    sys.exit(app.exec_())

