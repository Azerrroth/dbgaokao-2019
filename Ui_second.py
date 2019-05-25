# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eric\qtDesign\second.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
#连接到数据库
def connectDB(HostName,DbName, UserName, PassWord ):
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName(HostName)
    db.setDatabaseName(DbName)
    db.setUserName(UserName)
    db.setPassword(PassWord)
    db.setPort(3306) # 端口号
    db.open()
    return db
    
#返回某个表某一列的值的集合
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
        self.tableView.setGeometry(QtCore.QRect(340, 240, 256, 300))
        self.tableView.setFixedWidth(400)
        self.tableView.setObjectName("tableView")
        
        #默认隐藏表
        self.tableView.setHidden(True)
        #水平和垂直表头大小不可调整
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        #设置表格内容不可编辑和选中
        self.tableView.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(390, 120, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.s=self.comboBox.currentText()
        self.comboBox.addItems(self.l)
        
        #该信号槽使combobox内容可以动态更新以及表内容动态更新
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
        
    #动态获取comboBox选中的内容并使表内容更新
    def changetext(self, text):
        self.s=text
        self.tableView.setHidden(True)
        testModel =QtSql.QSqlTableModel() 
        #选中数据库
        testModel.setTable('Student')
        #表中内容由查询结果生成
        testModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        #筛选的条件
        testModel.setFilter("dept_name='%s'"%(self.s))
        #执行并插入到表中
        testModel.select()
        self.tableView.setModel(testModel)
        #隐藏某些列
        self.tableView.hideColumn(2)
        
    #关闭时断开数据库连接
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

