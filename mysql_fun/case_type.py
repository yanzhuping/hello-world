#通过输入消息类型查找对应的病例，以及该病例所在的主账号的账号、密码
from mysql_fun.fun_set import *
import requests
from time import sleep

def get_message(dc_env,dc_type,db_env=None,msg_type=None):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
    base_url = 'http://172.17.4.177:8087/func.php?'
    g_config = get_golobal_config(db_env)

    db = pymysql.Connect(host=g_config.get('host'), port=3306, user=g_config.get('mysqluser'),
                         passwd=g_config.get('mysqlpasswd'), db=g_config.get('dbname'), charset='utf8')

    cursor = db.cursor()

    sql = "select distinct crmUserCode from opm_statetidingsInitial where msgType='%s' order by actionDate desc limit 50" % msg_type
    cursor.execute(sql)
    usercode = cursor.fetchall()#这是获取医生编码
    print(usercode)

    for i in usercode:
        code=i[0]
        sql_1="select DISTINCT d.username,d.password from(((" \
              "opm_rbac_role a inner join opm_rbac_role_attribute b on a.roleId=b.roleId)" \
              "inner join opm_rbac_role_user_account c on b.roleId=c.roleId)" \
              "inner join opm_rbac_account d on c.accountId=d.accountId)" \
              "where b.doctorCode='%s'and a.rtId=1"%code   #通过医生编码查询用户名和密码
        cursor.execute(sql_1)
        try:
            msg=cursor.fetchone()
            print(msg)
            passwd=msg[1]
            username=msg[0]
            param_data = {'env': dc_env, 'type': dc_type, 'aes': 'de', 'str': passwd}
            r = requests.get(base_url + '/get', headers=header, params=param_data)
            print("account:"+username+"\n"+'passwd:' + r.text)
            sleep(1)
        except:
            print("可能未找到账号密码")
            pass

        sql_2="select name from opm_statetidingsInitial where crmUserCode='%s' and msgType='%s'"%(code,msg_type)
        cursor.execute(sql_2)
        patientname=cursor.fetchall()
        names = []
        for name in patientname:
            p_name=name[0]
            if p_name not in names:
                names.append(p_name)

        print("case：")
        print(names)
        print("\n"+"------------------------------------------------------------------")
    db.close()


if __name__ == '__main__':
    #输入环境以及消息类型(具体消息类型参考message_type），可得到对应该消息类型的病例以及病例所属的账号和密码
    # get_message('prod','iortho','sh_adv','c31')
    get_message('prod','comfos','bj_adv','a51')
    # get_message('sit','comfos','bj_sit','a7')
    # get_message('sit','iortho','sh_sit','c31')
