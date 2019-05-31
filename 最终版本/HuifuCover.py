# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\黄翰林\Desktop\数据库大作业\前端制作\GaoKao\cover.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import(QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtWidgets import*
from ConnectDB import*
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from functools import partial
from UseChild01 import*
from Ui_CentralTest2 import*
import locale
from xpinyin import Pinyin
def my_function(lis):             #输入一个名字的列表
        pin=Pinyin()
        result=[]
        for item in lis:
            result.append((pin.get_pinyin(item),item))
        result.sort()
        for i in range(len(result)):
            result[i]=result[i][1]
        return result
class Ui_Form(object):
   
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2000, 1000)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, -20, 800, 111))
        font = QtGui.QFont()
        font.setFamily("Adobe 宋体 Std L")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)


        self.label.setFont(font)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(600, 70, 800, 600))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        ##########添加的
        self.comboBox.addItem("")
        
        
     
        self.verticalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        #self.comboBox_2.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        #self.comboBox_3.addItem("")
        #self.comboBox_3.addItem("")
        #self.comboBox_3.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(900, 600, 100, 50))
        self.pushButton.setObjectName("pushButton")
        
        #self.tableView = QtWidgets.QTableView(Form)
        #self.tableView.setGeometry(QtCore.QRect(90, 190, 256, 192))
        #self.tableView.setObjectName("tableView")
        #self.tableView.setHidden(True)
        
        self.tableWidget = QtWidgets.QTableWidget(Form)
        ####更改
        self.tableWidget.setGeometry(QtCore.QRect(500, 400, 1000, 500))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHidden(True)
        
        #self.label_5 = QtWidgets.QLabel(Form)
        #self.label_5.setGeometry(QtCore.QRect(140, 210, 81, 41))
        #self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(900, 200, 200, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_2.setBuddy(self.comboBox)
        self.label_3.setBuddy(self.comboBox_2)
        self.label_4.setBuddy(self.comboBox_3)


        ###########更改：添加收藏夹
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(900, 70, 111, 41))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton")
        self.pushButton_4.clicked.connect(partial(self.showCentralTest, self.KaoshengName, self.s3))

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(900, 120, 111, 41))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setObjectName("pushButton_2")
        self.pushButton_5.clicked.connect(self.Adddata)
        
        self.pushButton_4.setHidden(True)
        self.pushButton_5.setHidden(True)
        self.pushButton.setHidden(True)





        
        self.comboBox.activated[str].connect(self.Changetext1)
        self.comboBox_2.activated[str].connect(self.Changetext2)
        self.comboBox_3.activated[str].connect(self.Changetext3)

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(self.tableWidget.show)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    
    s1=""
    s2=""
    s3=""
    KaoshengName=""
    max=0
    min=10000
    minrank=1
    countper=0
    def Changetext1(self, text):
        self.s1=text
        self.Choose()
    def Changetext2(self, text):
        self.s2=text
        self.Choose()
    def Changetext3(self, text):
        self.s3=text
        self.Choose()
        
        #print(self.s1+self.s2+self.s3)
    def Choose(self):
        if len(self.s1)*len(self.s2)*len(self.s3)>0:
            db=connectDB('youggls.top', 'test', 'abcdefg', '123456' )
            a, col, row=dataset3(db, self.s1, self.s2, self.s3)
            print(a)
            #db.close()

            
            self.tableWidget.setColumnCount(col)
            self.tableWidget.setRowCount(row+1)
            self.tableWidget.setHorizontalHeaderLabels(['专业代号', '专业名称', '录取最低位次', '最高分','最低分', '录取人数'])

            for i in range(row):
                self.countper+=a[i][5]
                for j in range(col):
                    if i<row:
                        if j==0:
                            searchBtn = QPushButton(a[i][j])
                            searchBtn.setObjectName("pushButtonx")
                            searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                            searchBtn.setStyleSheet('''background-color:QColor(202,235,216);''')
                            searchBtn.clicked.connect(partial(self.showSon, a[i][j], a[i][j+1]))
                            self.tableWidget.setCellWidget(i, j, searchBtn)
                        else:
                            self.tableWidget.setItem(i, j, QTableWidgetItem(str(a[i][j])))
                            if j==3:
                                if self.max<a[i][j]:
                                    self.max=a[i][j]
                            if j==4:
                                if self.min>a[i][j]:
                                    self.min=a[i][j]
                            if j==2:
                                if self.minrank<a[i][j]:
                                    self.minrank=a[i][j]
            #################大改革
            if row>0:
                searchBtn = QPushButton("查看收藏夹")
                searchBtn.setObjectName("pushButtonx")
                searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                searchBtn.setStyleSheet('''background-color:QColor(153,51,250);''')
                searchBtn.clicked.connect(partial(partial(self.showCentralTest, self.KaoshengName, self.s3)))
                self.tableWidget.setCellWidget(row, 0, searchBtn)
                
                
                searchBtn1 = QPushButton("添加到收藏")
                searchBtn1.setObjectName("pushButtonx")
                searchBtn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                searchBtn1.setStyleSheet('''background-color:QColor(153,51,250);''')
                searchBtn1.clicked.connect(self.Adddata)
                self.tableWidget.setCellWidget(row, 1, searchBtn1)
                
                
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(self.minrank)))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(str(self.max)))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(str(self.min)))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(self.countper)))
                self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    # 更改,可传递参数
    # 更改文本信息
    def showSon(self, text, s4):
        self.child = ChildrenForm()
        print(self.s1 + self.s2 + self.s3)
        self.child.ChangeText(self.s1, self.s2, self.s3, s4)
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(202, 216, 235))
        self.child.setPalette(palette)

        self.child.SearchStudent(self.s1, self.s3, self.s2, s4)
        self.child.show()
        print(text)
                        
            
           
        
    
        
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FirstForm"))
        self.label.setText(_translate("Form", "2018年内蒙古普通高校招生批量投档录取最高分最低分数查询"))
        self.label_2.setText(_translate("Form", "批次: "))
        self.label_3.setText(_translate("Form", "科类:  "))
        self.label_4.setText(_translate("Form", "院校:  "))
        
        #self.comboBox.setItemText(0, _translate("Form", "本科提前批"))
        #self.comboBox.setItemText(1, _translate("Form", "本科一批"))
        #self.comboBox.setItemText(2, _translate("Form", "本科二批"))
        #self.comboBox.setItemText(3, _translate("Form", "高职高专"))
        #list1=self.Getlist("course_id")
        ###################更改
        self.comboBox.addItems(["本科提前A", "本科提前B","本科一批", "本科二批"])
        #self.comboBox.addItem("本科提前批")
        #self.comboBox.addItem("本科一批")
        #self.comboBox.addItem("本科二批")
        #self.comboBox.addItem("高职高专")
        
        #self.comboBox_2.setItemText(0, _translate("Form", "文科"))
        #self.comboBox_2.setItemText(1, _translate("Form", "理科"))
        self.comboBox_2.addItems(["普通文科", "普通理科"])
        #self.comboBox_2.addItem("文科")
        #self.comboBox_2.addItem("理科")
        
        #self.comboBox_3.setItemText(0, _translate("Form", "南开大学"))
        #self.comboBox_3.setItemText(1, _translate("Form", "清华大学"))
        #self.comboBox_3.setItemText(2, _translate("Form", "北京大学"))
        #self.comboBox_3.setItemText(3, _translate("Form", "中国科学院大学"))
        self.comboBox_3.addItems(self.Getlist1("CollegeName"))
        #self.comboBox_3.addItems(['清华大学', '中国科学院'])
        #self.comboBox_3.setItemText( _translate("Form", "清华大学"))
        #self.comboBox_3.addItem("中华人民共和国大学纽约分校")
        # self.comboBox.setHidden(True)
        # self.comboBox_2.setHidden(True)
        # self.comboBox_3.setHidden(True)

        self.pushButton_4.setText(_translate("Form", "查看收藏夹"))
        self.pushButton_5.setText(_translate("Form", "添加到收藏夹"))
        self.pushButton.setText(_translate("Form", "专业信息"))
        #self.label_5.setText(_translate("Form", "好一点"))
        self.pushButton_3.setText(_translate("Form", "提交"))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet('''background-color:QColor(192,192,192);''')
        self.pushButton_2.setText(_translate("Form", "重置"))
        self.pushButton_2.clicked.connect(self.Clear)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet('''background-color:QColor(192,192,192);''')

    def Clear(self):
        self.tableWidget.setHidden(True)
        self.tableWidget.clear()
