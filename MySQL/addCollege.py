# -*- coding: utf-8 -*-
import pymysql

cont = pymysql.connect(host='127.0.0.1',
                       user='HHL', password='12345', database='test', charset='utf8')
cur = cont.cursor()
with open('collegename/wenerben.txt', 'rb')as fff:  # change the file name in collegename
    data = fff.readlines()
    for i in data:
        a = i.split(', ')

        a[1] = a[1].replace("\n", "")
        cur.execute("""INSERT INTO college (idcollege, name)
            SELECT '{}', '{}'
            FROM dual WHERE NOT EXISTS (select * from college where college.idcollege = '{}');
                """.format(a[0], a[1], a[0]))
        print(i, end="")
cont.commit()
cont.close()
