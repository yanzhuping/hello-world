#crm中相关的一些功能集合
from selenium.webdriver.support.ui import Select
import libs.keywords_trans as key_trans
from time import sleep
import random

def unqualified_quality_inspection(driver):
    '''质检不合格'''
    driver.find_element_by_css_selector("#ea_case_ea_tasks_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#category_c")).select_by_value("110000")
    Select(driver.find_element_by_css_selector("#type_c")).select_by_value("1101a1")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#no_qualified_tasks").click()
    key_trans.switch_to_win(driver, 1)
    Select(driver.find_element_by_css_selector("#pause_reason_list2")).select_by_value("3")
    driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(key_trans.get_root_path()+"/test_data/QC_Report.doc")
    driver.find_element_by_xpath('/html/body/form/input[5]').click()
    driver.switch_to.alert.accept()
    sleep(2)
    key_trans.switch_to_cur_win(driver)

def quality_inspection_qualified(driver):
    '''质检合格'''
    driver.find_element_by_css_selector("#ea_case_ea_tasks_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#category_c")).select_by_value("110000")
    Select(driver.find_element_by_css_selector("#type_c")).select_by_value("1101a1")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#qualified_tasks").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/th[1]/input').get_attribute("tooth_bit_18")
    driver.find_element_by_xpath('/html/body/form/input[2]').click()
    driver.switch_to.alert.accept()
    sleep(3)

def create_No_Treatment(driver):
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

def create_Word_scheme(driver):
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

def finish_phase(driver):
    '''结束当前病例的阶段'''
    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    driver.find_element_by_css_selector("#ea_case_ea_stage_1_edit_1").click()
    Select(driver.find_element_by_css_selector("#is_produce_c")).select_by_value("1")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)

def offline_new_guijiao(driver,patientname,institutions,doctorname):
    '''线下硅胶新病例'''
    sleep(5)
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#accounts_c").send_keys(institutions)
    driver.find_element_by_css_selector("#contacts_c").send_keys(doctorname)
    driver.find_element_by_css_selector("#btn_patients_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_xpath('//*[@id="addformlink"]/input').click()
    driver.find_element_by_css_selector("#name").send_keys(patientname)
    driver.find_element_by_css_selector("#ea_patients_popupcreate_save_button").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    key_trans.switch_to_cur_win(driver)
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    select = Select(driver.find_element_by_css_selector("#express_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#barcode_u_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#barcode_l_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(6)

def offline_new_photo(driver,patientname,institutions,doctorname):
    '''线下新病例口内照不合格'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#accounts_c").send_keys(institutions)
    driver.find_element_by_css_selector("#contacts_c").send_keys(doctorname)
    driver.find_element_by_css_selector("#btn_patients_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_xpath('//*[@id="addformlink"]/input').click()
    driver.find_element_by_css_selector("#name").send_keys(patientname)
    driver.find_element_by_css_selector("#ea_patients_popupcreate_save_button").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    key_trans.switch_to_cur_win(driver)
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("11")
    select = Select(driver.find_element_by_css_selector("#is_qualified_c"))
    select.select_by_value("2")
    driver.find_element_by_id("remark_c").send_keys("我觉得不合格，请重新上传")
    sleep(3)
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(5)
    driver.find_element_by_css_selector("#send_receipt").click()
    sleep(5)
    driver.switch_to.alert.accept()


def offline_middle_guijiao(driver ,crmusercode):
    '''线下中期硅胶'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    key_trans.switch_to_cur_win(driver)
    select =Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    select = Select(driver.find_element_by_css_selector("#express_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#barcode_u_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#barcode_l_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)

def offline_middle_photo(driver ,crmusercode):
    '''线下中期口内照'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    key_trans.switch_to_cur_win(driver)
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("11")
    select = Select(driver.find_element_by_css_selector("#is_qualified_c"))
    select.select_by_value("2")
    driver.find_element_by_id("remark_c").send_keys("中期口内照不合格，请重新上传")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    driver.find_element_by_css_selector("#send_receipt").click()
    sleep(4)
    driver.switch_to.alert.accept()