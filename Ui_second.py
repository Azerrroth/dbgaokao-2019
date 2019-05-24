# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eric\qtDesign\second.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
def connectDB(HostName,DbName, UserName, PassWord ):
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName(HostName)
    db.setDatabaseName(DbName)
    db.setUserName(UserName)
    db.setPassword(PassWord)
    db.setPort(3306) # 端口号
    db.open()
    return db

def selectdistinct(col, table, db):
    query=QtSql.QSqlQuery(db)
    query.prepare("select distinct %s from %s"%(col, table))
    a=[]
    if(query.exec()):
       while(query.next()): 
         a.append(query.value(0))
    return a
class Ui_MainWindow(object):
    db=connectDB('127.0.0.1', 'first_schemas', 'newuser', 'qwerty123456')
    l=selectdistinct('dept_name', 'Student', db)
    s=""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(340, 240, 256, 192))
        self.tableView.setObjectName("tableView")
        
        self.tableView.setHidden(True)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 120, 87, 22))
        self.comboBox.setObjectName("comboBox")
        
        
        self.comboBox.addItems(self.l)
        
        self.s=self.comboBox.currentText()
        self.comboBox.activated[str].connect(self.changetext)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.tableView.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "提交"))
        
    #动态获取comboBox选中的内容
    def changetext(self, text):
        self.s=text
        testModel =QtSql.QSqlTableModel()
        self.tableView.setHidden(True)
        testModel.setTable('Student')
        testModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        testModel.setFilter("dept_name='%s'"%(self.s))
        testModel.select()
        self.tableView.setModel(testModel)
         
    def closerevent(self, event):
        self.db.close()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

