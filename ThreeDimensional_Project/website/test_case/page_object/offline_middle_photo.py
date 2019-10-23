from selenium.webdriver.support.ui import Select
from time import sleep
from ThreeDimensional_Project.website.test_case.model.function import *

def offline_middle_photo(driver ,crmusercode):

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