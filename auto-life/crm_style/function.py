import os
import json
import random
import configparser
import getopt
import sys
import pymysql
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pymouse import *
# from pykeyboard import *
from time import sleep
from random import choice
from selenium.webdriver.common.by import By
import xlrd
# import win32com.client
#获取当前项目的根目录
def get_fileBasePath():
    func_path = os.path.dirname(__file__)
    # print(func_path)
    base_dir = os.path.dirname(func_path)
    # print(base_dir)
    # 将路径转化为字符串
    base_dir = str(base_dir)
    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)
    base = base_dir.split('/crm_style')[0]
    # print(base)
    return base
# print(get_fileBasePath())

def choice_file(dir):
    photolist = []
    filepath_1 = os.path.join(get_fileBasePath(), 'test_data', dir)
    filelist=os.listdir(filepath_1)
    for file in filelist:
        fullname = os.path.join(filepath_1, file)
        photolist.append(fullname)
    return photolist


#去重上传照片
def upload_photos(dir,num,driver,keyid):
    photolist1 = []
    a=0
    while a<num:
        a=a+1
        target=choice(choice_file(dir))
        if target not in photolist1:
            photolist1.append(target)
        elif target in photolist1:
            a=a-1
    for i in range(num):
        if i<8:
            driver.find_element(By.NAME, '%s-%s' % (keyid, str(i+1))).send_keys(photolist1[i])
            sleep(0.5)
        else:
            driver.find_element(By.NAME, '%s-%s' % (keyid, str(i+193))).send_keys(photolist1[i])
        sleep(0.5)




#获取窗口句柄，一个列表形式
def get_handles(driver):
    handles=driver.window_handles
    return handles

#生成指定范围内的随机数
def randomValue():
    i = 0
    list = []
    while i < 2:
        i = i + 1
        ran = random.randint(1111111111111, 9999999999999)
        list.append(str(ran))
    return list

#获取配置项
def get_golobal_config(env=None):
    common_config=[]
    file_path = get_fileBasePath() + "/crm_style"+"/config_1.ini"
    # print(file_path)
    cf = configparser.ConfigParser()
    cf.read(file_path,'utf-8')
    g_config = {}
    if env == "iortho_sit" or env is None:
        common_config.append("iortho_sit")
        common_config.append("iortho_sit_doc")
        common_config.append("mysql_datebase")
        # print(common_config)
        for config_name in common_config:
            for item in cf.items(config_name):
                g_config[item[0]] = item[1]
    elif env == "iortho_adv":
        common_config.append("iortho_adv")
        common_config.append("iortho_adv_doc")
        common_config.append("mysql_datebase")
        for config_name in common_config:
            for item in cf.items(config_name):
                g_config[item[0]] = item[1]
    elif env == "comfos_sit":
        common_config.append("comfos_sit")
        common_config.append("comfos_sit_doc")
        common_config.append("mysql_datebase")
        for config_name in common_config:
            for item in cf.items(config_name):
                g_config[item[0]] = item[1]
    return g_config


# print(get_golobal_config())

#获取命令行参数
def get_opt(argv):
    t_opt = {}
    opts, args = getopt.getopt(argv, "", ["env=","caseid=", "patientname=","num=","dir="])
    for opt, arg in opts:
        t_opt[opt[2:]] = arg
    return t_opt

#处理传入的dir参数
def get_dir():
    val=get_opt(sys.argv[1:]).get("dir")
    # print(val)
    # print(type(val))
    if val is None or val == "":
        val="singleDDM"
    elif val == "0":
        val="doubleDDM"
    elif val == "1":
        val = "doublePullOutMoreTeeth"
    elif val == "2":
        val = "doublePullingtooth"
    elif val == "3":
        val = "singlePullOutMoreTeeth"
    elif val == "4":
        val = "singlePullingtooth"
    elif val =='5':
        val='doubleNoPullingtooth'
    elif val =='6':
        val='doubleAllPullOutTooth'
    elif val =='7':
        val='singleBabyTeeth'
    elif val =='8':
        val='singleErp'
    # print(val)
    return val