#        self.s1=""
#        self.s3=""
#        self.s2=""
        self.max=0
        self.min=10000
        self.minrank=1
        self.countper=0
    
    def Getlist1(self, str):
        db=connectDB('youggls.top', 'test', 'abcdefg', '123456' )
        list1=selectdistinct(str, "college", db)
        print("显示大学")
        #print(list1)
     
        #print(list1.sort())
        #print(len(list))
        #db.close()
        list2=my_function(list1)
        print(list2)
        return list2
    
    def Getlist(self, str):
        db=connectDB('youggls.top', 'test', 'abcdefg', '123456' )
        list1=selectdistinct(str, "college", db)
        print("显示大学")
        #print(len(list1))
        #list1.sort()
        #print(list1.sort())
        #print(len(list))
        #db.close()
        list2=my_function(list1)
        print(list2)
        return list2
        
    

    ######更改
    def Adddata(self):
        
        
        print(self.KaoshengName)
        print(self.s3)
        print(self.max)
        print(self.min)
        print(self.minrank)
        print(self.countper)
        ##添加成功
        QMessageBox.about(self,  "提示", "添加成功！")
        #print(str(v1) + v2 + v3)
        db = connectDB('youggls.top', 'test', 'abcdefg', '123456')
        query = QtSql.QSqlQuery(db)
        #query.prepare("insert into StuFavor values ")
        query.prepare("insert into StuFavor values('%s','%s',%d,%d,%d,%d) " % (self.KaoshengName, self.s3, self.max, self.min, self.minrank, self.countper))
        if (query.exec()):
            #db.close()
            print("ok")

    def showCentralTest(self, username, collegename):
        # child= QtWidgets.QMainWindow()
        child = Children()
        #child.username11=username
        #child.collegename11=collegename
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(202, 216, 235))
        child.setPalette(palette)
        child.OperateDB(self.KaoshengName)
        # ui.setupUi(child)
        child.show()


class Children(QWidget, Ui_Formson):
    def __init__(self):
        super(Children, self).__init__()
        self.setupUi(self)
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    palette=QPalette()
    palette.setColor(QPalette.Background, QColor(202, 216, 235))
    Form.setPalette(palette)
    ui = Ui_Form()
    #print(ui.s1+ui.s2+ui.s3)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

