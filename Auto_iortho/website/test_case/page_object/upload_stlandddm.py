from Auto_iortho.website.test_case.models.function import *



def uploadStlAndDdm(driver,id,type_mopian,num):

    while True:
        try:
            # 切换至iframe嵌套
            driver.refresh()
            sleep(2)
            driver.switch_to.frame("otherPage")
            sleep(1)

            driver.find_element_by_xpath('//*[@id="phase-0"]/div[1]/div').click()
            # 上传咬合stl
            driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
            driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
            sleep(2)
            driver.find_element_by_css_selector("#ddmType").send_keys(choice_photo()[0])
            sleep(2)
            driver.find_element_by_css_selector("#ddmType").send_keys(choice_photo()[1])
            sleep(2)
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
            sleep(5)
            driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
            sleep(2)

            # 上传DDM文件
            driver.find_element_by_css_selector(".i18n_historyshow_ddm").click()
            driver.find_element_by_xpath('//*[@id="collapse_3_4"]/div/a[1]').click()
            sleep(2)
            driver.find_element_by_css_selector("#ddmType").send_keys(rename_file(id,type_mopian,num)[0])
            sleep(2)
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
            sleep(2)
            break
        except:
            print("文件上传失败，重新上传")
            driver.refresh()
            driver.find_element_by_xpath('//*[@id="phase-0"]/div[1]/div').click()
            driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
            driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="STLdataID"]/tbody/tr[1]/td[4]/a[1]').click()
            driver.switch_to.alert.accept()
            driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
            driver.find_element_by_xpath('//*[@id="STLdataID"]/tbody/tr/td[4]/a[1]').click()
            driver.switch_to.alert.accept()


