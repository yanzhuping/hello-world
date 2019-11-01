import unittest
from driver.driver import *
from website.test_case.models.config import *
from website.test_case.page_object.accept_alert import *
from website.test_case.page_object.add_notes import *
from website.test_case.page_object.adult_basic_information import *
from website.test_case.page_object.crm_receiving_records import *
from website.test_case.page_object.dsign_scheme import *
from website.test_case.page_object.login_crm import *
from website.test_case.page_object.login_iortho import *
from website.test_case.page_object.select_product import *
from website.test_case.page_object.serach_crm_patient import *
from website.test_case.page_object.serach_iortho_patient import *
from website.test_case.page_object.upload_ODS import *
from website.test_case.page_object.upload_photos import *
from website.test_case.page_object.upload_stlandddm import *
from website.test_case.page_object.upload_tooth_model import *
from website.test_case.page_object.view_CDSdata import *
from website.test_case.page_object.new_worksheet import *
from website.test_case.page_object.to_do_feedback_3D import *
from website.test_case.page_object.approval_3D import *
from website.test_case.page_object.idea_back_3D import *
from website.test_case.page_object.timeout_upload_again_3shape import *



class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    dr = browser()

    def __init__(self, methodName='runTest',driver=dr, param=None,
                 param1=None,param2=None,param3=None,param4=None,param5=None,param6=None):

        super(ParametrizedTestCase, self).__init__(methodName)

        self.input_name = param
        self.driver = driver
        self.username=param1
        self.password=param2
        self.url = param3
        self.crm_username = param4
        self.crm_password = param5
        self.crmurl = param6
        self.product_num = product_num
        self.hospital=hospital

    @staticmethod
    def parametrize(testcase_klass, param=None,param1=None,
                    param2=None,param3=None,param4=None,param5=None,param6=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass
                          (name, param=param,param1=param1,param2=param2,
                           param3=param3,param4=param4,param5=param5,param6=param6)
                          )
        return suite


