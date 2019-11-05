
#基本信息页面


def adult_basic_information(driver,patientname,hospital): #hospital是医疗机构，只需要传入1,2,3,4（数字代表在页面列表的位置）
    driver.find_element_by_css_selector('#required-1 > input').clear()

    driver.find_element_by_css_selector('#required-1 > input').send_keys(patientname)
    driver.find_element_by_id('male').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[%d]'%hospital).click()
    driver.find_element_by_id("patientBirthdate").click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[1]/ui-view/adult-info/base-info/div[2]/form/div[1]/ul/li[6]/input').send_keys("13083404589")

    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("gxchl").click()
    driver.find_element_by_id("chyj").click()




