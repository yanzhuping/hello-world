#生成大量不重复的姓名并存入指定的数据库或者excel中
#通过修改循环次数控制生成个数

import random
import pymysql
from Auto_iortho.website.test_case.models.function import get_fileBasePath
import xlsxwriter
from Auto_iortho.website.test_case.models.config import *

def getRandomName():
    '''将姓、名存入不同的列表'''

    firstNamePath=get_fileBasePath()+'/website/test_data/firstname.txt'
    midleNamePath=get_fileBasePath()+'/website/test_data/midlename.txt'
    lastNamePath=get_fileBasePath()+'/website/test_data/lastname.txt'

    firstname = []
    midlename = []
    lastname = []


    f1=open(firstNamePath,'r')
    content1='\n'.join(f1.read())
    content1=content1.split('\n')
    for first in content1:
        firstname.append(first)

    f2=open(midleNamePath,'r')
    content2='\n'.join(f2.read())
    content2=content2.split('\n')
    for midle in content2:
        midlename.append(midle)

    f3=open(lastNamePath,'r')
    content3='\n'.join(f3.read())
    content3=content3.split('\n')
    for last in content3:
        lastname.append(last)

    f1.close()
    f2.close()
    f3.close()

    return firstname,midlename,lastname

def nameToMySQL():
    '''将生成的大量姓名存入指定的数据库表'''

    db = pymysql.Connect(
        host= host, port=3306, user=mysqluser, passwd=mysqlpasswd, db=dbName, charset='utf8')

    # 创建一个游标对象，执行数据操作
    cursor = db.cursor()

    fullname=[]

    for i in range(20000):
        name1=random.choice(
            getRandomName()[0])+random.choice(
            getRandomName()[1])+random.choice(
            getRandomName()[2])
        # print(name1)
        name2=name1.rstrip()
        if name2 not in fullname:
            fullname.append(name2)

    print(len(fullname))


    for a in range(len(fullname)):

        cursor.execute("insert into %s(name) values('%s')"%(tableName,fullname[a]))
        db.commit()

    db.close()

nameToMySQL()

def nameToExcel():
    '''将生成的大量姓名存入excel表'''
    fullname = []

    for i in range(10000):
        name1 = random.choice(
            getRandomName()[0]) + random.choice(
            getRandomName()[1]) + random.choice(
            getRandomName()[2])

        name2 = name1.rstrip()
        if name2 not in fullname:   #防止存入的姓名重复
            fullname.append(name2)

    workbook=xlsxwriter.Workbook(get_fileBasePath()+'/website/test_data/names.xlsx')
    worksheet=workbook.add_worksheet()
    worksheet.write("A1","id")
    worksheet.write("B1","name")

    for i in range(len(fullname)):
        worksheet.write("A"+str(i+2),i+1)
        worksheet.write("B"+str(i+2),fullname[i])

    workbook.close()

# nameToExcel()
