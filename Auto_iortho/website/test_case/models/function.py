import json
import os
import re
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from time import sleep
from website.test_case.models.config import *
import pymysql
import xlrd
import win32com.client

from win32com.client import Dispatch

from email.mime.multipart import MIMEMultipart



#获取窗口句柄
def get_handles(driver):
    handles=driver.window_handles
    return handles

#暂存
def staging(driver):
    driver.find_element_by_class_name("page-teenagers-footer-save").click()

#下一页
def nextpage(driver):
    driver.find_element_by_class_name("page-teenagers-footer-next").click()
    sleep(2)

#提交
def submit(driver):
    driver.find_element_by_class_name('page-teenagers-footer-submit').click()
    sleep(10)
    # driver.close()


#跳转到预览页
def jumpPreview(driver):
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/adult-new-case/div[1]/teenagers-nav/div/ul/li[4]').click()
    sleep(2)

#跳转到基本信息页
def jumpBaseInformation(driver):
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/adult-new-case/div[1]/teenagers-nav/div/ul/li[1]').click()
    sleep(0.5)


#获取当前文件所在目录的上一级目录的绝对路径
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

    base = base_dir.split('/website')[0]

    return base

#截图并存在到指定文件夹
def insert_img(driver,filename, scroll_element_selector = "html"):

    filepath=get_fileBasePath()+'/website/test_report/screenshot/'+filename

    driver.get_screenshot_as_file(filepath)


    # js_height = "return document.querySelector('%s').scrollHeight + 300" % (scroll_element_selector)
    #
    # try:
    #     k = 1
    #     height = driver.execute_script(js_height)
    #     print('scroll height: ', height)
    #     while True:
    #         if k < height:
    #             js_move = "document.querySelector('%s').scrollTop = %s" % (scroll_element_selector, k)
    #             print(js_move)
    #             driver.execute_script(js_move)
    #             sleep(1)
    #             k += 300
    #         else:
    #             break
    #     scroll_width = driver.execute_script('return document.body.clientWidth')
    #     scroll_height = height
    #     driver.set_window_size(scroll_width, scroll_height)
    #     driver.get_screenshot_as_file(filepath)
    #
    #
    # except:
    #     print("截图失败")



#获取测试照片数据相对项目的路径
def choice_photo():

    photolist=[]

    filepath_1 = get_fileBasePath() + '/website/test_data/photos'
    # print(filepath)
    filelist=os.listdir(filepath_1)

    for file in filelist:
        fullname=os.path.join(filepath_1,file)
        fullname=fullname.replace("\\","/")
        photolist.append(fullname)

    return photolist


#获取患者详情页的url，并提取病例序号，以备后用
def getCaseNum(driver):

    strr=driver.current_url
    pat=re.compile(r"C\d\d\d\d\d\d\d\d\d\d\d")
    result=pat.search(strr).group()

    return result


#将当前页面拖到最底部
def pageDown(driver):
    js = "var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    sleep(2)

#将当前页面拖到最顶部
def pageUp(driver):
    js = "var action=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    sleep(2)


