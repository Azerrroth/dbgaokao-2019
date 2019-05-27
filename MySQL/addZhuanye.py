import pymysql

cont = pymysql.connect(host='youggls.top',
                       user='abcdefg', password='123456', database='test', charset='utf8')
cur = cont.cursor()
with open('zhuanye/wen1ans.txt') as f:
    data = f.readlines()
    for i in data:
        a = i.split(',')
        # a[1] = a[1].replace("\n", "")  #  notice to change 普通理科  普通文科
        cur.execute("""INSERT INTO zhuanye (college_id,ID, name,type) 
                SELECT   '{}','{}','{}','普通文科'
                from DUAL  
                where not exists(select college_id from zhuanye where college_id='{}'and ID='{}' and name='{}' and type = '普通文科'); 
                        """.format(a[0], a[1], a[2], a[0], a[1], a[2]))
        print(i, end="")
cont.commit()
cont.close()
