from time import sleep
import libs.create_3d as create3d
import libs.test_utils as test_utils
import libs.keywords_trans as key_trans
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Process3D:
    def __init__(self, mainhandler, crm_casecode, case_id):
        self.mainhandler = mainhandler
        self.driver = mainhandler.driver
        self.crm_casecode = crm_casecode
        self.case_id = case_id
        self.win_handle = {}

    def test_f(self):
        '''在iortho查看3D方案 '''
        print('在iortho查看3D方案 ')
        create3d.open_patient_detail(self.driver, self.mainhandler.g_config.get("iortho_url"), 2)
        key_trans.wait_for_3d_ele(self.driver)
        self.driver.refresh()

    def test_g(self):
        '''检查报价单'''
        print('检查报价单')
        self.win_handle["detail_handle"] = self.driver.current_window_handle
        print("到这里了")
        sleep(1)
        self.driver.find_element_by_class_name('bill.ng-scope').click()
        key_trans.switch_to_cur_win(self.driver)
        test_utils.insert_img(self.driver, self.case_id, '质检报告单.png')
        self.driver.close()
        self.switch_to_detail_handle()
        sleep(1)

    def test_h(self):
        '''通过待办事项进入第一个3D方案'''
        print('通过待办事项进入第一个3D方案')
        # 点击待办事项
        key_trans.switch_to_cur_win(self.driver, lambda: self.driver.find_element_by_class_name('case-name.layout-flex-1.ng-binding').click())
        # wait = WebDriverWait(self.driver, 10, 0.5)
        # wait.until(EC.visibility_of(self.driver.find_element_by_css_selector("[class^='play']>[class^='icon']")))
        sleep(10)
        Process3D.todo_feedback3d(self.driver)
        sleep(4)
        key_trans.close_tab(self.driver)

    def test_i(self):
        '''进入crm编辑意见修改任务单，并且点击意见不修改'''
        print('进入crm编辑意见修改任务单，并且点击意见不修改')
        key_trans.logincrm_handler(self.mainhandler)
        create3d.searchPatient(self.driver, self.crm_casecode)
        self.driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        sleep(1.5)
        self.driver.find_element_by_id("no_modified_tasks").click()
        self.driver.switch_to.alert.accept()
        self.driver.close()

    def test_j(self):    #运行到这个方法出错，应该还是那个患者详情页只能打开一个的问题，前面的窗口应该已经打开过，导致没有切换到患者详情页
        '''回到iortho从增强入口批准目标位方案'''
        print('回到iortho从增强入口批准目标位方案')
        key_trans.switch_to_cur_win(self.driver)
        create3d.open_patient_detail(self.driver, self.mainhandler.g_config.get("iortho_url"))
        key_trans.wait_for_3d_ele(self.driver)
        self.driver.find_element_by_css_selector(".web-design-list>div:first-child").click()
    
        # 这是弹出的打开方式选择器
        self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()

        key_trans.switch_to_cur_win(self.driver)
        sleep(10)
        Process3D.approval3D(self.driver)
        key_trans.close_tab(self.driver)

    def test_k(self):
        '''在crm中将已经批准的3D方案意见回传'''
        print('在crm中将已经批准的3D方案意见回传')
        self.driver.refresh()
        key_trans.logincrm_handler(self.mainhandler)
        create3d.searchPatient(self.driver, self.crm_casecode)
        Process3D.ideaBack3D(self.driver)
        key_trans.close_tab(self.driver)

    def test_l(self):
        '''对于已经意见回传的3D方案再次确认'''
        print('对于已经意见回传的3D方案再次确认')
        try:
            create3d.open_patient_detail(self.driver, self.mainhandler.g_config.get("iortho_url"), 4)
            key_trans.wait_for_3d_ele(self.driver)
            self.driver.find_element_by_css_selector(".web-design-list>div:first-child").click()
    
            # 这是弹出的打开方式选择器
            self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()
            key_trans.switch_to_cur_win(self.driver)
            sleep(10)
            Process3D.approval3D(self.driver)
            key_trans.close_tab(self.driver, 2)
        except:
            key_trans.switch_to_cur_win(self.driver)

    def test_m(self):
        '''设计全设计3D方案'''
        print('设计全设计3D方案')
        key_trans.create3d_handler(self.mainhandler, {"val": '{"dir_name": "doubleDDM"}'})

    def test_n(self):
        '''回到iortho，查看全设计方案'''
        print('回到iortho，查看全设计方案')
        create3d.open_patient_detail(self.driver, self.mainhandler.g_config.get("iortho_url"), 4)
        key_trans.wait_for_3d_ele(self.driver)


    def test_o(self):
        '''全设计3D超时，通过3shape上传重新提交模型'''
        print('全设计3D超时，通过3shape上传重新提交模型')
        self.driver.find_element_by_css_selector(".web-design-list>div:first-child").click()
    
        # 这是弹出的打开方式选择器
        self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()

        key_trans.switch_to_cur_win(self.driver)
        sleep(10)
        Process3D.timeoutUploadAgain3Shape(self.driver)
        key_trans.close_tab(self.driver)
        print("等待数据同步到cds")
        sleep(20)
        self.driver.refresh()
    
    def test_p(self):
        '''3D的3shape重传以后，检查cds的资料和收获记录'''
        print('3D的3shape重传以后，检查cds的资料和收获记录')
        key_trans.logincrm_handler(self.mainhandler)
        create3d.searchPatient(self.driver, self.crm_casecode)
        key_trans.switch_to_cur_win(self.driver, lambda: self.driver.find_element_by_css_selector("#pause_tasks_open").click())
        self.driver.switch_to.frame("otherPage")
        self.driver.find_element_by_css_selector('.todo-tasklist-list:last-child').click()
        test_utils.insert_img(self.driver, self.case_id, '3D重新上传之原始stl变化.png')
        key_trans.close_tab(self.driver)
        Process3D.receivingRecords(self.driver)
        test_utils.insert_img(self.driver, self.case_id, '3D重新上传之收获记录.png')
    
    def test_q(self):
        '''对于重新上传的3D方案不修改'''
        print('对于重新上传的3D方案不修改')
        self.driver.find_element_by_id('ea_case_ea_stage_1ea_case_ida').click()
        self.driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        self.driver.find_element_by_id('no_modified_tasks').click()
        self.driver.switch_to.alert.accept()
        sleep(2)
        key_trans.close_tab(self.driver)

    def test_r(self):
        '''回到iortho重新批准3D全设计方案'''
        print('回到iortho重新批准3D全设计方案')
        create3d.open_patient_detail(self.driver, self.mainhandler.g_config.get("iortho_url"))
        key_trans.wait_for_3d_ele(self.driver)
        self.driver.find_element_by_css_selector(".web-design-list>div:first-child").click()
    
        # 这是弹出的打开方式选择器
        self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()
        sleep(10)
        key_trans.switch_to_cur_win(self.driver)
        Process3D.approval3D(self.driver)

    @staticmethod
    def todo_feedback3d(driver):

        # 加载页的播放按钮
        driver.find_element_by_css_selector("[class^='play']>[class^='icon']").click()
        sleep(2)
        # 提交修改意见
        # driver.find_element_by_xpath(
        #     '//*[@id="__APPLICATION_ROOT__"]/div/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/a').click()
        driver.find_element_by_link_text("提交修改意见").click()
        driver.find_element_by_css_selector('[class^="feedback-textarea"]').send_keys("通过自动化脚本提交修改意见…………")
        driver.find_element_by_css_selector('[class^="plan-content"] button[class^="linear-button"]').click()

    @staticmethod
    def approval3D(driver):
        driver.find_element_by_css_selector("[class^='play']>[class^='icon']").click()
        sleep(2)
        driver.find_element_by_css_selector("[class^='body-right']>[class^='case-introduce'] button[class^='linear-button']").click()
        try:
            driver.find_element_by_css_selector("[class^='modal-footer'] button:first-child").click()
            driver.find_element_by_css_selector("[class^='modal-footer'] button[class^='submit']").click()
            sleep(2)
        except:
            driver.find_element_by_css_selector("[class^='modal-footer'] button[class^='submit']").click()
            sleep(2)

    @staticmethod
    def ideaBack3D(driver):
        driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        sleep(1.5)
        driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_stage_ea_design_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        driver.find_element_by_id('idea_back').click()
        driver.switch_to.alert.accept()
        driver.find_element_by_id('ea_case_id_c').click()
        sleep(1.5)
        driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        driver.find_element_by_id('no_modified_tasks').click()
        driver.switch_to.alert.accept()
        sleep(2)

    @staticmethod
    def timeoutUploadAgain3Shape(driver):

        driver.find_element_by_css_selector("[class^='play']>[class^='icon']").click()
        sleep(2)
        driver.find_element_by_css_selector(
            "[class^='body-right']>[class^='case-introduce'] button[class^='linear-button']").click()
        driver.find_element_by_css_selector("[class^='modal-footer'] button:nth-child(2)").click()

        driver.find_element_by_xpath(
            '//*[@id="__APPLICATION_NOTICE__"]/div/div/div/div[1]/div[2]/div[2]/div[3]/label').click()

        sleep(1.5)
        driver.switch_to.frame(driver.find_element_by_css_selector("[class^='threeShapeIframe']"))

        try:
            driver.find_element_by_css_selector(".patientlist-listcontent .tbody>div:first-child").click()
        except:
            driver.find_element_by_xpath(
                '/html/body/ui-view/div/new-order/dialog-threeshap/div/div[2]/div[2]/div[3]/div[4]/div[1]').click()

        driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[2]/div[3]').click()
        try:
            driver.find_element_by_xpath("//textarea[@placeholder='请输入您的修改意见……' and @maxlength='1000']").send_keys(
                "3D超时，通过3shape重新上传")
        except:
            driver.find_element_by_xpath(
                '//*[@id="__APPLICATION_NOTICE__"]/div/div/div/div[1]/div[3]/textarea').send_keys(
                "D超时，通过3shape重新上传")

        driver.find_element_by_css_selector("[class^='modal-footer'] button:nth-child(1)").click()
        sleep(5)

    @staticmethod
    def receivingRecords(driver):
        driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        sleep(1.5)
        test_utils.pageDown(driver)

    def switch_to_detail_handle(self):
        self.driver.switch_to.window(self.win_handle["detail_handle"])
        self.driver.refresh()
