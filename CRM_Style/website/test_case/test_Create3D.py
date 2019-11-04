import unittest
from CRM_Style.website.test_case.page_object.LoginCRM import *
from CRM_Style.website.test_case.page_object.serach_patient import *
from CRM_Style.website.test_case.page_object.upload_STLAndDDM import *
from CRM_Style.website.test_case.page_object.dsign_Scheme import *
from CRM_Style.website.test_case.page_object.upload_ods import *
from CRM_Style.website.test_case.page_object.accept_Alert import *
from CRM_Style.driver.driver import *

class Create3D(unittest.TestCase):

    #数据初始化，从这里传入参数即可
    def setUp(self):

        self.caseid = ["C01001243875"]     #传入病例的病例号，支持传入多个，以英文状态的逗号分隔

        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.username="shihm"
        self.password="123456"
        self.url="http://crm-web.sh-sit.eainc.com/crm/index.php?module=Home&action=index"
        self.douplepath=r"C:\Users\Administrator\Desktop\doupleDDM"
        self.singlepath=r"C:\Users\Administrator\Desktop\singleDDM"
        # self.zzdpath=r"C:\Users\Administrator\Desktop\ODSZKD"
        self.stl=[r"C:\Users\Administrator\Desktop\photos\001.jpg", r"C:\Users\Administrator\Desktop\photos\007.jpg"]

    def tearDown(self):
        self.driver.quit()

    #这是双膜的第1阶段的第1个方案
    def test_douple3D_1_1(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id,"1_1")   #这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                print(">>>上传咬合stl以及ddm")
                uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_1")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "1_1",0,1,1)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是双膜的第1阶段的第2个方案
    def test_douple3D_1_2(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id,"1_2")   #这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "1_2",0,2,2)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是双膜的第1阶段的第3个方案
    def test_douple3D_1_3(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id,"1_3")   #这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "1_3",0,3,3)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是双膜的第1阶段的第4个方案
    def test_douple3D_1_4(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id,"1_4")   #这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "1_4",0,4,4)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是双膜的第2阶段的第1个方案
    def test_douple3D_2_1(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id,"2_1")   #这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "2_1",1,1,1)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是双膜的第2阶段的第2个方案
    def test_douple3D_2_2(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id, "2_2")  # 这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "2_2", 1, 2, 2)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是双膜的第3阶段的第1个方案
    def test_douple3D_3_1(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.douplepath, id, "3_1")  # 这个应该返回一个ods列表
                get_new_json(self.douplepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.douplepath, id, "3_1", 2, 1, 1)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])


    #这是单膜的第1阶段的第1个方案
    def test_single3D_1_1(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id,"1_1")   #这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                print(">>>上传咬合stl以及ddm")
                uploadStlAndDdm(self.driver, self.stl, self.singlepath, id,"1_1")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "1_1",0,1,1)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是单膜的第1阶段的第2个方案
    def test_single3D_1_2(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id,"1_2")   #这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "1_2",0,2,2)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是单膜的第1阶段的第3个方案
    def test_single3D_1_3(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id,"1_3")   #这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "1_3",0,3,3)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是单膜的第1阶段的第4个方案
    def test_single3D_1_4(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id,"1_4")   #这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "1_4",0,4,4)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是单膜的第2阶段的第1个方案
    def test_single3D_2_1(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id,"2_1")   #这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "2_1",1,1,1)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是单膜的第2阶段的第2个方案
    def test_single3D_2_2(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id, "2_2")  # 这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "2_2", 1, 2, 2)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])

    # 这是单膜的第3阶段的第1个方案
    def test_single3D_3_1(self):
        print(">>>开始登录crm，因系统原因，登录时间可能较长，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        for id in self.caseid:
            try:
                print(">>>开始创建病例号为 %s 的3D方案" % (id))
                print(">>>准备文件重命名、更改json")
                rename_file(self.singlepath, id, "3_1")  # 这个应该返回一个ods列表
                get_new_json(self.singlepath, id)
                print(">>>查找病例")
                searchPatient(self.driver, id)
                # print(">>>上传咬合stl以及ddm")
                # uploadStlAndDdm(self.driver, self.stl, self.douplepath, id,"1_2")
                print(">>>设计方案中......")
                dsignScheme(self.driver)
                print(">>>上传ods四文件")
                uploadOds(self.driver, self.singlepath, id, "3_1", 2, 1, 1)
                print(">>>加载同步以及处理警告弹窗")
                acceptAlert(self.driver)
                print(">>>病例号为 %s 的3D方案创建成功" % (id) + "\n")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (id) + "\n")
                self.driver.switch_to.window(get_handles(self.driver)[0])