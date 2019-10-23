from selenium.webdriver.support.ui import Select

from website.test_case.models.function import *


def dsignScheme(driver):
    # 设计方案
    # driver.find_element_by_xpath(
    #     '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    # sleep(1.5)
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_design_1_创建_button"]').click()
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

    # 再次切回CDS
