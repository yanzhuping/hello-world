from Auto_iortho.website.test_case.models.function import *

def uploadOds(driver,type_mopian,num,id,phase,title,up):  #up这个参数是每一个阶段上传4个文件对应页的上传按钮
    # 上传ods，即4个文件
    driver.switch_to.frame("otherPage")
    sleep(1)
    driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div'%(phase)).click()     #这个地方可以参数化，phase-0，phase-1.....

    driver.find_element_by_css_selector("#i18n_historyshow_3Ddesign").click()
    sleep(4)

    driver.find_element_by_xpath('//*[@id="ODSTitle"]/ul/li[%d]/a'%(title)).click()  #这个参数化“li、li【2】。。。。。

    driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div[3]/div[%d]/div[3]/button[1]'%(up)).click()  #参数化，倒数第三个div、div【2】
    sleep(2)

    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(id,type_mopian,num)[1])
    sleep(1.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(id,type_mopian,num)[2])
    sleep(1.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(id,type_mopian,num)[3])
    sleep(1.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(rename_file(id,type_mopian,num)[4])
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="ODSUploadModal"]/div[3]/button').click()

