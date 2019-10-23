from selenium.webdriver.support.ui import Select
from time import sleep
from ThreeDimensional_Project.website.test_case.model.function import *




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