from time import sleep
from CRM_Style.website.test_case.model.function import *

def searchPatient(driver,id):
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("病例").click()

    while True:
        try:
            # 搜索患者
            driver.find_element_by_xpath('//*[@id="ea_patients_ea_case_1_name_basic"]').clear()
            driver.find_element_by_css_selector("#accounts_ea_case_1_name_basic").clear()
            driver.find_element_by_css_selector("#contacts_ea_case_1_name_basic").clear()
            driver.find_element_by_css_selector("#name_basic").clear()
            driver.find_element_by_css_selector("#name_basic").send_keys(id)
            driver.find_element_by_css_selector("#search_form_submit").click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[4]/b/a').click()
            break
        except:
            print("搜索失败，切换搜索模式")
            driver.find_element_by_id('basic_search_link').click()


    driver.find_element_by_css_selector("#pause_tasks_open").click()

    driver.switch_to.window(get_handles(driver)[0])

