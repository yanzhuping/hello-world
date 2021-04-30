import pymysql

def link_mysql():
    db = pymysql.Connect(
        host='rm-uf6346k4i25q6cyhxyo.mysql.rds.aliyuncs.com', port=3306, user='iortho_uat',
        passwd='vllwtqZziYx6QPo9', db='zmc_uat', charset='utf8')
    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()
    sql = "select * from zmc_vote where zmcCode='259b96ef-929f-11eb-b42c-00163e183747' and isDelete=0 and authKey='18017870857'"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    if result == ():
        print("fff")
        pass
    else:
        print("dadad")
        sql1 = "update zmc_vote set isDelete=1 where zmcCode='259b96ef-929f-11eb-b42c-00163e183747' and isDelete=0 and authKey='18017870857'"
        cursor.execute(sql1)
        db.commit()
    db.close()

link_mysql()