from website.test_case.models.function import *


def addNotes(driver):
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='拥挤'])[1]/following::button[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='拥挤'])[1]/following::textarea[1]").click()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='拥挤'])[1]/following::textarea[1]").clear()
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='拥挤'])[1]/following::textarea[1]").send_keys(
        "python+selenium")
    driver.find_element_by_xpath(
        u"(.//*[normalize-space(text()) and normalize-space(.)='取消'])[1]/following::button[1]").click()
    sleep(1)


