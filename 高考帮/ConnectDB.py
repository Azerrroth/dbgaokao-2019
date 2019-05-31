from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
def connectDB(HostName,DbName, UserName, PassWord ):
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL', 'firstconnection')
    db.setHostName(HostName)
    db.setDatabaseName(DbName)
    db.setUserName(UserName)
    db.setPassword(PassWord)
    db.setPort(3306) # 端口号
    db.open()
    return db

def datasetNew1(db, username):
    query=QtSql.QSqlQuery(db)
    query.prepare("select*from StuFavor where UserName='%s'  "%(username))
    a=[]
    length=rows=0
    if(query.exec()):
        #print("good")
        length=len(query.record())
        rows=query.size()
        while(query.next()): 
            b=[]
            for i in range(len(query.record())):
                b.append(query.value(i))
            a.append(b)
        #print(length)
    #print(a)
    return a, length, rows


def Alldataset(db, str):
    query=QtSql.QSqlQuery(db)
    query.prepare("select * FROM Candidate where idCandidate='%s' "%( str))
    a=[]
    length=rows=0
    if(query.exec()):
        #print("good")
        length=len(query.record())
        rows=query.size()
        while(query.next()): 
            b=[]
            for i in range(len(query.record())):
                b.append(query.value(i))
            a.append(b)
        #print(length)
    #print(a)
    return a, length, rows

    
def dataset1(db,ke, xiao, lei, zhuan):
    query=QtSql.QSqlQuery(db)
    query.prepare("""select idCandidate,Candidate_name,tot_score,AdmitType,Admittime
from Candidate  join zhuanye on Candidate.zhuanye_ID=zhuanye.ID 
and Candidate.CollegeID=zhuanye.college_id
where AdmissionLevel='%s' and CollegeName='%s' and Candidate.type='%s' 
and MajorName='%s' """%(ke, xiao, lei, zhuan))
    a=[]
    length=rows=0
    if(query.exec()):
        #print("good")
        length=len(query.record())
        rows=query.size()
        while(query.next()): 
            b=[]
            for i in range(len(query.record())):
                b.append(query.value(i))
            a.append(b)
        #print(length)
    #print(a)
    return a, length, rows



def dataset3(db, str1, str2, str3):
    query=QtSql.QSqlQuery(db)
    sql="""select t.ID,t.MajorName,r.rank,t.ma,t.mi,t.c 
from (select zhuanye.ID,zhuanye.MajorName,max(tot_score) ma,min(tot_score) mi,count(*) c
from (Candidate  join zhuanye on Candidate.zhuanye_ID=zhuanye.ID 
and Candidate.CollegeID=zhuanye.college_id) 
where AdmissionLevel='%s' and CollegeName='%s' and Candidate.type='%s' group by zhuanye.MajorName)
as t join rankArt r on t.ma=score"""

    query.prepare("""select t.ID,t.MajorName,r.rank,t.ma,t.mi,t.c 
from (select zhuanye.ID,zhuanye.MajorName,max(tot_score) ma,min(tot_score) mi,count(*) c
from (Candidate  join zhuanye on Candidate.zhuanye_ID=zhuanye.ID 
and Candidate.CollegeID=zhuanye.college_id) 
where AdmissionLevel='%s' and CollegeName='%s' and Candidate.type='%s' group by zhuanye.MajorName)
as t join rankArt r on t.ma=score"""%(str1, str3, str2))
    a=[]
    length=rows=0
    if(query.exec()):
        #print("good")
        length=len(query.record())
        rows=query.size()
        while(query.next()): 
            b=[]
            for i in range(len(query.record())):
                b.append(query.value(i))
            a.append(b)
        #print(length)
    #print(a)
    return a, length, rows



def selectdistinct(col, table, db):
    query=QtSql.QSqlQuery(db)
    query.prepare("select distinct %s from %s"%(col, table))
    a=[]
    if(query.exec()):
       while(query.next()): 
         a.append(query.value(0))
    return a
    
    
    
class Ui_MainWindow(object):
    db=connectDB('youggls.top', 'test', 'abcdefg', '123456')
    
    #学院列表
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
        
        #self.s=self.comboBox.currentText()
        self.comboBox.activated[str].connect(self.changetext)
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)

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
        #print(self.s)
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
    #print(ui.s)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
