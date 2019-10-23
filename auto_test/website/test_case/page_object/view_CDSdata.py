from website.test_case.models.function import *
def toViewCDSdata(driver):

    driver.refresh()

    driver.switch_to.frame("otherPage")
    driver.find_element_by_xpath('//*[@id="phase-0"]/div[1]/div').click()
    sleep(1)
    # insert_img(driver,"cds资料.jpg")
    driver.find_element_by_class_name('i18n_historyshow_order').click()
    sleep(2)
    driver.find_element_by_id('photo-7').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="casedataID"]/tbody/tr/td[1]/a').click()

    sleep(1)



