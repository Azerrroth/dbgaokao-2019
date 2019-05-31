from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from HuifuCover import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from Ui_CentralTest2 import *


from PyQt5.QtWidgets import*


def connectDB(HostName, DbName, UserName, PassWord):
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL','qt_sql_default_connection')
    db.setHostName(HostName)
    db.setDatabaseName(DbName)
    db.setUserName(UserName)
    db.setPassword(PassWord)
    db.setPort(3306)  # 端口号
    db.open()
    return db


class Ui_sign(object):
    szhanghao = ""
    smima = ""
    szhucezh = ""
    szhucemm = ""
    sconfirmmm = ""
    sinvitednum = ""
    db = connectDB('youggls.top', 'test', 'abcdefg', '123456')

    def setupUi(self, sign):
        
        sign.setObjectName("sign")
        sign.resize(1000, 500)
        
        self.centralwidget = QtWidgets.QWidget(sign)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
        "border-image: url(C:/Users/黄翰林/Desktop/数据库大作业/前端制作/GaoKao/images/gaokao.jpg);}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.signsystem = QtWidgets.QTabWidget(self.centralwidget)
        self.signsystem.setTabPosition(QtWidgets.QTabWidget.North)
        self.signsystem.setObjectName("signsystem")
        self.denglu = QtWidgets.QWidget()
        self.denglu.setObjectName("denglu")
        self.label = QtWidgets.QLabel(self.denglu)
        self.label.setGeometry(QtCore.QRect(310, 80, 60, 30))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.denglu)
        self.label_2.setGeometry(QtCore.QRect(310, 140, 60, 30))
        self.label_2.setObjectName("label_2")
        
        ##添加标题
        self.label_x = QtWidgets.QLabel(self.denglu)
        self.label_x.setGeometry(QtCore.QRect(400, 20, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)


        self.label_x.setFont(font)
        self.label_x.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label_x.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x.setObjectName("label")
        
        self.zhanghao = QtWidgets.QLineEdit(self.denglu)
        self.zhanghao.setGeometry(QtCore.QRect(400, 80, 171, 40))
        self.zhanghao.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.zhanghao.setObjectName("zhanghao")
        self.mima = QtWidgets.QLineEdit(self.denglu)
        self.mima.setGeometry(QtCore.QRect(400, 130, 171, 40))
        self.mima.setInputMask("")
        self.mima.setText("")
        self.mima.setMaxLength(18)
        self.mima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mima.setObjectName("mima")

        self.buttonBox = QtWidgets.QPushButton(self.denglu)
        self.buttonBox.setGeometry(QtCore.QRect(350, 230, 90, 28))
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setStyleSheet('''background-color:QColor(192,192,192);''')

        self.buttonBox_q1 = QtWidgets.QPushButton(self.denglu)
        self.buttonBox_q1.setGeometry(QtCore.QRect(500, 230, 90, 28))
        self.buttonBox_q1.setObjectName("buttonBox_q1")
        self.buttonBox_q1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox_q1.setStyleSheet('''background-color:QColor(192,192,192);''')


        self.signsystem.addTab(self.denglu, "")
        self.zhuce = QtWidgets.QWidget()
        self.zhuce.setObjectName("zhuce")
        self.zhucezhanghao = QtWidgets.QLineEdit(self.zhuce)
        self.zhucezhanghao.setGeometry(QtCore.QRect(400, 40, 171, 40))
        self.zhucezhanghao.setObjectName("zhucezhanghao")
        self.zhucemima = QtWidgets.QLineEdit(self.zhuce)
        self.zhucemima.setGeometry(QtCore.QRect(400, 100, 171, 40))
        self.zhucemima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.zhucemima.setObjectName("zhucemima")
        self.querenmima = QtWidgets.QLineEdit(self.zhuce)
        self.querenmima.setGeometry(QtCore.QRect(400, 160, 171, 40))
        self.querenmima.setEchoMode(QtWidgets.QLineEdit.Password)
        self.querenmima.setObjectName("querenmima")
        self.label_3 = QtWidgets.QLabel(self.zhuce)
        self.label_3.setGeometry(QtCore.QRect(300, 40, 100, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.zhuce)
        self.label_4.setGeometry(QtCore.QRect(300, 100, 100, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.zhuce)
        self.label_5.setGeometry(QtCore.QRect(300, 160, 100, 30))
        self.label_5.setObjectName("label_5")

        self.buttonBox2 = QtWidgets.QPushButton(self.zhuce)
        self.buttonBox2.setGeometry(QtCore.QRect(350, 300, 90, 28))
        self.buttonBox2.setObjectName("buttonBox2")
        self.buttonBox2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox2.setStyleSheet('''background-color:QColor(192,192,192);''')


        self.buttonBox_q2 = QtWidgets.QPushButton(self.zhuce)
        self.buttonBox_q2.setGeometry(QtCore.QRect(500, 300, 90, 28))
        self.buttonBox_q2.setObjectName("buttonBox_q2")
        self.buttonBox_q2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox_q2.setStyleSheet('''background-color:QColor(192,192,192);''')


        self.label_6 = QtWidgets.QLabel(self.zhuce)
        self.label_6.setGeometry(QtCore.QRect(300, 220, 100, 30))
        self.label_6.setObjectName("label_6")
        self.yaoqingma = QtWidgets.QLineEdit(self.zhuce)
        self.yaoqingma.setGeometry(QtCore.QRect(400, 220, 171, 40))
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

        self.buttonBox_q1.clicked.connect(self.Stop)
        self.buttonBox_q2.clicked.connect(self.Stop)

        self.buttonBox.clicked.connect(self.accountinfo)
        self.buttonBox2.clicked.connect(self.newaccountinfo)
        QtCore.QMetaObject.connectSlotsByName(sign)

    def Stop(self):
        sys.exit(0)
    def accountinfo(self):
        self.szhanghao = self.zhanghao.text()
        self.smima = self.mima.text()
        print(self.szhanghao+self.smima)
        query = QtSql.QSqlQuery(self.db)
        query.prepare("select * from Account where username='%s' and pwd='%s'" % (self.szhanghao, self.smima))
        if query.exec():
            if query.size()!=0:
                print("连接成功")
                cl = Children()
                cl.KaoshengName=self.szhanghao
                #添加图片
#                palette=QPalette()
#                palette.setBrush(QPalette.Background, QBrush(QPixmap("C:/Users/黄翰林/Desktop/数据库大作业/前端制作/GaoKao/images/gaokao.jpg")))
#                cl.setPalette(palette)
#                palette=QPalette()
#                palette.setBrush(QPalette.Background, QBrush(QPixmap("./images/gaokao.jpg")))
#                cl.setPalette(palette)
                palette = QPalette()
                palette.setColor(QPalette.Background, QColor(202, 216, 235))
                cl.setPalette(palette)
                #cl.setStyleSheet("QWidget#cl{\n"
        #"border-image: url(C:/Users/黄翰林/Desktop/数据库大作业/前端制作/GaoKao/images/gaokao.jpg);}")
                cl.show()
            else:
                QMessageBox.about(sign, "提示", "账号或密码错误")
                print("账号或密码错误")
        else:
            print("连接失败")

    def newaccountinfo(self):
        self.szhucezh = self.zhucezhanghao.text()
        self.szhucemm = self.zhucemima.text()
        self.sconfirmmm = self.querenmima.text()
        self.sinvitednum = self.yaoqingma.text()
        query = QtSql.QSqlQuery(self.db)
        query.prepare("select * from Account where username='%s'" % (self.szhucezh))
        query1 = QtSql.QSqlQuery(self.db)
        query1.prepare("select * from InvitedList where InvitedList.key='%s'" % (self.sinvitednum))
        if len(self.szhucezh) == 0:
            print("账号为空")
        else:
            query.exec()
            if query.size() != 0:
                QMessageBox.about(sign, "提示", "账号已存在")
                print("账号已存在")
            elif self.szhucemm != self.sconfirmmm:
                QMessageBox.about(sign, "提示", "密码不一致")
                print("密码不一致")
            elif len(self.szhucemm) == 0:
                QMessageBox.about(sign, "提示", "密码为空")
                print("密码为空")
            elif len(self.sinvitednum) == 0:
                QMessageBox.about(sign, "提示", "验证码为空")
                print("验证码为空")
            else:
                query1.exec()
                if query1.size() == 0:
                    QMessageBox.about(sign, "提示", "邀请码无效")
                    print("邀请码无效")
                else:
                    a = ""
                    b = 0
                    while (query1.next()):
                        a = query1.value(0)
                        b = query1.value(1)
                    if (b == 0):
                        QMessageBox.about(sign, "提示", "邀请码失效")
                        print("邀请码失效")
                    else:
                        print(a, b)
                        query.prepare("insert into Account values('%s','%s','%s')" % (
                        self.szhucezh, self.szhucemm, self.sinvitednum))
                        query.exec()
                        query.prepare("update InvitedList set number=%d where InvitedListist.key='%s'" % (b - 1, a))
                        query.exec()
                        QMessageBox.about(sign, "提示", "注册成功")
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
        
        self.label_x.setText(_translate("sign", "高考帮"))
        
        self.signsystem.setTabText(self.signsystem.indexOf(self.denglu), _translate("sign", "登录"))
        self.label_3.setText(_translate("sign", "账号"))
        self.label_4.setText(_translate("sign", "密码"))
        self.label_5.setText(_translate("sign", "确认密码"))
        self.label_6.setText(_translate("sign", "邀请码"))
        self.signsystem.setTabText(self.signsystem.indexOf(self.zhuce), _translate("sign", "注册"))

class Children(QWidget, Ui_Form):
    def __init__(self):
        super(Children, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    sign = QtWidgets.QMainWindow()
    ui = Ui_sign()
    ui.setupUi(sign)
    sign.show()
    sys.exit(app.exec_())
