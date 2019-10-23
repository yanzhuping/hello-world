#新建标准版的加工单

def NewWorksheet(driver):
    driver.find_element_by_id("mainsuit0").click()
    driver.find_element_by_id("treatTarget0").click()
    driver.find_element_by_id("treatTooth1").click()
    driver.find_element_by_id("facetype1").click()
    driver.find_element_by_id("sagittalRight1").click()
    driver.find_element_by_id("sagittalLeft1").click()
    driver.find_element_by_id("midline2").click()
    driver.find_element_by_id("antinail1").click()
