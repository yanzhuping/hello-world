#导入相关模块
from selenium  import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#加载浏览器驱动
def create_makeit(username,password,url,lastname,num):

    chrome_options = webdriver.ChromeOptions()
    #
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1500,900')
    # chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    print("开始创建病例")
    driver.get(url)
    # driver.switch_to.frame("the-real-login-page")
    driver.find_element_by_id("_username").clear()
    driver.find_element_by_id("_username").send_keys(username)
    driver.find_element_by_id("_password").clear()
    driver.find_element_by_id("_password").send_keys(password)
    sleep(1)
    driver.find_element_by_id("_btn_login").click()
    sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(4)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[2]/img[1]').click()
    driver.switch_to.window(driver.window_handles[1])

    a=0
    while a<num:
        a += 1
        try:
            driver.refresh()
            patientname=str(a)+lastname
            driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/div/div/div[2]/div').click()
            driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/div/new-order/div/div/div[2]/div[1]/select-button[1]/div/input').clear()
            driver.find_element_by_xpath(
                '//*[@id="root-route"]/ui-view/div/new-order/div/div/div[2]/div[1]/select-button[1]/div/input').send_keys(patientname)
            # js = 'document.getElementById("patientBirthdate").removeAttribute("readonly")'
            # derver.execute_script(js)
            driver.find_element_by_id("patientBirthdate").click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[1]/td[2]').click()
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='机构'])[1]/following::select[1]").click()
            Select(driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='机构'])[1]/following::select[1]")).select_by_visible_text(u"上海天使口腔门诊部")
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='机构'])[1]/following::select[1]").click()
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='拔牙'])[1]/following::span[1]").click()
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='上传口扫文件'])[1]/following::span[1]").click()
            sleep(3)
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='帐号与简介'])[1]/following::div[4]").click()
            sleep(2)
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='点击加载更多'])[1]/following::div[1]").click()
            driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='时间:'])[1]/following::div[4]").click()
            sleep(1)
            try:
                driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/div/new-order/attention/div/div/div[3]/button').click()
            except:
                pass
            print("病例名为:"+str(a)+lastname+"创建成功")
        except:
            driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/div/new-order/div/div/div[1]/div/span/a').click()
            print("病例名为:" + str(a) + lastname + "创建失败")
        sleep(1)
    print("全部执行完成！")
    driver.quit()

if __name__ == '__main__':
    url_sit='https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas'
    url_adv='https://iorthoadv.angelalign.com/cas/login?service=https://iorthoadv.angelalign.com/OPM/shiro-cas'
    url_prod="https://iortho.angelalign.com/cas/login?service=https://iortho.angelalign.com/OPM/shiro-cas"

    # create_makeit('yanzp0857','111111',url_sit,"ccccc",30)

    # create_makeit('cesys13784','111111',url_adv,"yanya",15)
    create_makeit('cesys13784','1234567',url_prod,'yayauu')





