from time import sleep


def uploadToothModel(driver):
    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    sleep(2)
    # driver.find_element_by_xpath(
    #     u"(.//*[normalize-space(text()) and normalize-space(.)='数字模型文件'])[1]/following::label[1]").click()
    # driver.find_element_by_xpath(
    #     u"(.//*[normalize-space(text()) and normalize-space(.)='上颌'])[1]/following::label[1]").click()
    # driver.find_element_by_id("uploadFile_stl_0").clear()
    # driver.find_element_by_id("uploadFile_stl_0").send_keys(r"C:\Users\Administrator\Desktop\photos\001.jpg")
    # driver.find_element_by_xpath(
    #     u"(.//*[normalize-space(text()) and normalize-space(.)='下颌'])[1]/following::label[1]").click()
    # driver.find_element_by_id("uploadFile_stl_1").clear()
    # driver.find_element_by_id("uploadFile_stl_1").send_keys(r"C:\Users\Administrator\Desktop\photos\001.jpg")
    driver.find_element_by_id("hasSilicon1").click()
