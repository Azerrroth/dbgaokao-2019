import pymysql

cont = pymysql.connect(host='youggls.top',
                       user='abcdefg', password='123456', database='test', charset='utf8')
cur = cont.cursor()
with open('collegename/wenerben.txt', 'r')as fff:  # change the file name in collegename
    data = fff.readlines()
    for i in data:
        a = i.split(',')
        a[1] = a[1].replace("\n", "")
        cur.execute("""INSERT INTO college (idcollege, name)
            SELECT '{}', '{}'
            FROM dual WHERE NOT EXISTS (select * from college where college.idcollege = '{}');
                """.format(a[0], a[1], a[0]))
        print(i, end="")
cont.commit()
cont.close()
