#导入相关模块
from selenium  import webdriver
from time import sleep
import time

class create():
    def login(self,driver):
        driver.implicitly_wait(10)
        #打开时代天使登陆页面
        driver.get(
            "https://opm-cas.sh-sit.eainc.com:8443/cas/login?service=https://opm-cas.sh-sit.eainc.com:8443/OPM/shiro-cas")

        #窗口最大化
        driver.maximize_window()
        #切换至frame页面
        driver.switch_to.frame("the-real-login-page")
        #输入账号和密码
        driver.find_element_by_id("_username_line").click()
        driver.find_element_by_id("_username").clear()
        driver.find_element_by_id("_username").send_keys("qin")
        driver.find_element_by_id("_l_password").click()
        driver.find_element_by_id("_password").clear()
        driver.find_element_by_id("_password").send_keys("111111")
        driver.find_element_by_id("_btn_login").click()
       #关掉新功能介绍swiper
        #driver.find_element_by_class_name("close").click()
        sleep(3)
        #跳转到列表页
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
        sleep(3)

    def select(self,driver,patientname):
        #在列表选择矫治器类型
        driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[3]/span[1]').click()
        driver.find_element_by_xpath(
            '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()

        # 获取所有窗口的句柄
        self.num = driver.window_handles

        #将driver绑定在新窗口句柄
        driver.switch_to.window(self.num[1])

        #完善矫治器加工单项目，必填项必须完成
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[1]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='*'])[1]/following::input[1]").send_keys(patientname)
        driver.find_element_by_id("female").click()

        driver.find_element_by_xpath('//*[@id="required-2"]/div[1]/div').click()
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[2]').click()

        driver.find_element_by_id("patientBirthdate").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='六'])[1]/following::td[7]").click()
        driver.find_element_by_id("ansyl").click()
        driver.find_element_by_id("chyj").click()
        sleep(2)
        driver.find_element_by_css_selector('#root-route > ui-view > adult-new-case > div.page-teenagers > '
                                            'teenagers-nav > div > ul > li:nth-child(2) > '
                                            'div.layout-row.layout-x-center.layout-y-center').click()
        driver.find_element_by_css_selector('#root-route > ui-view > adult-new-case > div.page-teenagers > '
                                            'teenagers-nav > div > ul > li:nth-child(2) > '
                                            'div.layout-row.layout-x-center.layout-y-center').click()
        sleep(2)
        driver.find_element_by_id("mainsuit0").click()
        driver.find_element_by_id("treatTarget0").click()
        driver.find_element_by_id("treatTooth1").click()
        driver.find_element_by_id("facetype1").click()
        driver.find_element_by_id("sagittalRight1").click()
        driver.find_element_by_id("sagittalLeft1").click()
        driver.find_element_by_id("midline1").click()
        driver.find_element_by_id('antinail2').click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='<上一页'])[1]/following::div[1]").click()

        #上传照片文件
        driver.find_element_by_id("pic-0").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\2.jpg")
        driver.find_element_by_id("pic-1").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\3.jpg")
        driver.find_element_by_id("pic-2").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\4.jpg")
        driver.find_element_by_id("pic-3").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\5.jpg")
        driver.find_element_by_id("pic-4").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\6.jpg")
        driver.find_element_by_id("pic-5").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\7.jpg")
        driver.find_element_by_id("pic-6").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\8.jpg")
        driver.find_element_by_id("pic-7").send_keys(r"C:\Users\qinmaoding\Desktop\xiongmaoren\9.jpg")
        sleep(3)

        #选择数字模型
        driver.find_element_by_id("hasSilicon1").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='本地上传'])[1]/following::label[2]").click()

        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='<上一页'])[1]/following::div[1]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='暂存'])[1]/following::button[1]").click()
        sleep(10)
        driver.close()

    def create_champion(self,driver):
        self.login(driver)
        for i in range(2,8):
            name=str(i)+"-质检不合格0923"
            self.select(driver,name)
            driver.switch_to.window(self.num[0])

if __name__ == '__main__':
    driver = webdriver.Chrome()
    C=create()
    C.create_champion(driver)
    driver.quit()