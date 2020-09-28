import configparser
import getopt
import xlrd
import os
import pymysql
import shutil
from time import sleep
from PIL import Image
import numpy as np
import re
import cv2
from selenium.webdriver import ActionChains
import json
from xpinyin import Pinyin

excel_option = ["id", "desc", "keywords", "selector", "val", "level"]
common_config = ["mysql_datebase", "email"]


# 获取配置项
def get_golobal_config(env=None, file_path=None):
    if env is None:
        env = "iortho_sit"
    if file_path is None:
        file_path = "config.ini"
    cf = configparser.ConfigParser()
    cf.read(os.path.join(get_root_path(),file_path),'utf-8')
    g_config = {}
    common_config.append(env)
    for config_name in common_config:
        for item in cf.items(config_name):
            g_config[item[0]] = item[1]
    return g_config


# 获取命令行参数
def get_opt(argv):
    t_opt = {}
    opts, args = getopt.getopt(argv, "", ["env=", "test_case=", "level=", "func=", "casecode=", "phase=", "type=", "update"])
    for opt, arg in opts:
        if "update" in opt:
            t_opt[opt[2:]] = True
        else:
            t_opt[opt[2:]] = arg
    return t_opt


# 读取Excel
def read_excel(file_path, option_key=None, json_type=None):
    if option_key is None:
        # excel要取的列以及对应的关键字
        option_key = ["id", "desc", "keywords", "selector", "val", "level"]
    data_list = []
    json_data = {}
    work_book = xlrd.open_workbook(file_path)
    data_sheet = work_book.sheets()[0]
    row_num = data_sheet.nrows
    col_num = data_sheet.ncols
    for i in range(row_num):
        col_data = {}
        for j in range(col_num):
            if j < len(option_key):
                if json_type is True:
                    if i > 0 and j == 0:
                        json_data[data_sheet.cell_value(i, 0)] = data_sheet.cell_value(i, 1)
                else:
                    col_data[option_key[j]] = data_sheet.cell_value(i, j)
        # 去掉excel第一行是注释
        if i > 0:
            data_list.append(col_data)
    return json_data if json_type is True else data_list


# 获取指定路径下的所有文件路径
def list_dir(file_path, file_list=None):
    if file_list is None:
        file_list = []
    # 文件直接返回
    if os.path.isfile(file_path):
        file_list.append(file_path)
        return file_list
    dir_list = os.listdir(file_path)
    for cur_file in dir_list:
        # 获取文件的绝对路径
        path = os.path.join(file_path, cur_file)
        if os.path.isfile(path):  # 判断是否是文件还是目录需要用绝对路径
            file_list.append(path)
        if os.path.isdir(path):
            list_dir(path, file_list)  # 递归子目录
    return file_list


# 获取执行用例的目录
def get_execute_dir(file_path=None):
    if file_path is None:
        file_path = "execute"
    return os.path.join(get_root_path(), "test_case", file_path)


# 获取项目根路径
def get_root_path():
    return os.path.dirname(os.path.dirname(__file__))




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


# 截图并存在到指定文件夹
def insert_img(driver, dir_name, filename):
    dir_path = os.path.join(get_root_path(), "test_report", "screenshot", dir_name)
    if os.path.exists(dir_path):
        driver.get_screenshot_as_file(os.path.join(dir_path, filename))
    else:
        os.makedirs(dir_path)


def handle_case_result(case_result,case_store):
    failed_case_id = case_result.get("failed")
    generate_test_report(case_result,case_store)
    for case_id in case_result.get("total"):
        # 删除成功的截图以及保存的照片
        if case_id not in failed_case_id:
            del_file(os.path.join(get_root_path(), "test_report", "screenshot", case_id))
            save_check_filelist = list_dir(os.path.join(get_root_path(), "test_report", "screenshot", "save_check"))
            for save_check_file in save_check_filelist:
                save_check_filename = os.path.split(save_check_file)[1]
                if save_check_filename.startswith(case_id):
                    del_file(save_check_file)

#生成测试报告
def generate_test_report(case_result,case_store):
    final_path=os.path.join(get_root_path(),"test_report","report.html")
    origin_path=os.path.join(get_root_path(),"test_report","report_temp.html")
    table_str=""
    p = Pinyin()
    for (key,case_list) in case_store.items():
        if key in case_result.get("failed"):
            for index,case in enumerate(case_list):
                flag='成功' if case.get("traceback") is None else '失败'
                info=case.get('traceback',"").replace(f"\n","<br>")
                img_src="screenshot/{}/{}_{}.png".format(case.get("id"),index, p.get_pinyin(case.get("desc"),""))
                table_str += f""" <tr>
                    <td {'class="red"' if flag=='失败' else ''}>{flag}</td>
                    <td>{case.get("id")}</td>
                    <td>{case.get('desc')}</td>
                    <td>{case.get('keywords')}</td>
                    <td>{case.get('selector')}</td>
                    <td>{case.get('val')}</td>
                    <td>{info}</td>
                    <td>
                        <img src="{img_src}" />
                    </td>
                </tr>"""
    with open(origin_path,'r',encoding="utf-8") as temp:
        with open(final_path,"w",encoding="utf-8") as final_f:
            for line in temp:
                line=line.replace("__total_result__",str(len(case_result.get("total"))))
                line = line.replace("__failed_result__", str(len(case_result.get("failed"))))
                line = line.replace("__result_table_info__", table_str)
                final_f.write(line)