#将对应文件夹的文件更改名称，符合上传要求
def rename_file(id,type_mopian,num):  #num是哪一个阶段的3D方案，1_1,1_2,2_1.....

    ods = []
    filepath_2=''

    if type_mopian == 0:
        filepath_2 = get_fileBasePath() + '/website/test_data/doupleDDM'
    elif type_mopian == 1:
        filepath_2 = get_fileBasePath() + '/website/test_data/singleDDM'
    # print(filepath)

    filelist = os.listdir(filepath_2)
    for files in filelist:
        olddir = os.path.join(filepath_2, files)
        filetype = os.path.splitext(files)[1]
        if num=="1_1":
            if "V6" in files:
                newdir = os.path.join(filepath_2, id + "_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_2, id + filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="1_2":
            if "V6" in files:
                newdir = os.path.join(filepath_2, id + "_1"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_2, id +"_1"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="1_3":
            if "V6" in files:
                newdir = os.path.join(filepath_2, id + "_11"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_2, id +"_11"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        else:
            print("阶段参数传递错误")

    return ods

#修改json文件中的病例序号，得到一个新的json文件
def get_new_json(id,type_mopian):
    filepath_3 = ''
    if type_mopian == 0:  #双膜
        filepath_3 = get_fileBasePath() + '/website/test_data/doupleDDM'
    elif type_mopian == 1: #单膜
        filepath_3 = get_fileBasePath() + '/website/test_data/singleDDM'

    filename = os.listdir(filepath_3)  # 获取需要修改的文件的名字
    name = []
    key="CaseInfo"
    for filename_rest in filename:
        if os.path.splitext(filename_rest)[1] == '.json':
            name.append(os.path.join(filepath_3, filename_rest))

    for f11 in name:
        key_ = key.split(".")
        key_length = len(key_)
        with open(f11, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            i = 0
            a = json_data
            value = "{'CaseID': %s, 'Name': '目标位'}" % (id)
            while i < key_length:
                if i + 1 == key_length:
                    a[key_[i]] = value
                    i = i + 1
                else:
                    a = a[key_[i]]
                    i = i + 1
        f.close()
        with open(f11, 'w', encoding='utf-8') as f1:
            json.dump(json_data, f1, ensure_ascii=False)
        f1.close()


#发送邮件模块，不带附件，只有内容
def send_mail(latest_report,e_server,e_user,e_password,e_sender,e_receives):

    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = e_server

    user = e_user
    password = e_password #这是客户端授权码，根据自己邮箱密码来设置

    sender = e_sender
    receives = e_receives

    subject = 'Web Selenium 自动化测试报告'


    msg = MIMEText(mail_content, 'html', 'utf-8')   #邮件内容
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send email end!")


#发送带附件+正文的邮件模块
def send_mail_attachment(latest_report,e_server,e_user,e_password,e_sender,e_receives):

    smtpserver = e_server

    user = e_user
    password = e_password #这是客户端授权码，根据自己邮箱密码来设置

    sender = e_sender
    receives = e_receives

    subject = 'Web Selenium 自动化测试报告'   #邮件标题

    f = open(latest_report, 'rb')
    mail_content = f.read()        #需要发送的正文
    f.close()

    send_file=open(latest_report,'rb').read()  #需要发送的附件

    att=MIMEText(send_file,'base64','utf-8')
    att['Content-Type']='application/octet-stream'
    att['Content-Disposition'] = "attachment;filename='%s'"%(latest_report)

    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receives)
    msgRoot.attach(att)


    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print("Start send email...")
    smtp.sendmail(sender, receives, msgRoot.as_string())
    smtp.quit()
    print("Send email end!")


#在所有的测试报告中查找最新的一份测试报告
def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    print("the latest report is " + lists[-2])

    file = os.path.join(report_dir, lists[-2])

    return file


#从数据库读取一条数据
def readDataFromMySQL(host,mysqluser,mysqlpasswd,dbName,tableName):

    #连接数据库
    db = pymysql.Connect(
        host=host, port=3306, user=mysqluser, passwd=mysqlpasswd, db=dbName, charset='utf8')

    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()

    sql="select name from %s order by id asc limit 1"%(tableName)
    cursor.execute(sql)
    input_name=cursor.fetchone()
    db.close()

    return input_name[0]


#从数据库中删除已经读取的数据
def deleteDataFromMySQL(host,mysqluser,mysqlpasswd,dbName,tableName):
    # 连接数据库
    db = pymysql.Connect(
        host=host, port=3306, user=mysqluser, passwd=mysqlpasswd, db=dbName, charset='utf8')

    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()
    sql="delete from %s where name='%s'"%(
        tableName,readDataFromMySQL(host,mysqluser,mysqlpasswd,dbName,tableName))
    cursor.execute(sql)

    db.commit()
    db.close()

# deleteDataFromMySQL('localhost','root','root123','test1','names')

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

    xlBook = win32com.client.Dispatch('Excel.Application').Workbooks.Open(
        get_fileBasePath()+'/website/test_data/names.xlsx')

    sht = xlBook.Worksheets('Sheet1')

    sht.Rows(1).Delete()

    xlBook.Save()

    xlBook.Close(SaveChanges=0)

# deleteDataFromExcel()