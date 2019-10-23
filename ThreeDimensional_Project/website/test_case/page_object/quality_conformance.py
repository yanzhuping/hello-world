from selenium.webdriver.support.ui import Select
from time import sleep
from ThreeDimensional_Project.website.test_case.model.function import *



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