from selenium.webdriver.support.ui import Select
from time import sleep
from CRM_Style.website.test_case.model.function import *


def offline_new_photo(driver,patientname,institutions,doctorname):
    '''线下新病例口内照不合格'''
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