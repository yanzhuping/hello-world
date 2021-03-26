from crm_style.function import *
import requests
from time import sleep

def get_message(dc_env,dc_type,db_env=None,tel=None):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
    base_url = 'http://172.17.4.177:8087/func.php?'
    g_config = get_golobal_config(db_env)

    db = pymysql.Connect(host=g_config.get('host'), port=3306, user=g_config.get('mysqluser'),
                         passwd=g_config.get('mysqlpasswd'), db=g_config.get('dbname'), charset='utf8')

    cursor = db.cursor()

    sql = "select DISTINCT a.username,a.password,e.name from (((" \
          "opm_rbac_account a inner join opm_rbac_user b on a.userId=b.userId)" \
          "inner join opm_rbac_role_user_account c on a.accountId=c.accountId)" \
          "inner join opm_rbac_role d on c.roleId=d.roleId)" \
          "inner join opm_rbac_role_template e on d.rtId=e.rtId " \
          "where b.mobile='%s' " \
          "and b.isDelete=0 " \
          "and a.isDelete=0 " \
          "and a.username is not Null " \
          "and a.username !=''"%tel
    cursor.execute(sql)
    msg = cursor.fetchall()

    for i in msg:
        username=i[0]
        passwd=i[1]
        identity=i[2]
        try:
            param_data = {'env': dc_env, 'type': dc_type, 'aes': 'de', 'str': passwd}
            r = requests.get(base_url + '/get', headers=header, params=param_data)
            print("account:"+username+"\n"+'passwd:' + r.text+"\n"+"身份："+identity+"\n"+"绑定的号码:"+tel)
            sleep(1)
        except:
            print("密码解析失败！")
            pass
        print("\n"+"------------------------------------------------------------------")
    db.close()


if __name__ == '__main__':
    # 通过输入手机号得到该手机号下面的所有账号的用户名、身份、密码
    # get_message('prod','iortho','sh_adv','18910908719')
    get_message('sit','iortho','sh_sit','17755118191')