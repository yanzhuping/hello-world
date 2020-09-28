import configparser
import os
import pymysql

common_config = []
#获取配置项
def get_golobal_config(env=None, file_path=None):
    if env is None:
        env = "sh_sit"
    if file_path is None:
        file_path = "config_1.ini"
    cf = configparser.ConfigParser()
    cf.read(os.path.join(get_root_path(),"mysql_fun",file_path),'utf-8')
    # print(os.path.join(get_root_path(),"mysql_fun",file_path))
    g_config = {}
    common_config.append(env)
    for config_name in common_config:
        for item in cf.items(config_name):
            g_config[item[0]] = item[1]
    # print(g_config)
    return g_config

#获取根目录路径
def get_root_path():
    return os.path.dirname(os.path.dirname(__file__))

#链接数据库并创建一个游标对象
def connect_db(env=None, file_path=None):
    g_config = get_golobal_config(env, file_path)
    db = pymysql.Connect(host=g_config.get('host'), port=3306, user=g_config.get('mysqluser'),
                         passwd=g_config.get('mysqlpasswd'), db=g_config.get('dbname'), charset='utf8')
    cursor = db.cursor()
    return cursor
