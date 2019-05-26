import pymysql

cont = pymysql.connect(host='youggls.top',
                       user='abcdefg', password='123456', database='test', charset='utf8')
cur = cont.cursor()
with open('person/test.txt', 'r') as pe:
    data = pe.readlines()
    for i in data:
        a = i.split(',')
        if a[19] == "\n":
            a[19] = "0"
        while (len(a) < 21):
            a.append("0")

        if a[20] == "\n" or a[20] == "":
            a[20] = "0"

        cur.execute("""insert into Candidate (idCandidate,Candidate_name,gender,minzu,status,CollegeID,CollegeName,
        zf1,addScore,tot_score,AdmissionLevel,zhuanye_ID,AdmitType,AdmitTime,
        Chinese,Math,CLiberal,CScience,ForeignLanguage,FLListen,FLSpeaking,type)
        SELECT '{}','{}','{}','{}','{}','{}','{}',{},'{}',{},'{}','{}','{}',
        (select str_to_date('{}', '%Y-%m-%d %H:%i:%s')),{},{},{},{},{},{},{},'普通文科'
        from DUAL 
        where not exists(select idCandidate from Candidate where idCandidate='{}');"""
                    .format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10], a[11], a[12], a[13],
                            a[14], a[15], a[16], a[17], a[18], a[19], a[20], a[0]))
        print(i, end="")
cur.close()
cont.commit()
cont.close()
