from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import sys
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
if __name__ == "__main__":
    db=connectDB('127.0.0.1', 'first_schemas', 'newuser', 'qwerty123456')
    #查询语句
    query=QtSql.QSqlQuery(db)
    query.prepare("select distinct dept_name from Student")
    a=[]
    if(query.exec()):
       while(query.next()): 
         a.append(query.value(0))
    a.sort()
    query.prepare("select * from Student where dept_name='%s'"%(a[0]))
    if(query.exec()):
        length=len(query.record())#获取列数，query.size()是行数
        while(query.next()):
          for i in range(length):
                print(query.value(i))

