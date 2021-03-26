import requests
from crm_style.function import *

class Get_passwd():
    def __init__(self,env,type,db_env):
        self.env=env
        self.type=type
        self.g_config = get_golobal_config(db_env)

        self.header={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}
        self.base_url = 'http://192.168.37.62:8087//func.php?'

    def connect_mysql(self,username):
        g_config = self.g_config
        db = pymysql.Connect(host=g_config.get('host'), port=3306, user=g_config.get('mysqluser'),
                             passwd=g_config.get('mysqlpasswd'), db=g_config.get('dbname'), charset='utf8')
        cursor = db.cursor()
        sql = "select passWord from %s where username='%s'" % (g_config.get('table'), username)
        cursor.execute(sql)
        input_name = cursor.fetchone()
        db.close()
        return input_name[0]

    def decode_1(self,username):
        passwd = self.connect_mysql(username)
        param_data = {'env': self.env, 'type': self.type, 'aes': 'de', 'str': passwd}
        r = requests.get(self.base_url + '/get', headers=self.header, params=param_data)
        print('account:'+username+"\n"+'password:' + r.text)
        return r.text

    # def decode(self,passwd):
    #     '''这个是通过输入加密字符得到密码的'''
    #     param_data = {'env': self.env, 'type': self.type, 'aes': 'de', 'str': passwd}
    #     r = requests.get(self.base_url + '/get', headers=self.header, params=param_data)
    #     print(r.url)
    #     print(r.status_code)
    #     print('password:' + r.text)

if __name__ == '__main__':
    #在对应的环境输入用户名即可获得密码
    # Get_passwd('sit','iortho','sh_sit').decode_1('yanzp0857')
    Get_passwd('prod', 'iortho', 'sh_adv').decode_1('huy1262')



