from time import sleep
from ThreeDimensional_Project.website.test_case.model.function import *

def uploadOds(driver,type_mopian,id,num,phase,title,up):
    # 上传ods，即4个文件
    driver.switch_to.frame("otherPage")
    driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div'%(phase)).click()     #这个地方可以参数化，phase-0，phase-1.....

    driver.find_element_by_css_selector("#i18n_historyshow_3Ddesign").click()
    sleep(4)

    driver.find_element_by_xpath('//*[@id="ODSTitle"]/ul/li[%d]/a'%(title)).click()  #这个参数化“li、li【2】。。。。。

    driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div[3]/div[%d]/div[3]/button[1]'%(up)).click()  #参数化，倒数第三个div、div【2】
    sleep(2)

    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(type_mopian,id,num)[1])
    sleep(1.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(type_mopian,id,num)[2])
    sleep(1.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(type_mopian,id,num)[3])
    sleep(1.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(type_mopian,id,num)[4])
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="ODSUploadModal"]/div[3]/button').click()

