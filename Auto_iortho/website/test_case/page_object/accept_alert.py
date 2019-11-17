from Auto_iortho.website.test_case.models.function import *

def acceptAlert(driver):

    # 再次回到CRM

    # sleep(1)
    driver.find_element_by_css_selector("#operation").click()
    # 处理警告弹窗
    driver.switch_to.alert.accept()
    sleep(1)
    try:
        driver.switch_to.alert.accept()
        sleep(2)
    except:
        pass

    driver.find_element_by_css_selector("#do_submit").click()

    driver.switch_to.alert.accept()
    sleep(3)

    driver.switch_to.alert.accept()
    sleep(3)

    driver.find_element_by_css_selector("#send_design").click()
    driver.switch_to.alert.accept()
    sleep(3)
