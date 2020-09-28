#重构3d创建方法，代码更简洁
from crm_style.function import *
from time import sleep
from selenium.webdriver.support.select import Select

def Login_1(driver,base_url,username,password):
    '''登录crm'''
    try:
        driver.set_page_load_timeout(15)
        driver.get(base_url)
    except:
        driver.execute_script("window.stop()")
    driver.find_element_by_css_selector("#username").send_keys(username)
    driver.find_element_by_css_selector("#password").send_keys(password)
    driver.find_element_by_css_selector(".btn-submit").click()

def searchPatient_1(driver,id):
    '''查找病例'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("病例").click()
    while True:
        try:
            # 搜索患者
            driver.find_element_by_xpath('//*[@id="ea_patients_ea_case_1_name_basic"]').clear()
            driver.find_element_by_css_selector("#accounts_ea_case_1_name_basic").clear()
            driver.find_element_by_css_selector("#contacts_ea_case_1_name_basic").clear()
            driver.find_element_by_css_selector("#name_basic").clear()
            driver.find_element_by_css_selector("#name_basic").send_keys(id)
            driver.find_element_by_css_selector("#search_form_submit").click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[4]/b/a').click()
            break
        except:
            print("搜索失败，切换搜索模式")
            driver.find_element_by_id('basic_search_link').click()

def uploadStlAndDdm(driver, ods, phase=None):
    '''上传咬合stl文件、ddm文件'''
    # driver.refresh()
    sleep(2)
    driver.switch_to.frame("otherPage")
    if phase is None:
        phase_ele = driver.find_element_by_css_selector(".todo-tasklist-list:last-child")
    else:
        phase_ele = driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div' % phase)
    photo_list = choice_file("photo")
    i = 0
    while i < 3:
        i = i+1
        phase_ele.click()
        # 上传咬合stl
        driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
        driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
        sleep(1)
        driver.find_element_by_css_selector("#ddmType").send_keys(photo_list[0])
        driver.find_element_by_css_selector("#ddmType").send_keys(photo_list[1])
        driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
        sleep(2)
        # 上传DDM文件

        # driver.find_element_by_css_selector(".i18n_historyshow_ddm").click()
        driver.find_element_by_css_selector("#DDM > div.panel-head-type > h4 > a > span.i18n_historyshow_ddm").click()

        driver.find_element_by_xpath('//*[@id="collapse_3_4"]/div/a[1]').click()
        sleep(2)
        driver.find_element_by_css_selector("#ddmType").send_keys(ods[0])
        sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
        except:
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
        sleep(2)
        break

def dsignScheme(driver):
    '''设计3D方案'''
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_design_1_创建_button"]').click()
    sleep(2)
    select = Select(driver.find_element_by_css_selector("#jaw_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#case_design_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#difficulty_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#design_type_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    sleep(1)
    try:
        driver.switch_to.alert.accept()
        driver.find_element_by_css_selector("#SAVE_HEADER").click()
        driver.switch_to.alert.accept()
    except:
        pass

def uploadOds(driver, ods, phase=None):
    '''上传ods四个文件'''
    driver.refresh()
    sleep(2)
    driver.switch_to.frame("otherPage")
    sleep(1.5)
    if phase is None:
        phase_ele = driver.find_element_by_css_selector(".todo-tasklist-list:last-child")
    else:
        phase_ele = driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div' % phase)
    phase_ele.click()
    sleep(1)
    phase_ele.click()
    sleep(1)
    try:
        driver.find_element_by_css_selector("#i18n_historyshow_3Ddesign").click()
        driver.find_element_by_css_selector("#ODSTitle>ul>li:last-child").click()
    except:
        driver.find_element_by_css_selector("#i18n_historyshow_3Ddesign").click()   #这是因为文件上传失败了，点进去找不到文件
        driver.find_element_by_css_selector("#ODSTitle>ul>li:last-child").click()
    driver.find_element_by_css_selector(".ODSSolutionBody>div:last-child .ODSSolutionBodyFoot button").click()
    sleep(2)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[1])
    sleep(0.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[2])
    sleep(0.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[3])
    sleep(0.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[4])
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="ODSUploadModal"]/div[3]/button').click()

def acceptAlert(driver):
    '''同步。处理弹窗、提交、发送'''
    driver.find_element_by_css_selector("#operation").click()
    driver.switch_to.alert.accept()
    sleep(3)
    try:
        driver.switch_to.alert.accept()
        sleep(1.5)
        try:
            driver.switch_to.alert.accept()
            sleep(1.5)
        except:
            pass
    except:
        pass
    driver.find_element_by_css_selector("#do_submit").click()
    driver.switch_to.alert.accept()
    sleep(3)
    driver.switch_to.alert.accept()
    sleep(3)
    driver.find_element_by_css_selector("#send_design").click()
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    sleep(3)