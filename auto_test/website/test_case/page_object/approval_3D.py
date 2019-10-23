#批准3D方案
from time import sleep

def approval3D(driver):
    driver.find_element_by_class_name('icon__11943b9').click()
    sleep(3)
    driver.find_element_by_xpath("//button[@class='linear-button__0ca0ac6' and text()='批准此方案']").click()
    try:
        driver.find_element_by_xpath("//button[@class='blue__5c0dcf0 small__d2f4d93' and text()='仍然批准']").click()
        driver.find_element_by_xpath("//button[@class='submit__3055d35' and text()='批准此方案']").click()
        sleep(5)
    except:
        driver.find_element_by_xpath("//button[@class='submit__3055d35' and text()='批准此方案']").click()
        sleep(5)


