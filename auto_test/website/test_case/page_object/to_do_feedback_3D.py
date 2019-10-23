#对3D方案进行意见反馈

from time import sleep

def toDoFeedback3D(driver):

    #加载页的播放按钮
    driver.find_element_by_class_name('icon__11943b9').click()
    sleep(3)
    #提交修改意见
    # driver.find_element_by_xpath(
    #     '//*[@id="__APPLICATION_ROOT__"]/div/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/a').click()
    driver.find_element_by_xpath("//a[@class='linear-button__0ca0ac6' and text()='提交修改意见']").click()
    driver.find_element_by_class_name('feedback-textarea__6fc21c2').send_keys("通过自动化脚本提交修改意见…………")
    driver.find_element_by_class_name('linear-button__dd76270').click()





