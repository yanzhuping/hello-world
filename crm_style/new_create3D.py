#重构3d创建方法，代码更简洁
from crm_style.function import *
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

def login_iortho(driver,username,password,url):
    print("执行登录")
    '''登陆iortho'''
    driver.get(url)
    # driver.switch_to.frame("the-real-login-page")
    driver.find_element_by_id("_username").clear()
    driver.find_element_by_id("_username").send_keys(username)
    driver.find_element_by_id("_password").clear()
    driver.find_element_by_id("_password").send_keys(password)
    driver.find_element_by_id("_btn_login").click()
    sleep(2)

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
        sleep(2)
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
        try:
            # sit环境
            driver.find_element_by_xpath('//span[@id="picker"]/div[2]/input').send_keys(photo_list[0])
            driver.find_element_by_xpath('//span[@id="picker"]/div[2]/input').send_keys(photo_list[1])
            sleep(3)
            driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[1]').click()
            driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[3]/button').click()
        except:
            # adv
            driver.find_element_by_id('ddmType').send_keys(photo_list[0])
            driver.find_element_by_id('ddmType').send_keys(photo_list[1])
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
            print("adv环境cds上传stl")

        sleep(2)
        # 上传DDM文件
        #点击ddm上传
        driver.find_element_by_xpath('//*[@id="DDM"]/div[1]/h4/a/span[1]').click()
        #点击上传
        driver.find_element_by_xpath('//*[@id="collapse_3_4"]/div/a[1]').click()
        sleep(2)
        # 先删除上传的stl记录

        #sit
        try:
            driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[2]').click()
            sleep(1)
            driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['ddm'])
            sleep(2)
            driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[1]').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[3]/button').click()
        #adv
        except:
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/span[2]').click()
            sleep(1)
            driver.find_element_by_id('ddmType').send_keys(ods[0])
            sleep(2)
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
            print('adv','上传ddm')
        break

def dsignScheme(driver):
    '''设计3D方案'''
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    sleep(1.5)
    # driver.find_element_by_xpath('//*[@id="ea_stage_ea_design_1_创建_button"]').click() #无头模式下该按钮无法点击
    js = "var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    sleep(2)
    driver.find_element_by_id('ea_stage_ea_design_1_创建_button').click()#加一个拖动
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
        driver.find_element_by_css_selector("#i18n_historyshow_3Ddesign").click()
        driver.find_element_by_css_selector("#ODSTitle>ul>li:last-child").click()
    driver.find_element_by_css_selector(".ODSSolutionBody>div:last-child .ODSSolutionBodyFoot button").click()
    sleep(2)
    try:
        driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['ods'])
        sleep(0.5)
        driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['json'])
        sleep(0.5)
        driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['doc'])
        sleep(0.5)
        # driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['v6_ods'])
        sleep(6)
        driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[3]/button').click()
        sleep(2)
    except:
        driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['ods'])
        sleep(0.5)
        driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['json'])
        sleep(0.5)
        driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['doc'])
        sleep(0.5)
        #{Alert text : 3D设计文件(V6)必须是v6ods文件(文件名中不能含有改类型、磨除关键字)}
        # driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['v6_ods'])
        sleep(6)
        driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="ODSUploadModal"]/div[3]/button').click()
        sleep(2)
        print('adv ods文件上传')

def acceptAlert(driver):
    '''有时候有多个alert连续存在'''
    i=0
    while i<3:
        i=i+1
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            if alert:
                alert.accept()
        except:
            pass
        sleep(0.5)

def submit3d(driver):
    driver.find_element_by_css_selector("#operation").click()
    acceptAlert(driver)
    driver.find_element_by_css_selector("#do_submit").click()
    acceptAlert(driver)
    driver.find_element_by_css_selector("#send_design").click()
    acceptAlert(driver)
    sleep(3)
    planstatus=driver.find_element_by_xpath('//*[@id="state_c"]/..').text
    print('方案状态为:',planstatus)
    if planstatus == '已发送':
        print("方案创建成功")
    else:
        raise Exception('创建失败')

def Filling_steps(driver):
    #点击编辑
    driver.find_element_by_css_selector("#edit_button").click()
    sleep(1.5)
    #分步
    driver.find_element_by_css_selector("#upper_jaw_step_begin_c").send_keys("2")
    sleep(1)
    driver.find_element_by_css_selector("#upper_jaw_step_c").send_keys("20")
    sleep(1)

    driver.find_element_by_css_selector("#upper_jaw_step_more_c").send_keys("2")
    sleep(1)

    driver.find_element_by_css_selector("#lower_jaw_step_begin_c").send_keys("2")
    sleep(1)

    driver.find_element_by_css_selector("#lower_jaw_step_c").send_keys("20")
    sleep(1)
    driver.find_element_by_css_selector("#lower_jaw_step_more_c").send_keys("2")
    sleep(1)
    #点击保存
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    sleep(3)