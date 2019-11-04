from time import sleep
from CRM_Style.website.test_case.model.function import *

def uploadStlAndDdm(driver,type_mopian,id,num,phase):

    i=0
    while i<3:
        i=i+1
        try:
            driver.switch_to.window(get_handles(driver)[1])
            driver.refresh()
            sleep(2)

            # 切换至iframe嵌套
            driver.switch_to.frame("otherPage")

            driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div'%(phase)).click()

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
            driver.find_element_by_css_selector("#ddmType").send_keys(rename_file(type_mopian,id,num)[0])
            sleep(2)
            driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
            sleep(2)
            break
        except:
            print("文件上传失败，重新上传")
            driver.refresh()
            driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div'%(phase)).click()
            driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
            driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="STLdataID"]/tbody/tr[1]/td[4]/a[1]').click()
            driver.switch_to.alert.accept()
            driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
            driver.find_element_by_xpath('//*[@id="STLdataID"]/tbody/tr/td[4]/a[1]').click()
            driver.switch_to.alert.accept()

    # 回到crm
    driver.switch_to.window(get_handles(driver)[0])