class standard_process(ParametrizedTestCase):

    def test_a(self):
        '''登录iortho并选择产品，本用例选择标准版'''
        print("开始执行第一条测试用例：登录以及选择产品类型")
        print("开始登录")
        login_iortho(self.driver, self.url, self.username, self.password)
        insert_img(self.driver, "工作台.jpg", '#root-route')
        while True:
            try:
                print("开始选择产品，本次选用标准版\n")
                select_product(self.driver,self.product_num)
                sleep(1)
                break
            except:
                print("选择产品失败。重新选择\n")

        self.driver.switch_to.window(get_handles(self.driver)[1])
        sleep(2)

    def test_b(self):
        '''完善委托加工单的一系列操作'''
        print("开始执行第二条测试用例：委托加工单")

        while True:
            try:
                print("查看未完善的预览页")
                jumpPreview(self.driver)
                insert_img(self.driver, "未完善的预览页.jpg", '.page-teenagers')

                print("完善基本信息")
                jumpBaseInformation(self.driver)
                adult_basic_information(self.driver, self.input_name,self.hospital)
                insert_img(self.driver, "基本信息.jpg", '.page-teenagers')

                nextpage(self.driver)

                print("完善加工单")
                NewWorksheet(self.driver)
                insert_img(self.driver, "加工单.jpg", '.page-teenagers')

                nextpage(self.driver)

                print("上传影像资料")
                uploadPhoto(self.driver)

                print("上传牙颌模型")
                uploadToothModel(self.driver)

                nextpage(self.driver)

                insert_img(self.driver, "完善的预览页.jpg", '.page-teenagers')

                print("提交病例\n")
                submit(self.driver)
                break
            except Exception as e:
                print(e,"病例创建失败，重新执行")

        deleteDataFromMySQL(host, mysqluser, mysqlpasswd, dbName, tableName)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])

        sleep(1)

    def test_c(self):

        '''在iortho搜索病例、查看病例资料，并添加备注'''
        print("搜索提交的病例")
        serachIorthoPathient(self.driver,self.input_name)
        self.driver.switch_to.window(get_handles(self.driver)[1])

        print("获取病例序号并设置全局变量")
        globals()["caseid"] = getCaseNum(self.driver)

        print("添加备注")
        addNotes(self.driver)
        insert_img(self.driver,"患者详情页.jpg", 'page-patient-detail')

        print("查看病例资料\n")
        self.driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='编辑病例'])[1]/following::div[1]").click()
        self.driver.switch_to.window(get_handles(self.driver)[2])
        sleep(1.5)
        insert_img(self.driver,"病例资料.jpg")


        #新加的

        self.driver.close()

        self.driver.switch_to.window(get_handles(self.driver)[1])

        return globals()["caseid"]

    def test_d(self):
        '''查看收获记录以及cds中的委托加工单'''
        print("开始执行第四条用例：收货记录以及CDS资料")
        print("登录crm")
        #登录crm并查找用例1创建的的病例
        loginCrm(self.driver,self.crmurl,self.crm_username,self.crm_password)

        searchPatient(self.driver,globals()["caseid"])

        self.driver.switch_to.window(get_handles(self.driver)[1])

        print("在crm中查找创建的病例并查看收获记录")
        receivingRecords(self.driver)
        insert_img(self.driver,"收货记录.jpg")

        print("进入CDS查看病例资料以及委托加工单\n")
        self.driver.switch_to.window(get_handles(self.driver)[2])
        toViewCDSdata(self.driver)
        self.driver.switch_to.window(get_handles(self.driver)[3])
        insert_img(self.driver,"委托加工单.jpg")

        # self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[2])

    def test_e(self):
        '''创建3D方案'''
        print("开始执行第五条测试用例：创建3D方案：")

        print("重命名文件以符合上传标准")
        print("更改json文件中的caseinfo键对应的值")
        print("上传stl文件")
        print("上传ddm")
        get_new_json(globals()["caseid"],1)

        uploadStlAndDdm(self.driver,globals()["caseid"],1,"1_1")

        self.driver.switch_to.window(get_handles(self.driver)[1])

        print("设计3D方案")
        dsignScheme(self.driver)

        self.driver.switch_to.window(get_handles(self.driver)[2])
        self.driver.refresh()
        sleep(3)

        print("上传ods四个文件")
        uploadOds(self.driver, 1,"1_1", globals()["caseid"], 0, 1, 1)

        self.driver.switch_to.window(get_handles(self.driver)[1])
        print("加载同步、处理警告、提交\n")
        acceptAlert(self.driver)
        self.driver.switch_to.window(get_handles(self.driver)[2])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])

    def test_f(self):
        '''在iortho查看3D方案'''

        print("开始执行第六条测试用例：在iortho查看创建的3D方案:")


        serachIorthoPathient(self.driver,self.input_name)
        self.driver.switch_to.window(get_handles(self.driver)[1])

        print("等待数据同步到iortho，等待65s.....\n")
        sleep(65)
        self.driver.refresh()


    def test_g(self):
        '''检查报价单'''
        self.driver.find_element_by_class_name('bill.ng-scope').click()
        sleep(2)
        self.driver.switch_to_window(get_handles(self.driver)[2])
        insert_img(self.driver,'质检报告单.jpg')
        self.driver.close()
        self.driver.switch_to_window(get_handles(self.driver)[1])



    def test_h(self):
        '''通过待办事项进入第一个3D方案'''
        # 点击待办事项
        self.driver.find_element_by_class_name('case-name.layout-flex-1.ng-binding').click()

        # 怎么知道已经加载完成，可以点击播放？暂时先等待
        sleep(45)
        self.driver.switch_to.window(get_handles(self.driver)[2])
        toDoFeedback3D(self.driver)
        sleep(4)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.refresh()

    def test_i(self):
        '''进入crm编辑意见修改任务单，并且点击意见不修改'''
        loginCrm(self.driver,self.crmurl,self.crm_username,self.crm_password)
        searchPatient(self.driver,globals()["caseid"])
        self.driver.switch_to.window(get_handles(self.driver)[2])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        sleep(1.5)
        self.driver.find_element_by_id("no_modified_tasks").click()
        self.driver.switch_to.alert.accept()
        sleep(1.5)

        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        sleep(30)

    def test_j(self):
        '''回到iortho从增强入口批准目标位方案'''
        serachIorthoPathient(self.driver, self.input_name)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.find_element_by_xpath("//span[@class='ng-binding' and text()='目标位3D方案1']").click()

        #这是弹出的打开方式选择器
        self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()
        sleep(45)
        self.driver.switch_to.window(get_handles(self.driver)[2])
        approval3D(self.driver)
        sleep(5)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        sleep(40)

    def test_k(self):
        '''在crm中将已经批准的3D方案意见回传'''
        self.driver.refresh()
        loginCrm(self.driver,self.crmurl,self.crm_username,self.crm_password)
        searchPatient(self.driver,globals()["caseid"])
        self.driver.switch_to.window(get_handles(self.driver)[2])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        ideaBack3D(self.driver)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])


    def test_l(self):
        '''对于已经意见回传的3D方案再次确认'''
        try:
            serachIorthoPathient(self.driver, self.input_name)
            self.driver.switch_to.window(get_handles(self.driver)[1])
            self.driver.refresh()
            self.driver.find_element_by_xpath("//span[@class='ng-binding' and text()='目标位3D方案1']").click()

            # 这是弹出的打开方式选择器
            self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()
            sleep(45)
            self.driver.switch_to.window(get_handles(self.driver)[2])
            approval3D(self.driver)
            sleep(5)
            self.driver.close()
            self.driver.switch_to.window(get_handles(self.driver)[1])
        except:
            self.driver.switch_to.window(get_handles(self.driver)[1])

    def test_m(self):
        '''设计全设计3D方案'''
        self.driver.refresh()
        loginCrm(self.driver, self.crmurl, self.crm_username, self.crm_password)
        searchPatient(self.driver, globals()["caseid"])
        self.driver.switch_to.window(get_handles(self.driver)[1])
        #点击当前阶段
        self.driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        sleep(1.5)
        dsignScheme(self.driver)
        self.driver.switch_to.window(get_handles(self.driver)[2])
        uploadOds(self.driver, 1, "1_2", globals()["caseid"], 0, 2, 2)
        sleep(2)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        acceptAlert(self.driver)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])


    def test_n(self):
        '''回到iortho，查看全设计方案'''
        serachIorthoPathient(self.driver,self.input_name)
        self.driver.switch_to.window(get_handles(self.driver)[1])

        print("等待数据同步到iortho，等待65s.....\n")
        sleep(65)
        self.driver.refresh()
    #
    def test_o(self):
        '''全设计3D超时，通过3shape上传重新提交模型'''
        self.driver.find_element_by_xpath("//span[@class='ng-binding' and text()='方案2']").click()

        # 这是弹出的打开方式选择器
        self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()
        sleep(45)
        self.driver.switch_to.window(get_handles(self.driver)[2])
        timeoutUploadAgain3Shape(self.driver)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        sleep(60)
        self.driver.refresh()

    def test_p(self):
        '''3D的3shape重传以后，检查cds的资料和收获记录'''
        loginCrm(self.driver, self.crmurl, self.crm_username, self.crm_password)
        searchPatient(self.driver, globals()["caseid"])

        self.driver.switch_to.window(get_handles(self.driver)[2])
        self.driver.switch_to.frame("otherPage")
        self.driver.find_element_by_xpath('//*[@id="phase-0"]/div[1]/div').click()
        insert_img(self.driver,'3D重新上传之原始stl变化.jpg')
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[1])
        receivingRecords(self.driver)
        insert_img(self.driver,'3D重新上传之收获记录.jpg')

    def test_q(self):
        '''对于重新上传的3D方案不修改'''
        self.driver.find_element_by_id('ea_case_ea_stage_1ea_case_ida').click()
        self.driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        self.driver.find_element_by_id('no_modified_tasks').click()
        self.driver.switch_to.alert.accept()
        sleep(45)
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])


    def test_r(self):
        '''回到iortho重新批准3D全设计方案'''
        serachIorthoPathient(self.driver, self.input_name)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.refresh()
        self.driver.find_element_by_xpath("//span[@class='ng-binding' and text()='方案2']").click()

        # 这是弹出的打开方式选择器
        self.driver.find_element_by_class_name('web-design-list-hover-btn.mrg-b-20').click()
        sleep(45)
        self.driver.switch_to.window(get_handles(self.driver)[2])
        approval3D(self.driver)


if __name__ == '__main__':

    # suite = unittest.TestSuite()
    # suite.addTest(ParametrizedTestCase.parametrize(standard_process,param="患者姓名"))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    input_name = readDataFromMySQL(host, mysqluser, mysqlpasswd, dbName, tableName)

    suite = unittest.TestSuite()
    suite.addTest(
        ParametrizedTestCase.parametrize(
            standard_process, param=input_name, param1=username,
            param2=password, param3=url, param4=crm_username, param5=crm_password, param6=crmurl))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

