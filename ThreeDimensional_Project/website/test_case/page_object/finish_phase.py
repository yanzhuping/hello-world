from selenium.webdriver.support.ui import Select
from time import sleep


def finish_phase(driver,crmcasecode):
    '''结束当前病例的阶段'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("病例").click()

    # 搜索患者
    driver.find_element_by_xpath('//*[@id="ea_patients_ea_case_1_name_basic"]').clear()
    driver.find_element_by_css_selector("#accounts_ea_case_1_name_basic").clear()
    driver.find_element_by_css_selector("#contacts_ea_case_1_name_basic").clear()
    driver.find_element_by_css_selector("#name_basic").clear()
    driver.find_element_by_css_selector("#name_basic").send_keys(crmcasecode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[4]/b/a').click()

    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)

    driver.find_element_by_css_selector("#ea_case_ea_stage_1_edit_1").click()
    Select(driver.find_element_by_css_selector("#is_produce_c")).select_by_value("1")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)