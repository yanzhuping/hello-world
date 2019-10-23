from selenium.webdriver.support.ui import Select
from time import sleep
from ThreeDimensional_Project.website.test_case.model.function import *

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