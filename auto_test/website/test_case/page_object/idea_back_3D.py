#当前阶段的已经批准的3D方案意见回传
from time import sleep
def ideaBack3D(driver):
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    sleep(1.5)
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_stage_ea_design_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_id('idea_back').click()
    driver.switch_to.alert.accept()
    driver.find_element_by_id('ea_case_id_c').click()
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_id('no_modified_tasks').click()
    driver.switch_to.alert.accept()
    sleep(40)