#处理传入的病例序号参数
def get_caseid():
    val=get_opt(sys.argv[1:]).get("caseid","1")
    if val == 1:
        pass
    if val !="":
        val=val
    return val

#处理服务号参数，根据该参数执行不同的脚本
def get_num():
    val=get_opt(sys.argv[1:]).get('num')
    if val is None:
        val="0_1_1"
    if val != "":
        val=val
    return val

#处理传入的患者姓名（线下新建病例需要该参数）
def get_patientname():
    val=get_opt(sys.argv[1:]).get('patientname')
    if val is None:
        val="线下"+ str(random.randint(11111,99999))
    if val != "":
        val=val
    return val

def rename_file(id,dir):
    ods = []
    filepath_1 = os.path.join(get_fileBasePath(), "test_data", dir)
    filelist = os.listdir(filepath_1)
    pre_path = "{}_{}".format(id, random.randint(1, 1000000))
    for filepath in filelist:
        olddir = os.path.join(filepath_1, filepath)
        filetype = os.path.splitext(filepath)[1]
        if "V6" in filepath:
            newdir = os.path.join(filepath_1, pre_path + "_V6" + filetype)
            os.rename(olddir, newdir)
        else:
            newdir = os.path.join(filepath_1, pre_path + filetype)
            os.rename(olddir, newdir)
        if filetype == ".json":
            get_new_json(newdir, id)
        ods.append(newdir)
    return ods

# 修改json文件中的指定键对应的值
def get_new_json(filepath, id, json_key=None):
    if json_key is None:
        json_key = "CaseInfo"
    key_ = json_key.split(".")
    key_length = len(key_)
    def _readFile(encoding):
        with open(filepath, 'r', encoding=encoding) as f:
            json_data = json.load(f)
            i = 0
            a = json_data
            value = "{'CaseID': %s, 'Name': '目标位'}" % id
            while i < key_length:
                if i + 1 == key_length:
                    a[key_[i]] = value
                    i = i + 1
                else:
                    a = a[key_[i]]
                    i = i + 1
            f.close()
            with open(filepath, 'w', encoding=encoding) as f1:
                json.dump(json_data, f1, ensure_ascii=False)
            f1.close()
    try:
        _readFile('utf-8')
    except:
        _readFile('gbk')


def readDataFromMySQL(g_config):
    # 连接数据库
    db = pymysql.Connect(
        host=g_config.get("host"), port=3306, user=g_config.get("mysqluser"),
        passwd=g_config.get("mysqlpasswd"), db=g_config.get("dbname"), charset='utf8')
    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()

    sql="select name from %s order by id asc limit 1"%(g_config.get("tablename"))
    cursor.execute(sql)
    input_name = cursor.fetchone()
    db.close()

    return input_name[0]

# 从数据库中删除已经读取的数据
def deleteDataFromMySQL(g_config):
    # 连接数据库
    db = pymysql.Connect(
        host=g_config.get("host"), port=3306, user=g_config.get("mysqluser"),
        passwd=g_config.get("mysqlpasswd"), db=g_config.get("dbname"), charset='utf8')

    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()
    sql="delete from %s where name='%s'"%(
        g_config.get("tablename"),readDataFromMySQL(g_config))
    cursor.execute(sql)

    db.commit()
    db.close()

def check_loading_is_hide(driver):
    wait = WebDriverWait(driver, 40, 0.5)
    loading_ele = driver.execute_script("return document.querySelector('.iortho-global-loading')")
    percent_ele = driver.execute_script("return document.querySelector('#fileupload_loadingImg')")
    popover = driver.execute_script("return document.querySelector(\"[ng-show=\'$ctrl.popoverShow\']\")")
    if percent_ele is not None:
        wait.until(EC.staleness_of(percent_ele))
    if loading_ele is not None:
        wait.until(EC.staleness_of(loading_ele))
    if popover is not None:
        wait.until(EC.invisibility_of_element(popover))

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __getX(self):
        return self.x

    def __getY(self):
        return self.y

    @property
    def print_value(self):
        return print('x坐标为：'+str(self.__getX())+'\n'+'y坐标为：'+str(self.__getY()))
