# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\eric\zhuce.ui'
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
class Ui_sign(object):
    szhanghao=""
    smima=""
    szhucezh=""
    szhucemm=""
    sconfirmmm=""
    sinvitednum=""
    db=connectDB('127.0.0.1', 'test', 'newuser', 'qwerty123456')
    def setupUi(self, sign):
        sign.setObjectName("sign")
        sign.resize(818, 581)
        self.centralwidget = QtWidgets.QWidget(sign)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signsystem = QtWidgets.QTabWidget(self.centralwidget)
        self.signsystem.setTabPosition(QtWidgets.QTabWidget.North)
        self.signsystem.setObjectName("signsystem")
        self.denglu = QtWidgets.QWidget()
        self.denglu.setObjectName("denglu")
        self.label = QtWidgets.QLabel(self.denglu)
        self.label.setGeometry(QtCore.QRect(160, 80, 30, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.denglu)
        self.label_2.setGeometry(QtCore.QRect(160, 130, 30, 16))
        self.label_2.setObjectName("label_2")
        self.zhanghao = QtWidgets.QLineEdit(self.denglu)
        self.zhanghao.setGeometry(QtCore.QRect(230, 80, 171, 21))
        self.zhanghao.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.zhanghao.setObjectName("zhanghao")
        self.mima = QtWidgets.QLineEdit(self.denglu)
        self.mima.setGeometry(QtCore.QRect(230, 130, 171, 21))
        self.mima.setInputMask("")
        self.mima.setText("")
        self.mima.setMaxLength(18)
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setObjectName("mima")
        
        self.buttonBox = QtWidgets.QPushButton(self.denglu)
        self.buttonBox.setGeometry(QtCore.QRect(180, 230, 193, 28))
        self.buttonBox.setObjectName("buttonBox")
        
        self.buttonBox_q1 = QtWidgets.QPushButton(self.denglu)
        self.buttonBox_q1.setGeometry(QtCore.QRect(500, 230, 193, 28))
        self.buttonBox_q1.setObjectName("buttonBox_q1")
        
        self.signsystem.addTab(self.denglu, "")
        self.zhuce = QtWidgets.QWidget()
        self.zhuce.setObjectName("zhuce")
        self.zhucezhanghao = QtWidgets.QLineEdit(self.zhuce)
        self.zhucezhanghao.setGeometry(QtCore.QRect(290, 40, 171, 21))
        self.zhucezhanghao.setObjectName("zhucezhanghao")
        self.zhucemima = QtWidgets.QLineEdit(self.zhuce)
        self.zhucemima.setGeometry(QtCore.QRect(290, 100, 171, 21))
        self.zhucemima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.zhucemima.setObjectName("zhucemima")
        self.querenmima = QtWidgets.QLineEdit(self.zhuce)
        self.querenmima.setGeometry(QtCore.QRect(290, 160, 171, 21))
        self.querenmima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.querenmima.setObjectName("querenmima")
        self.label_3 = QtWidgets.QLabel(self.zhuce)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 31, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.zhuce)
        self.label_4.setGeometry(QtCore.QRect(210, 100, 30, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.zhuce)
        self.label_5.setGeometry(QtCore.QRect(200, 160, 60, 16))
        self.label_5.setObjectName("label_5")
        
        
        self.buttonBox2 = QtWidgets.QPushButton(self.zhuce)
        self.buttonBox2.setGeometry(QtCore.QRect(230, 270, 193, 28))
        self.buttonBox2.setObjectName("buttonBox2")
        
        self.buttonBox_q2 = QtWidgets.QPushButton(self.zhuce)
        self.buttonBox_q2.setGeometry(QtCore.QRect(500, 270, 193, 28))
        self.buttonBox_q2.setObjectName("buttonBox_q2")
        
        self.label_6 = QtWidgets.QLabel(self.zhuce)
        self.label_6.setGeometry(QtCore.QRect(200, 220, 72, 15))
        self.label_6.setObjectName("label_6")
        self.yaoqingma = QtWidgets.QLineEdit(self.zhuce)
        self.yaoqingma.setGeometry(QtCore.QRect(292, 220, 171, 21))
        self.yaoqingma.setObjectName("yaoqingma")
        self.signsystem.addTab(self.zhuce, "")
        self.horizontalLayout.addWidget(self.signsystem)
        sign.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(sign)
        self.statusbar.setObjectName("statusbar")
        sign.setStatusBar(self.statusbar)

        ####self.zhanghao
        
        self.retranslateUi(sign)
        self.signsystem.setCurrentIndex(0)
        
        
        self.buttonBox.clicked.connect( self.accountinfo)
        self.buttonBox2.clicked.connect(self.newaccountinfo)
        QtCore.QMetaObject.connectSlotsByName(sign)
    
       
    def accountinfo(self):
        self.szhanghao=self.zhanghao.text()
        self.smima=self.mima.text()
        query=QtSql.QSqlQuery(self.db)
        query.prepare("select * from account where username='%s' and pwd='%s'"%(self.szhanghao, self.smima) )
        if query.exec() and query.size()!=0:
            print("连接成功")
        else:
            print("账号或密码错误")
    def newaccountinfo(self):
        self.szhucezh=self.zhucezhanghao.text()
        self.szhucemm=self.zhucemima.text()
        self.sconfirmmm=self.querenmima.text()
        self. sinvitednum=self.yaoqingma.text()
        query=QtSql.QSqlQuery(self.db)
        query.prepare("select * from account where username='%s'"%(self.szhucezh))
        query1=QtSql.QSqlQuery(self.db)
        query1.prepare("select * from invitedlist where invitedlist.key='%s'"%(self.sinvitednum))
        if len(self.szhucezh)==0:
                print("账号为空")
        else:
            query.exec()
            if query.size()!=0:
                print("账号已存在")
            elif  self.szhucemm!=self.sconfirmmm:
                print("密码不一致")
            elif len(self.szhucemm)==0:
                print("密码为空")
            elif len(self.sinvitednum)==0:
                print("验证码为空")
            else:
                 query1.exec()
                 if query1.size()==0:
                    print("邀请码无效")
                 else:
                    a=""
                    b=0
                    while(query1.next()): 
                            a=query1.value(0)
                            b=query1.value(1)
                    if(b==0):
                        print("邀请码失效")
                    else:
                        print(a, b)
                        query.prepare("insert into account values('%s','%s','%s')"%(self.szhucezh, self.szhucemm, self.sinvitednum))
                        query.exec()
                        query.prepare("update invitedlist set number=%d where invitedlist.key='%s'"%(b-1, a))
                        query.exec()
                        print("注册成功")
                        
    def retranslateUi(self, sign):
        _translate = QtCore.QCoreApplication.translate
        sign.setWindowTitle(_translate("sign", "MainWindow"))
        self.buttonBox.setText(_translate("sign", "确认"))
        self.buttonBox2.setText(_translate("sign", "确认"))
        self.buttonBox_q1.setText(_translate("sign", "取消"))
        self.buttonBox_q2.setText(_translate("sign", "取消"))
        self.label.setText(_translate("sign", "账号"))
        self.label_2.setText(_translate("sign", "密码"))
        self.signsystem.setTabText(self.signsystem.indexOf(self.denglu), _translate("sign", "登录"))
        self.label_3.setText(_translate("sign", "账号"))
        self.label_4.setText(_translate("sign", "密码"))
        self.label_5.setText(_translate("sign", "确认密码"))
        self.label_6.setText(_translate("sign", "邀请码"))
        self.signsystem.setTabText(self.signsystem.indexOf(self.zhuce), _translate("sign", "注册"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sign = QtWidgets.QMainWindow()
    ui = Ui_sign()
    ui.setupUi(sign)
    sign.show()
    sys.exit(app.exec_())
    ui.db.close()