# 删除文件
def del_file(filepath):
    if os.path.exists(filepath):
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
        if os.path.isfile(filepath):
            os.remove(filepath)


# 将当前页面拖到最底部
def pageDown(driver):
    js = "var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    sleep(2)


# 单张截图通过滚动截图拼接成一张整图
def full_page_screenshot(driver, filename, selector=None):
    sleep(2)
    if selector is None:
        dom_ele = "document.documentElement"
    elif selector.startswith("/"):
        dom_ele = 'document.evaluate(\'{0}\',document).iterateNext()'.format(selector)
    else:
        dom_ele = 'document.querySelector(\'{}\')'.format(selector)
    driver.execute_script('{}.scrollTop=0'.format(dom_ele))
    driver.execute_script('document.querySelector(".iortho-header").style.display="none"')
    sleep(5)
    client_height = driver.execute_script('return {}.clientHeight'.format(dom_ele))
    print(client_height)
    # 页面高度
    page_height = driver.execute_script('return {}.scrollHeight'.format(dom_ele))
    print(page_height)
    driver.save_screenshot(filename)

    if page_height > client_height:
        n = page_height // client_height  # 需要滚动的次数
        base_mat = np.atleast_2d(Image.open(filename))  # 打开截图并转为二维矩阵

        for i in range(n):
            driver.execute_script('{}.scrollTop={};'.format(dom_ele, client_height * (i + 1)))
            sleep(.5)
            tem_img = f'test_{i}.png'
            # action_chains.move_by_offset(0, 0)
            # action_chains.perform()
            driver.save_screenshot(tem_img)  # 保存截图
            mat = np.atleast_2d(Image.open(tem_img))  # 打开截图并转为二维矩阵
            base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
            os.remove(tem_img)
        Image.fromarray(base_mat).save(filename)
    driver.execute_script(
        'document.querySelector(".iortho-header").style.display="block"')


# 去掉文件名特殊字符
def rep_filename(filename):
    regexp = re.compile(r"[/\*\'\[\]]")
    return regexp.sub("", filename)


# 均值哈希算法
def aHash(img):
    # 缩放为8*8
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    # 转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    # 遍历累加求像素和
    for i in range(8):
        for j in range(8):
            s = s + gray[i, j]
    # 求平均灰度
    avg = s / 64
    # 灰度大于平均值为1相反为0生成图片的hash值
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# 差值感知算法
def dHash(img):
    # 缩放8*8
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str


# Hash值对比
def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n


# 等比例压缩图片
def resize_img(ori_img, dst_img, dst_w=None, dst_h=None, save_q=75):
    im = Image.open(ori_img)
    ori_w, ori_h = im.size
    width_ratio = height_ratio = None
    ratio = 1
    if (dst_w and  ori_w > dst_w) or (dst_h and ori_h > dst_h):
        if dst_w and ori_w > dst_w:
            width_ratio = float(dst_w) / ori_w  # 正确获取小数的方式
        if dst_h and ori_h > dst_h:
            height_ratio = float(dst_h) / ori_h

        if width_ratio and height_ratio:
            if width_ratio < height_ratio:
                ratio = width_ratio
            else:
                ratio = height_ratio

        if width_ratio and not height_ratio:
            ratio = width_ratio
        if height_ratio and not width_ratio:
            ratio = height_ratio

        new_width = int(ori_w * ratio)
        new_height = int(ori_h * ratio)
    else:
        new_width = ori_w
        new_height = ori_h
    im.resize((new_width, new_height), Image.ANTIALIAS).save(dst_img, quality=save_q)


# 格式化数字字符串  比如 2.0=>2
def format_digit_str(val):
    if val is None:
        return val
    try:
        if isinstance(val, str):
            pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
            if pattern.match(val) is None:
                return val
            else:
                val = float(val)
        return [str(val), str(int(val))][int(val) == val]
    except:
        return val


# 加载excel中的选择器（key对应的实际选择器表达式）
def load_ele_selector(ele_key):
    if ele_key == "" or ele_key is None:
        return ""
    file_path = os.path.join(get_root_path(), "element_selector")
    dir_names = ele_key.split(".")
    dir_names_len=len(dir_names)
    if dir_names_len<=1:
        return ""
    # 比如：casedetail.detail.submit   casedetail是目录名，detai是json文件名，submit是json文件中key
    for index, name in enumerate(dir_names):
        if index != dir_names_len-1:
            if index == dir_names_len-2:
                name = name+".xls"
            file_path = os.path.join(file_path, name)
    json_data = ""
    try:
        json_data = read_excel(file_path, ["key", "selector"], True)
    except:
        pass
    return json_data


def get_selector_val(mainhandler, case):
    selector = case.get("selector")
    if selector != "" and selector is not None and selector.find(".") > -1:
        index = selector.rindex(".")
        # 比如：casedetail.detail.submit  把"casedetail.detail"作为key存放json文件里的数据在ele_selector_store
        store_key = selector[0:index]
        # json文件中的key （上面的submit）
        selector_json_key = selector[index+1:]
        json_data = mainhandler.ele_selector_store.get(store_key)
        if json_data is None:
            # 重新加载json数据
            json_data = load_ele_selector(selector)
        if json_data is not None and json_data != "":
            selector_json_val = json_data.get(selector_json_key)
            mainhandler.ele_selector_store[store_key] = json_data
            if selector_json_val != "" and selector_json_val is not None:
                case["selector"] = selector_json_val
