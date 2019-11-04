from time import sleep
from CRM_Style.website.test_case.model.function import *

def acceptAlert(driver):

    # 再次回到CRM
    driver.switch_to.window(get_handles(driver)[0])
    # sleep(1)
    driver.find_element_by_css_selector("#operation").click()
    # 处理警告弹窗
    driver.switch_to.alert.accept()
    sleep(3)
    try:
        driver.switch_to.alert.accept()
        sleep(1.5)
        try:
            driver.switch_to.alert.accept()
            sleep(1.5)
        except:
            pass
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
