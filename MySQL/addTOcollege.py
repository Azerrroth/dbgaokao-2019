import pymysql

cont = pymysql.connect(host='youggls.top',
                       user='abcdefg', password='123456', database='test', charset='utf8')
cur = cont.cursor()
with open('test.txt', 'r')as fff:
    data = fff.readlines()
    for i in data:
        a = i.split(',')
        a[1]=a[1].replace("\n","")
        cur.execute("""INSERT INTO college (idcollege, name) 
                SELECT   '{}','{}'
                from DUAL  
                where not exists(select idcollege from college where name='{}'); 
                """.format(a[0], a[1], a[1]))
        print(i+"\n")
cont.commit()
cont.close()