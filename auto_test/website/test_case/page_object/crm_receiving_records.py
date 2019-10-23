#查找收货记录


from time import sleep

from website.test_case.models.function import pageDown


def receivingRecords(driver):
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    sleep(1.5)
    pageDown(driver)

