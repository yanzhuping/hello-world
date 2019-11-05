#3D超时，重新上传方案，选择3shape上传
from time import sleep

def timeoutUploadAgain3Shape(driver):

    driver.find_element_by_class_name('icon__11943b9').click()
    sleep(3)
    driver.find_element_by_xpath("//button[@class='linear-button__0ca0ac6' and text()='批准此方案']").click()

    driver.find_element_by_xpath("//button[@class='primary__f4046af' and text()='重新提交牙颌模型']").click()

    driver.find_element_by_xpath(
        '//*[@id="__APPLICATION_NOTICE__"]/div/div/div/div[1]/div[2]/div[2]/div[3]/label').click()

    sleep(1.5)
    driver.switch_to.frame(2)

    try:
        driver.find_element_by_xpath("//button[@class='ng-binding' and text()='张雅竹']").click()
    except:
        driver.find_element_by_xpath(
            '/html/body/ui-view/div/new-order/dialog-threeshap/div/div[2]/div[2]/div[3]/div[4]/div[1]').click()

    driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[2]/div[3]').click()
    try:
        driver.find_element_by_xpath("//textarea[@placeholder='请输入您的修改意见……' and @maxlength='1000']").send_keys(
            "3D超时，通过3shape重新上传")
    except:
        driver.find_element_by_xpath('//*[@id="__APPLICATION_NOTICE__"]/div/div/div/div[1]/div[3]/textarea').send_keys(
            "D超时，通过3shape重新上传")

    driver.find_element_by_xpath("//button[@class='blue__5c0dcf0' and text()='提交']").click()

    sleep(5)