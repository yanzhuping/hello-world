import os
import json
import random


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
    base = base_dir.split('/website')[0]
    # print(base)
    return base


# 获取照片文件的相对路径
def choice_photo():
    photolist = []
    filepath_3 = os.path.join(get_fileBasePath(), 'test_data', 'photos')
    filelist=os.listdir(filepath_3)
    for file in filelist:
        fullname = os.path.join(filepath_3, file)
        photolist.append(fullname)
    return photolist


#修改指定路径的文件名称，并将路径文件存储在列表中
def rename_file(type_mopian,id,num):  #num是阶段
    ods = []
    filepath_1 = ''
    if type_mopian == 0:
        filepath_1 = get_fileBasePath()+"/test_data/doupleDDM"
    if type_mopian == 1:
        filepath_1 = get_fileBasePath() + "/test_data/singleDDM"
    filelist = os.listdir(filepath_1)
    for files in filelist:
        olddir = os.path.join(filepath_1, files)
        filetype = os.path.splitext(files)[1]
        if num=="1_1":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id + filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="1_2":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_1"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id +"_1"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="1_3":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_11"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id +"_11"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="1_4":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_111"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id +"_111"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="2_1":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_1111"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id +"_1111"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="2_2":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_11111"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id +"_11111"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        elif num=="3_1":
            if "V6" in files:
                newdir = os.path.join(filepath_1, id + "_111111"+"_V6" + filetype)
                os.rename(olddir, newdir)
            else:
                newdir = os.path.join(filepath_1, id +"_1111"+ filetype)
                os.rename(olddir, newdir)
            ods.append(newdir)
        else:
            print("阶段参数传递错误")
    return ods


#修改json文件中的指定键对应的值
def get_new_json(type_mopian,id):
    filepath_2=''
    if type_mopian == 0:
        filepath_2 = get_fileBasePath() + "/test_data/doupleDDM"
    if type_mopian == 1:
        filepath_2 = get_fileBasePath() + "/test_data/singleDDM"
    filename = os.listdir(filepath_2)  # 获取需要修改的文件的名字
    name = []
    key="CaseInfo"
    for filename_rest in filename:
        if os.path.splitext(filename_rest)[1] == '.json':
            name.append(os.path.join(filepath_2, filename_rest))
    for f11 in name:
        key_ = key.split(".")
        key_length = len(key_)
        with open(f11, 'r',encoding='gbk') as f:
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
        with open(f11, 'w',encoding='gbk') as f1:
            json.dump(json_data, f1, ensure_ascii=False)
        f1.close()


# get_new_json(0,"C122222222")

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