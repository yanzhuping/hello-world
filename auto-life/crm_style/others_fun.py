from selenium.webdriver.support.ui import Select
from time import sleep
from crm_style.function import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def Create_Quality_Conformance(driver):
    '''质检不合格'''
    driver.find_element_by_css_selector("#ea_case_ea_tasks_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#category_c")).select_by_value("110000")
    Select(driver.find_element_by_css_selector("#type_c")).select_by_value("1101a1")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#no_qualified_tasks").click()
    driver.switch_to.window(get_handles(driver)[1])
    Select(driver.find_element_by_css_selector("#pause_reason_list2")).select_by_value("3")
    driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(get_fileBasePath()+"/test_data/QC_Report.doc")
    driver.find_element_by_xpath('/html/body/form/input[5]').click()
    driver.switch_to.alert.accept()
    sleep(4)
    driver.quit()

def Create_Quality_Reject(driver):
    '''质检合格'''
    driver.find_element_by_css_selector("#ea_case_ea_tasks_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#category_c")).select_by_value("110000")
    Select(driver.find_element_by_css_selector("#type_c")).select_by_value("1101a1")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#qualified_tasks").click()
    driver.switch_to.window(get_handles(driver)[1])
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/th[1]/input').get_attribute("tooth_bit_18")
    driver.find_element_by_xpath('/html/body/form/input[2]').click()
    driver.switch_to.alert.accept()
    sleep(3)
    driver.quit()

def Create_Word_scheme(driver):
    '''文字方案'''

    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#ea_stage_ea_proposal_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#difficulty_c")).select_by_value("3")
    Select(driver.find_element_by_css_selector("#jaw_c")).select_by_value("3")
    driver.find_element_by_css_selector("#forecast_upper_jaw_step_c").send_keys("10")
    driver.find_element_by_css_selector("#forecast_low_jaw_step_c").send_keys("10")
    driver.find_element_by_css_selector("#quote_c").send_keys("1000")
    driver.find_element_by_css_selector("#conformation_price_c").send_keys("10000")

    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_css_selector("#do_submit").click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()
    sleep(4)
    driver.quit()

def Create_No_Treatment(driver):
    '''不收治'''
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#ea_stage_ea_proposal_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#treated_diagnosis_c")).select_by_value("2")
    Select(driver.find_element_by_css_selector("#difficulty_c")).select_by_value("3")
    Select(driver.find_element_by_css_selector("#jaw_c")).select_by_value("3")
    driver.find_element_by_css_selector("#not_treated_c").send_keys("此病例难治乎，撤！！！")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_css_selector("#do_submit").click()
    driver.switch_to.alert.accept()
    driver.switch_to.alert.accept()
    sleep(4)
    driver.quit()

def finish_phase(driver):
    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)

    driver.find_element_by_css_selector("#ea_case_ea_stage_1_edit_1").click()
    Select(driver.find_element_by_css_selector("#is_produce_c")).select_by_value("1")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)

def offline_new_guijiao(driver,patientname,institutions,doctorname):
    '''线下硅胶新病例'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#accounts_c").send_keys(institutions)
    driver.find_element_by_css_selector("#contacts_c").send_keys(doctorname)
    driver.find_element_by_css_selector("#btn_patients_c").click()

    driver.switch_to.window(get_handles(driver)[1])
    driver.find_element_by_xpath('//*[@id="addformlink"]/input').click()
    driver.find_element_by_css_selector("#name").send_keys(patientname)
    driver.find_element_by_css_selector("#ea_patients_popupcreate_save_button").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    driver.switch_to.window(get_handles(driver)[0])
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    select = Select(driver.find_element_by_css_selector("#express_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#barcode_u_c").send_keys(randomValue()[0])
    driver.find_element_by_css_selector("#barcode_l_c").send_keys(randomValue()[1])
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)
    driver.quit()

def offline_new_photo(driver,patientname,institutions,doctorname):
    '''线下新病例口内照'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#accounts_c").send_keys(institutions)
    driver.find_element_by_css_selector("#contacts_c").send_keys(doctorname)
    driver.find_element_by_css_selector("#btn_patients_c").click()
    driver.switch_to.window(get_handles(driver)[1])
    driver.find_element_by_xpath('//*[@id="addformlink"]/input').click()
    driver.find_element_by_css_selector("#name").send_keys(patientname)
    driver.find_element_by_css_selector("#ea_patients_popupcreate_save_button").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    driver.switch_to.window(get_handles(driver)[0])
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("11")
    select = Select(driver.find_element_by_css_selector("#is_qualified_c"))
    select.select_by_value("2")
    driver.find_element_by_id("remark_c").send_keys("口内照不合格，请重新上传")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    driver.find_element_by_css_selector("#send_receipt").click()
    sleep(4)
    driver.quit()

