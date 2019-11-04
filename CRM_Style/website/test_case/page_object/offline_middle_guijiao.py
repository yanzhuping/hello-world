from CRM_Style.website.test_case.model.function import *
from selenium.webdriver.support.ui import Select
from time import sleep

def offline_middle_guijiao(driver ,crmusercode):

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