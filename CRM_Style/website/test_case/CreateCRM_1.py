from CRM_Style.website.test_case.page_object.LoginCRM import *
from CRM_Style.website.test_case.page_object.serach_patient import *
from CRM_Style.website.test_case.page_object.offline_new_guijiao import *
from CRM_Style.website.test_case.page_object.offline_new_photo import *
from CRM_Style.website.test_case.page_object.finish_phase import *
from CRM_Style.website.test_case.page_object.offline_middle_guijiao import *
from CRM_Style.website.test_case.page_object.offline_middle_photo import *
from CRM_Style.website.test_case.page_object.quality_reject import *
from CRM_Style.website.test_case.page_object.quality_conformance import *
from CRM_Style.website.test_case.page_object.no_treatment import *
from CRM_Style.website.test_case.page_object.word_scheme import *
from CRM_Style.driver.driver import *
import traceback
from CRM_Style.website.test_case.page_object.new_create3D import *

class Create3D():
    def __init__(self,username,password,url):
        self.driver=browser()
        self.caseid = get_caseid()
        self.username=username
        self.password=password
        self.url=url

    def test_create3D(self):
        ods=rename_file(self.caseid,get_dir())
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login_1(self.driver,self.url,self.username,self.password)
        try:
            searchPatient_1(self.driver, self.caseid)
            self.driver.find_element_by_css_selector("#pause_tasks_open").click()
            self.driver.switch_to.window(get_handles(self.driver)[1])
            uploadStlAndDdm(self.driver, ods, phase=None)
            self.driver.switch_to.window(get_handles(self.driver)[0])
            dsignScheme(self.driver)
            self.driver.switch_to.window(get_handles(self.driver)[1])
            uploadOds(self.driver, ods, phase=None)
            self.driver.switch_to.window(get_handles(self.driver)[0])
            acceptAlert(self.driver)
            print("创建成功")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，\033[0m" % (self.caseid) + "\n")
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_new_guijiao(self,patientname,institutions,doctorname,):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            randomValue()
            print(">>>开始创建线下新病例硅胶")
            offline_new_guijiao(self.driver, patientname,institutions,doctorname)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :患者名为 %s的线下病例创建失败，继续执行下一个\033[0m" % (patientname) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_new_photo(self,patientname,institutions,doctorname,):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建线下新病例口内照")
            offline_new_photo(self.driver, patientname,institutions,doctorname)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :患者名为 %s的线下病例创建失败，继续执行下一个\033[0m" % (patientname) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_middle_guijiao(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            finish_phase(self.driver,self.caseid)
            print(">>>开始创建线下中期硅胶")
            offline_middle_guijiao(self.driver, self.caseid)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :病例序号为 %s的线下中期硅胶病例创建失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_middle_photo(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            finish_phase(self.driver,self.caseid)
            print(">>>开始创建线下中期口内照")
            offline_middle_photo(self.driver, self.caseid)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :病例序号为 %s的线下中期口内照病例创建失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_quality_reject(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver,self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_Quality_Reject(self.driver)
        print("创建成功")

    def test_quality_conformance(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_Quality_Conformance(self.driver)
        print("创建成功")

    def test_no_treatment(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_No_Treatment(self.driver)
        print("创建成功")

    def test_word_scheme(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_Word_scheme(self.driver)
        print("创建成功")

    def test_finish_phase(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            finish_phase(self.driver,self.caseid)
            sleep(2)
            self.driver.quit()
        except:
            print("病例号为%s的病例结束阶段失败，继续执行下一个"%(self.caseid))
            traceback_info = traceback.format_exc()
            print(traceback_info)

def run(username,password,url,institutions,doctorname):
    while True:
        if get_num() == "3d":
            Create3D(username, password, url).test_create3D()
            break
        elif get_num() == "新建硅胶":
            Create3D(username, password, url).test_offline_new_guijiao(get_patientname(),institutions,doctorname)
            break
        elif get_num() == "新建口内照":
            Create3D(username, password, url).test_offline_new_photo(get_patientname(),institutions,doctorname)
            break
        elif get_num() == "中期硅胶":
            Create3D(username, password, url).test_offline_middle_guijiao()
            break
        elif get_num() == "中期口内照":
            Create3D( username, password, url).test_offline_middle_photo()
            break
        elif get_num() == "质检合格":
            Create3D(username, password, url).test_quality_reject()
            break
        elif get_num() == "质检不合格":
            Create3D(username, password, url).test_quality_conformance()
            break
        elif get_num() == "不收治":
            Create3D(username, password, url).test_no_treatment()
            break
        elif get_num() == "文字方案":
            Create3D( username, password, url).test_word_scheme()
            break
        elif get_num() == "结束阶段":
            Create3D( username, password, url).test_finish_phase()
            break
        else:
            sleep(3)
            print("指令格式不正确，请重新输入")