def reeceiving_records(driver ,crmusercode):
    '''创建收获记录'''
    driver.find_element_by_link_text("病例管理").click()
    # driver.find_element_by_xpath('//*[@id="moduleList"]/ul/li[2]/span[2]').click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    driver.switch_to.window(handles[0])
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    # select = Select(driver.find_element_by_css_selector("#express_type_c"))
    # select.select_by_value("3")
    # select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    # select.select_by_value("1")
    # driver.find_element_by_css_selector("#barcode_u_c").send_keys(randomValue()[0])
    # driver.find_element_by_css_selector("#barcode_l_c").send_keys(randomValue()[1])
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    sleep(4)
    driver.find_element_by_id('ea_case_id_c').click()
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_id('no_qualified_tasks').click()
    driver.switch_to.window(driver.window_handles[1])
    Select(driver.find_element_by_css_selector("#pause_reason_list")).select_by_value("1501")
    Select(driver.find_element_by_css_selector("#pause_reason_list2")).select_by_value("3")
    driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(get_fileBasePath() + "/test_data/QC_Report.doc")
    driver.find_element_by_xpath('/html/body/form/input[5]').click()
    driver.switch_to.alert.accept()
    sleep(4)
    driver.quit()


def offline_middle_guijiao(driver ,crmusercode):
    '''线下中期硅胶'''
    driver.find_element_by_link_text("病例管理").click()
    # driver.find_element_by_xpath('//*[@id="moduleList"]/ul/li[2]/span[2]').click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    driver.switch_to.window(handles[0])
    select =Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    select = Select(driver.find_element_by_css_selector("#express_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#barcode_u_c").send_keys(randomValue()[0])
    driver.find_element_by_css_selector("#barcode_l_c").send_keys(randomValue()[1])
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)
    driver.quit()

def offline_middle_photo(driver ,crmusercode):
    '''线下中期口内照'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    driver.switch_to.window(get_handles(driver)[1])
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    driver.switch_to.window(get_handles(driver)[0])
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("11")
    select = Select(driver.find_element_by_css_selector("#is_qualified_c"))
    select.select_by_value("2")
    driver.find_element_by_id("remark_c").send_keys("口内照不合格，请重新上传")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    driver.find_element_by_css_selector("#send_receipt").click()
    sleep(4)
    driver.quit()

def get_element(driver, selector, is_immedite=None):
    check_loading_is_hide(driver)
    wait = WebDriverWait(driver, 15, 0.5)
    text = None
    # 支持选择器中带文本 比如：div>span[text]=病例 正常选择器中是没有这种写法的
    if selector.find("[text]=") > -1:
        selector, text = selector.split("[text]=")
    if selector.startswith("/"):
        if is_immedite:
            elements = driver.find_elements_by_xpath(selector)
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, selector)))
    else:
        if is_immedite:
            elements = driver.find_elements_by_css_selector(selector)
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
    if len(elements) > 0 and text is not None:
        for ele in elements:
            if ele.text == text:
                return ele
        return None
    return elements[0] if elements is not None and len(elements) > 0 else None

# 检查有没有loading层覆盖 有的话等待loading消失
def check_loading_is_hide(driver):
    wait = WebDriverWait(driver, 40, 0.5)
    loading_ele = driver.execute_script("return document.querySelector('.iortho-global-loading')")
    percent_ele = driver.execute_script("return document.querySelector('#fileupload_loadingImg')")
    popover = driver.execute_script("return document.querySelector(\"[ng-show=\'$ctrl.popoverShow\']\")")
    if percent_ele is not None:
        wait.until(EC.staleness_of(percent_ele))
    if loading_ele is not None:
        wait.until(EC.staleness_of(loading_ele))
    if popover is not None:
        wait.until(EC.invisibility_of_element(popover))

def set_photo_disqualification(driver):
    '''设置照片不合格'''
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    sleep(1.5)
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_stage_ea_receipt_1"]/table/tbody/tr[2]/th[6]/span/a/img').click()
    i = 0
    while i < 2:
        img_ele = get_element(driver,
                                        "#list_subpanel_ea_stage_ea_receipt_1 tbody tr:nth-child(2)>th:nth-child(6) img")
        if img_ele.get_attribute("src").find("arrow_down.gif") == -1:
            img_ele.click()
        else:
            break
    link_ele = driver.execute_script(
        'var list=document.querySelectorAll("#list_subpanel_ea_stage_ea_receipt_1>table>tbody tr:nth-child(2)~tr");'
        'var link_ele;'
        'list.forEach(function(v){'
        'var first_td=v.firstElementChild;'
        'if(first_td.nextElementSibling.firstElementChild.innerText=="口内照"){'
        '    link_ele=first_td.firstElementChild.firstElementChild;'
        '}'
        '});'
        'return link_ele;'
        )
    link_ele.click()
    driver.find_element_by_id('edit_button').click()
    Select(driver.find_element_by_css_selector('#is_qualified_c')).select_by_value('2')
    driver.find_element_by_id("remark_c").send_keys("照片异常，请重新上传")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    driver.find_element_by_css_selector("#send_receipt").click()
    sleep(4)
    driver.quit()