def drag_and_drop(driver,source_xpath,target,offset,x_change):
    '''单次拖拽图片方法
    Args:
        browser:浏览器驱动
        source_xpath：原始图片xpath表达式
        target：目标图片webElement对象
        offset：用于左右两侧图片上下有偏差的情况。 向上偏移为负数 向下偏移为正数
    Returns：
        无返回值None
    Raises:
        未捕捉
    '''

    mouse=PyMouse()
    #图片中心点的原始坐标
    source=driver.find_element_by_xpath(source_xpath)
    source_coordinate= Point(source.location.get('x'),source.location.get('y'))
    target_coordinate= Point(target.location.get('x'),target.location.get('y'))
    #计算中心点到四边的距离
    xCentreFrom = source.size.get('height') // 2
    yCentreFrom = source.size.get('width') // 2
    xCentreTo = target.size.get('height') // 2
    yCentreTo =target.size.get('width') // 2
    #图片中心点的原始坐标
    source_coordinate= Point(source.location.get('x'),source.location.get('y'))
    target_coordinate= Point(target.location.get('x'),target.location.get('y'))
    #调试代码
    # source_coordinate.print_value
    # target_coordinate.print_value
    #图片左上角的坐标
    source_coordinate.x += xCentreFrom+x_change
    source_coordinate.y += yCentreFrom+offset
    target_coordinate.x += xCentreTo+x_change
    target_coordinate.y += yCentreTo+offset
    # 拖拽鼠标
    mouse.press(source_coordinate.x,source_coordinate.y,1)
    mouse.move(((target_coordinate.x - source_coordinate.x) // 2) + source_coordinate.x, ((target_coordinate.y - source_coordinate.y) // 2) + source_coordinate.y)
    sleep(1)
    mouse.move(target_coordinate.x, target_coordinate.y)
    sleep(1)
    mouse.release(target_coordinate.x, target_coordinate.y,1)
    sleep(1)


def choose_pic(driver,source_xpath,target_list,offset,x_change):
    '''通过调用单次拖拽图片的方法，实现将全部图片拖拽到目标位置
    Args:
        browser:浏览器驱动
        source_xpath：原始图片xpath表达式
        target_list：目标图片webElement对象的一个List
        offset：用于左右两侧图片上下有偏差的情况。 向上偏移为负数 向下偏移为正数
    Returns：
        无返回值None
    Raises:
        未捕捉
    '''

    # keyboard=PyKeyboard()
    # # 按F11全屏
    # driver.execute_script("alert('窗口置于最前！')")
    # sleep(1)
    # driver.switch_to_alert().accept()
    # sleep(1)
    # keyboard.tap_key(keyboard.function_keys[11])
    # sleep(2)
    # #拖拽照片
    # for target in target_list:
    #     drag_and_drop(driver,source_xpath,target,offset,x_change)
    # #按F11恢复窗口
    # keyboard.tap_key(keyboard.function_keys[11])


#从excel姓名表中读取指定的数据
def readDataFromExcel():
    db=xlrd.open_workbook(get_fileBasePath()+'/website/test_data/names.xlsx')

    table=db.sheet_by_name('Sheet1')
    # name=table.name
    # rowNum=table.nrows
    # colNum=table.ncols
    #获取第2行第2列，即第1条数据
    input_name=table.cell_value(1,1)  #行和列都是从0开始
    # print(input_name)
    return input_name

# readDataFromExcel()

#删除excel中的指定内容,即读取用完的内容删掉
def deleteDataFromExcel():
    pass
    # xlBook = win32com.client.Dispatch('Excel.Application').Workbooks.Open(
    #     get_fileBasePath()+'/website/test_data/names.xlsx')
    #
    # sht = xlBook.Worksheets('Sheet1')
    #
    # sht.Rows(1).Delete()
    #
    # xlBook.Save()
    #
    # xlBook.Close(SaveChanges=0)

# deleteDataFromExcel()


#对比两个excel文件的不同