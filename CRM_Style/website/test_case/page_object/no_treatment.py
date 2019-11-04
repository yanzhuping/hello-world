from selenium.webdriver.support.ui import Select
from time import sleep

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