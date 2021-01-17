from crm_style.others_fun import *
from crm_style.new_create3D import *
from driver.driver import *
import traceback
from crm_style.erp_process import *
from crm_style.simple_case import *
from random import choice

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
        Login_1(self.driver, self.url, self.username, self.password)
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
        Login_1(self.driver, self.url, self.username, self.password)
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
        Login_1(self.driver, self.url, self.username, self.password)
        try:
            searchPatient_1(self.driver,self.caseid)
            finish_phase(self.driver)
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
        Login_1(self.driver, self.url, self.username, self.password)
        try:
            searchPatient_1(self.driver,self.caseid)
            finish_phase(self.driver)
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
        Login_1(self.driver, self.url, self.username, self.password)
        searchPatient_1(self.driver,self.caseid)
        Create_Quality_Reject(self.driver)
        print("创建成功")

    def test_quality_conformance(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login_1(self.driver, self.url, self.username, self.password)
        # searchPatient_1(self.driver, self.caseid)
        # Create_Quality_Conformance(self.driver)
        reeceiving_records(self.driver ,self.caseid)

        print("创建成功")

    def test_no_treatment(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login_1(self.driver, self.url, self.username, self.password)
        searchPatient_1(self.driver, self.caseid)
        Create_No_Treatment(self.driver)
        print("创建成功")

    def test_word_scheme(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login_1(self.driver, self.url, self.username, self.password)
        searchPatient_1(self.driver, self.caseid)
        Create_Word_scheme(self.driver)
        print("创建成功")

    def test_finish_phase(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login_1(self.driver, self.url, self.username, self.password)
        try:
            searchPatient_1(self.driver,self.caseid)
            finish_phase(self.driver)
            print("结束病例阶段成功")
        except:
            print("病例号为%s的病例结束阶段失败"%(self.caseid))
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_set_photo_disqualification(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login_1(self.driver, self.url, self.username, self.password)
        try:
            searchPatient_1(self.driver, self.caseid)
            set_photo_disqualification(self.driver)
        except:
            print("病例号为%s的口内照不合格创建失败" % (self.caseid))
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_erp_process(self):

        Login_1(self.driver, self.url, self.username, self.password)
        searchPatient_1(self.driver, self.caseid)
        ordnumber=process_orders(self.driver)
        print(type(ordnumber))
        connect_to_the_database(ordnumber)

        login_erp(self.driver)
        put_in_storage(self.driver,ordnumber)

        outbound(self.driver,ordnumber)
        print("发货成功")


class Create_New_Case():
    def __init__(self,i_username,i_password,i_url):
        self.driver=browser()
        self.i_username=i_username
        self.i_password=i_password
        self.i_url=i_url

    def test_new_case_champion_A6_1(self,g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        champion_A6_1(self.driver,g_config)

    def test_new_case_champion_A6_2(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        champion_A6_2(self.driver, g_config)

    def test_new_case_champion_A6_3(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        champion_A6_3(self.driver, g_config)

    def test_stand(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        stand(self.driver, g_config)


    def test_child(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child(self.driver, g_config)

    def test_child_A6(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child_A6(self.driver, g_config)

    def test_child_champion(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child_champion(self.driver, g_config)

    def test_child_champion_A6(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child_champion_A6(self.driver, g_config)

def test_comfos_case(username,password,url,g_config):
    driver=browser()
    comfos_case(driver,username,password,url,g_config)

def run(username,password,url,institutions,doctorname,i_username,i_password,i_url,c_username,c_password,c_url,g_config):
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
        elif get_num() == "病例照片不合格":
            Create3D(username, password, url).test_set_photo_disqualification()
            break
        elif get_num() == "发货":
            Create3D(username, password, url).test_erp_process()
            break
        elif get_num() == "冠军A6本阶段":
            Create_New_Case(i_username,i_password,i_url).test_new_case_champion_A6_1(g_config)
            break
        elif get_num() == "冠军A6后续阶段":
            Create_New_Case(i_username,i_password,i_url).test_new_case_champion_A6_2(g_config)
            break
        elif get_num() == "冠军非A6":
            Create_New_Case(i_username,i_password,i_url).test_new_case_champion_A6_3(g_config)
            break
        elif get_num() == "标准":
            Create_New_Case(i_username,i_password,i_url).test_stand(g_config)
            break
        elif get_num() == "儿童":
            Create_New_Case(i_username,i_password,i_url).test_child(g_config)
            break
        elif get_num() == "儿童A6":
            Create_New_Case(i_username,i_password,i_url).test_child_A6(g_config)
            break
        elif get_num() == "儿童加冠军":
            Create_New_Case(i_username,i_password,i_url).test_child_champion(g_config)
            break
        elif get_num() == "儿童加冠军A6":
            Create_New_Case(i_username,i_password,i_url).test_child_champion_A6(g_config)
            break
        elif get_num() == "北京病例":
            test_comfos_case(c_username,c_password,c_url,g_config)
            break
        else:
            sleep(3)
            print("指令格式不正确，请重新输入")