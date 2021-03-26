from crm_style.others_fun import *
from crm_style.new_create3D import *
from driver.driver import *
import traceback
from crm_style.erp_process import *
from crm_style.simple_case_1 import *
from libs.simple_case import *
from random import choice
from libs.create_3d import to_get_casecode
from libs.create_3d import open_patient_detail
from libs.keywords_trans import  check_loading_is_hide
from libs.keywords_trans import  assert_text_handler_1

import datetime
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
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
            #将目标位改为全设计
            self.driver.find_element_by_id('edit_button').click()
            #点击病例类别
            Select(self.driver.find_element_by_id('case_type_c')).select_by_value('6')
            # 点击客服负责人X
            self.driver.find_element_by_id('btn_clr_customer_service_manager_c').click()
            # 输入客服负责人
            self.driver.find_element_by_id("customer_service_manager_c").send_keys('客服小蔡')
            #点击保存
            self.driver.find_element_by_id('SAVE_HEADER').click()
            sleep(5)
            self.driver.find_element_by_css_selector("#pause_tasks_open").click()
            self.driver.switch_to.window(get_handles(self.driver)[1])
            uploadStlAndDdm(self.driver, ods, phase=None)
            self.driver.switch_to.window(get_handles(self.driver)[0])
            dsignScheme(self.driver)
            self.driver.switch_to.window(get_handles(self.driver)[1])
            uploadOds(self.driver, ods, phase=None)
            self.driver.switch_to.window(get_handles(self.driver)[0])
            # Filling_steps(self.driver)
            submit3d(self.driver)
        except Exception as e:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，\033[0m" % (self.caseid) + "\n")
            traceback_info = traceback.format_exc()
            print(traceback_info)
            print('创建3d失败，失败原因：',e)
    def test_create3D_1(self,g_config):
        timex_list= []

        i=0
        while i<65:
            timex_dict = {"time": "", "isSuccess": ""}
            url=r'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
            i=i+1
            login_iortho(self.driver, "qinmd8888","111111",url)
            stand(self.driver, g_config)
            sleep(70)
            casecode=to_get_casecode(self.driver,url)
            ods=rename_file_1(casecode,i)
            print(">>>开始登录crm，请耐心等候......" + "\n")
            Login_1(self.driver,self.url,self.username,self.password)
            try:
                searchPatient_1(self.driver, casecode)
                self.driver.find_element_by_css_selector("#pause_tasks_open").click()
                self.driver.switch_to.window(get_handles(self.driver)[3])
                uploadStlAndDdm(self.driver, ods, phase=None)
                self.driver.switch_to.window(get_handles(self.driver)[2])
                dsignScheme(self.driver)
                self.driver.switch_to.window(get_handles(self.driver)[3])
                uploadOds(self.driver, ods, phase=None)
                self.driver.switch_to.window(get_handles(self.driver)[2])
                # Filling_steps(self.driver)
                submit3d(self.driver)
                sleep(70)

                open_patient_detail(self.driver, "https://opm-cas.sh-sit.eainc.com:8443/OPM/#/workbench", from_state=None)
                check_loading_is_hide(self.driver)

                #打印当前时间
                starttime = datetime.datetime.now()
                print(starttime)
                # 点击web
                web_selector = "#root-route > ui-view > page-patient > div > ui-view > page-patient-detail > div > ui-view > patient-detail-content > div.detail-panel.layout-col > div.detail-content.layout-row.layout-nowrap > div.detail-timezone-right > div:nth-child(2) > div.detail-timezone-body.layout-col.ng-scope > timezone > div > div.timezone-item.ng-scope.has-icon-3d > div.timezone-item-body > div > div.mes-btn > timezone-input > div:nth-child(4)"
                self.driver.find_element_by_css_selector(web_selector).click()
                #切换至当前窗口
                self.driver.switch_to.window(get_handles(self.driver)[6])
                #失败判断元素
                a='//*[@id="ID_APP_NOTICE"]/div/div/div[2]/button'
                #查看3D按钮元素定位
                b='#ID_APP_ROOT > div > div:nth-child(2) > div > div > a > div._8bafe75b103f9abc > div.bfb02a8248b87a45'
                #点击查看方案，断言失败弹框是否存在，1存在
                try:
                    if assert_text_handler_1(self.driver, a, '确定', '查看是否有确定按钮')==2:

                        print("方案打开成功")
                    elif assert_text_handler_1(self.driver, a, '确定', '查看是否有确定按钮')==1:
                        print("方案报错")
                        timex_dict['isSuccess']='失败'

                except:
                    print("没有断言")
                    locator = (By.CSS_SELECTOR, b)
                    WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                    self.driver.find_element_by_css_selector(b).click()
                    timex_dict['isSuccess'] = '成功'

                endtime = datetime.datetime.now()
                print(endtime)
                timex = (endtime - starttime).seconds
                print(timex)
                timex_dict['time'] = timex
                timex_list.append(timex_dict)
                print(i)
                print(timex_list)

            except:

                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，\033[0m" % (self.caseid) + "\n")
                traceback_info = traceback.format_exc()
                print(traceback_info)
                # i= i - 1
                print(i)


            self.driver.quit()
            self.driver = browser()
        print(timex_list)
        cg=0
        sb=0
        for tj in timex_list:
            if tj['isSuccess']=='失败':
                sb=sb+1
            else:
                cg=cg+1
        print("成功的个数:"+str(cg),"失败的个数:"+str(sb))

    def test_create3D_3(self,g_config):
        timex_list= []

        names = ["温荣司","空平门","沙宋阚"]
        for name in names :
            timex_dict = {"time": "", "isSuccess": ""}
            url=r'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
            login_iortho(self.driver, "qinmd8888","111111",url)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/input").send_keys(name)
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div[2]/div[1]/div/div/div").click()
            handles = self.driver.window_handles

            self.driver.switch_to_window(handles[-1])
            # stand(self.driver, g_config)
            # sleep(70)
            # casecode=to_get_casecode(self.driver,url)
            # ods=rename_file_1(casecode,i)
            # print(">>>开始登录crm，请耐心等候......" + "\n")
            # Login_1(self.driver,self.url,self.username,self.password)
            # try:
            #     searchPatient_1(self.driver, casecode)
            #     self.driver.find_element_by_css_selector("#pause_tasks_open").click()
            #     self.driver.switch_to.window(get_handles(self.driver)[3])
            #     uploadStlAndDdm(self.driver, ods, phase=None)
            #     self.driver.switch_to.window(get_handles(self.driver)[2])
            #     dsignScheme(self.driver)
            #     self.driver.switch_to.window(get_handles(self.driver)[3])
            #     uploadOds(self.driver, ods, phase=None)
            #     self.driver.switch_to.window(get_handles(self.driver)[2])
            #     # Filling_steps(self.driver)
            #     submit3d(self.driver)
            #     sleep(70)

            # open_patient_detail(self.driver, "https://opm-cas.sh-sit.eainc.com:8443/OPM/#/workbench", from_state=None)
            check_loading_is_hide(self.driver)

            #打印当前时间
            starttime = datetime.datetime.now()
            print(starttime)
                # 点击web
            web_selector = "#root-route > ui-view > page-patient > div > ui-view > page-patient-detail > div > ui-view > patient-detail-content > div.detail-panel.layout-col > div.detail-content.layout-row.layout-nowrap > div.detail-timezone-right > div:nth-child(2) > div.detail-timezone-body.layout-col.ng-scope > timezone > div > div.timezone-item.ng-scope.has-icon-3d > div.timezone-item-body > div > div.mes-btn > timezone-input > div:nth-child(4)"
            self.driver.find_element_by_css_selector(web_selector).click()
                #切换至当前窗口
            self.driver.switch_to.window(get_handles(self.driver)[2])
                #失败判断元素
            a='//*[@id="ID_APP_NOTICE"]/div/div/div[2]/button'
                #查看3D按钮元素定位
            b='#ID_APP_ROOT > div > div:nth-child(2) > div > div > a > div._8bafe75b103f9abc > div.bfb02a8248b87a45'
                #点击查看方案，断言失败弹框是否存在，1存在
            try:
                if assert_text_handler_1(self.driver, a, '确定', '查看是否有确定按钮','')==2:

                    print("方案打开成功")
                elif assert_text_handler_1(self.driver, a, '确定', '查看是否有确定按钮','')==1:
                    print("方案报错")
                    timex_dict['isSuccess']='失败'

            except:
                print("没有断言")
                locator = (By.CSS_SELECTOR, b)
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
                self.driver.find_element_by_css_selector(b).click()
                timex_dict['isSuccess'] = '成功'

            endtime = datetime.datetime.now()
            print(endtime)
            timex = (endtime - starttime).seconds
            print(timex)
            timex_dict['time'] = timex
            timex_list.append(timex_dict)
            # print(i)
            print(timex_list)

            # except:
            #
            #     print("\033[31m注意 ：病例号为 %s的病例创建3D失败，\033[0m" % (self.caseid) + "\n")
            #     traceback_info = traceback.format_exc()
            #     print(traceback_info)
            #     # i= i - 1
            #     print(i)


            self.driver.quit()
            self.driver = browser()
        print(timex_list)
        cg=0
        sb=0
        for tj in timex_list:
            if tj['isSuccess']=='失败':
                sb=sb+1
            else:
                cg=cg+1
        print("成功的个数:"+str(cg),"失败的个数:"+str(sb))




    def test_create3D_2(self,g_config):

        i=0
        while i<5:

            url=r'https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
            i=i+1
            login_iortho(self.driver, "qinmd8888","111111",url)
            stand(self.driver, g_config)
            sleep(70)
            casecode=to_get_casecode(self.driver,url)
            ods = rename_file(casecode, get_dir())
            print(">>>开始登录crm，请耐心等候......" + "\n")
            Login_1(self.driver, self.url, "shihm", "123456")
            try:
                searchPatient_1(self.driver, casecode)
                # 将目标位改为全设计
                self.driver.find_element_by_id('edit_button').click()
                # 点击病例类别
                Select(self.driver.find_element_by_id('case_type_c')).select_by_value('6')
                # 点击保存
                self.driver.find_element_by_id('SAVE_HEADER').click()
                sleep(1)
                self.driver.find_element_by_css_selector("#pause_tasks_open").click()
                self.driver.switch_to.window(get_handles(self.driver)[3])
                uploadStlAndDdm(self.driver, ods, phase=None)
                self.driver.switch_to.window(get_handles(self.driver)[2])
                dsignScheme(self.driver)
                self.driver.switch_to.window(get_handles(self.driver)[3])
                uploadOds(self.driver, ods, phase=None)
                self.driver.switch_to.window(get_handles(self.driver)[2])
                # Filling_steps(self.driver)
                submit3d(self.driver)
                print("创建成功")
            except:
                print("\033[31m注意 ：病例号为 %s的病例创建3D失败，\033[0m" % (self.caseid) + "\n")
                traceback_info = traceback.format_exc()
                print(traceback_info)
            sleep(30)
            self.driver.quit()
            self.driver = browser()






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
    def test_cbct_quality_conformance(self):
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
        print(self.caseid)
        database_manual_tooth_throwing(self.caseid)
        print('本地启动localservice，cds上传dtl照片2张，ddm文件一个（ 标准版上传单模）')
        # self.driver.find_element_by_css_selector("#pause_tasks_open").click()
        # self.driver.switch_to.window(get_handles(self.driver)[1])
        # uploadStlAndDdm(self.driver, ods, phase=None)
        # self.driver.switch_to.window(get_handles(self.driver)[0])
        # dsignScheme(self.driver)
        # self.driver.switch_to.window(get_handles(self.driver)[1])
        # uploadOds(self.driver, ods, phase=None)
        # self.driver.switch_to.window(get_handles(self.driver)[0])
        # t_opt = mainhandler.t_opt
        # dir_name = getOdsFile(t_opt.get("phase"), t_opt.get("type"), t_opt.get("update"))
        # logincrm_handler(mainhandler)
        # ods = rename_file(casecode, dir_name)
        # sleep(5)
        self.driver.close()
        Login_1(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        key_trans.switch_to_cur_win(self.driver, lambda: self.driver.find_element_by_css_selector("#pause_tasks_open").click())
        ods = rename_file(self.caseid, get_dir())
        uploadStlAndDdm(self.driver, ods)
        dsignScheme(self.driver)
        uploadOds(self.driver, ods)
        acceptAlert(self.driver)
        sleep(1000)
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
        connect_to_the_database(ordnumber)

        login_erp(self.driver)
        put_in_storage(self.driver,ordnumber)
        sleep(3)
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
    def test_child_K1(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child_K1(self.driver, g_config)
    def test_child_champion(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child_champion(self.driver, g_config)

    def test_child_champion_A6(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        child_champion_A6(self.driver, g_config)

    def test_comfos(self, g_config):
        login_iortho(self.driver, self.i_username, self.i_password, self.i_url)
        comfos(self.driver, g_config)

def test_create_makeit_3shape_api(g_config):
    a=0
    b=0
    while a<get_caseNum():
        a = a + 1
        try:
            if create_makeit_api(g_config)== True:
                b=b+1
        except:
            traceback_info = traceback.format_exc()
            print(traceback_info)
            pass
        print("#########################分隔线################################")
        sleep(get_Waitingtime())
    print("共创建的案例个数:%d"%get_caseNum())
    print("创建失败的案例个数：%d"%(get_caseNum()-b))
    # print("微笑模拟成功的个数：%d"%c)
    # print('自动化排牙成功率: {:.2f}%'.format(get_caseNum()-b/get_caseNum()*100))
    # print('微笑模拟成功率: {:.2f}%'.format(c/b*100))

def test_create_makeit_stl_api(g_config):
    a=0
    b=0
    while a<get_caseNum():
        a = a + 1
        try:
            if create_makeit_stl(g_config)== True:
                b=b+1
        except:
            traceback_info = traceback.format_exc()
            print(traceback_info)
            pass
        print("#########################分隔线################################")
        sleep(get_Waitingtime())
    print("共创建的案例个数:%d"%get_caseNum())
    print("创建失败的案例个数：%d"%(get_caseNum()-b))

def run(username,password,url,institutions,doctorname,i_username,i_password,i_url,g_config):
    while True:
        if get_num() == "3d":
            Create3D(username, password, url).test_create3D()
            break
        elif get_num() == "3d_1":
            Create3D(username, password, url).test_create3D_1(g_config)
            break
        elif get_num() == "3d_3":
            Create3D(username, password, url).test_create3D_3(g_config)
            break
         #循环造3D，但不打开
        elif get_num() == "3d_2":
            Create3D(username, password, url).test_create3D_2(g_config)
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
        elif get_num() == "儿童K1":
            Create_New_Case(i_username,i_password,i_url).test_child_K1(g_config)
            break
        elif get_num() == "儿童加冠军":
            Create_New_Case(i_username,i_password,i_url).test_child_champion(g_config)
            break
        elif get_num() == "儿童加冠军A6":
            Create_New_Case(i_username,i_password,i_url).test_child_champion_A6(g_config)
            break
        elif get_num() == "comfos":
            Create_New_Case(i_username,i_password,i_url).test_comfos(g_config)
            break
        elif get_num() == "makeit_3shape":
            test_create_makeit_3shape_api(g_config)
            break
        elif get_num() == "makeit_stl":
            test_create_makeit_stl_api(g_config)
            break
        elif get_num() == "cbct质检不合格":
            Create3D(username, password, url).test_cbct_quality_conformance()
            break
        else:
            print("指令格式不正确，请重新输入")
            break
