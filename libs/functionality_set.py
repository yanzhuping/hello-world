#crm中相关的一些功能集合
from selenium.webdriver.support.ui import Select
import libs.keywords_trans as key_trans
from time import sleep
import random
from crm_style.erp_process import *
from libs.keywords_trans import *

def model_accept(driver):
    '''模型接收'''
    #点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    #点击创建收货记录
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_receipt_1_创建_button"]').click()
    #选择咬合记录
    Select(driver.find_element_by_css_selector("#material_type_c")).select_by_value("18")
    sleep(1)
    # 点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
def silicone_accept(driver):
    '''硅橡胶接收'''
    #点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    #点击创建收货记录
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_receipt_1_创建_button"]').click()
    #选择硅胶
    Select(driver.find_element_by_css_selector("#material_type_c")).select_by_value("15")
    #选择上颌
    Select(driver.find_element_by_css_selector("#material_detail_type_c")).select_by_value("151")
    sleep(1)
    # 点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
def number_accept(driver):
    '''数字模型接收'''
    #点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    #点击创建收货记录
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_receipt_1_创建_button"]').click()
    #选择口扫
    Select(driver.find_element_by_css_selector("#material_type_c")).select_by_value("14")
    sleep(1)
    # 点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
def photo_accept(driver):
    '''照片接收'''
    #点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    #点击创建收货记录
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_receipt_1_创建_button"]').click()
    #选择口内照
    Select(driver.find_element_by_css_selector("#material_type_c")).select_by_value("11")
    sleep(1)
    Select(driver.find_element_by_css_selector("#is_qualified_c")).select_by_value("1")
    # 点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
def x_accept(driver):
    '''x接收'''
    #点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    #点击创建收货记录
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_receipt_1_创建_button"]').click()
    #选择x照片
    Select(driver.find_element_by_css_selector("#material_type_c")).select_by_value("13")
    #选择实物
    Select(driver.find_element_by_css_selector("#material_detail_type_c")).select_by_value("131")
    sleep(1)
    # 点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()

def unqualified_quality_inspection(driver):
    '''质检不合格'''
    #点击新病例阶段

    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    driver.find_element_by_xpath("//*[contains(text(),'口内照')]/../../td[1]/span").click()
    sleep(1)
    #点击口内照编辑
    driver.find_element_by_id('edit_button').click()
    # 实例化一个Select类的对象
    selector = Select(driver.find_element_by_id("is_qualified_c"))
    selector.select_by_value("1")  # 通过value属性值进行选择
    sleep(1)
    #点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
    #点击病例号
    driver.find_element_by_xpath('//*[@id="DEFAULT"]/tbody/tr[2]/td[2]/a').click()
    # driver.find_element_by_css_selector("#ea_case_ea_tasks_1_创建_button").click()
    # Select(driver.find_element_by_css_selector("#category_c")).select_by_value("110000")
    # Select(driver.find_element_by_css_selector("#type_c")).select_by_value("1101a1")
    # driver.find_element_by_css_selector("#SAVE_HEADER").click()
    #点击质检任务单
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()

    sleep(2)
    #如果是海外病例，会有一个alert提示
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    driver.find_element_by_css_selector("#no_qualified_tasks").click()
    sleep(3)
    key_trans.switch_to_win(driver, 1)
    sleep(2)
    Select(driver.find_element_by_css_selector("#pause_reason_list")).select_by_value("1402")
    Select(driver.find_element_by_css_selector("#pause_reason_list2")).select_by_value("3")
    sleep(1)
    driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(key_trans.get_root_path()+"/test_data/QC_Report.doc")
    driver.find_element_by_xpath('/html/body/form/input[5]').click()
    sleep(3)
    #driver.switch_to.alert.accept()
    acceptAlert(driver)
    sleep(1)
    key_trans.switch_to_cur_win(driver)
def unqualified_quality_inspection_go(driver):
    '''质检不合格 进'''
    #点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    #点击收货记录排序
    #driver.find_element_by_css_selector('[sugar="slot59"]').click()
    #点击口内照记录单号 注意口内照编辑后定位顺序会发生改变
    driver.find_element_by_xpath("//*[contains(text(),'口内照')]/../../td[1]/span").click()
    sleep(1)
    #点击口内照编辑
    driver.find_element_by_id('edit_button').click()
    # 实例化一个Select类的对象
    selector = Select(driver.find_element_by_id("is_qualified_c"))
    selector.select_by_value("1")  # 通过value属性值进行选择
    sleep(1)
    #点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
    #点击病例号
    driver.find_element_by_xpath('//*[@id="DEFAULT"]/tbody/tr[2]/td[2]/a').click()
    #点击质检任务单
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()

    driver.find_element_by_css_selector("#no_qualified_tasks").click()
    sleep(3)
    key_trans.switch_to_win(driver, 1)
    sleep(2)
    Select(driver.find_element_by_css_selector("#pause_reason_list")).select_by_value("1402")
    Select(driver.find_element_by_css_selector("#pause_reason_list2")).select_by_value("3")
    sleep(1)
    driver.find_element_by_xpath('/html/body/form/input[1]').send_keys(key_trans.get_root_path()+"/test_data/QC_Report.doc")
    driver.find_element_by_xpath('/html/body/form/input[5]').click()
    sleep(3)
    #driver.switch_to.alert.accept()
    acceptAlert(driver)
    sleep(1)
    try:
        key_trans.switch_to_cur_win(driver)
        key_trans.switch_to_cur_win_ifchange(driver)
    except:
        pass
    sleep(1)
    #点击收货记录口内扫
    driver.find_element_by_id('ea_receipt_id_c').click()
    sleep(2)
    #点击确认不合格进
    driver.find_element_by_id('check_go_next').click()
    sleep(2)
    #切换到弹框
    key_trans.switch_to_win(driver, 1)
    sleep(2)
    Select(driver.find_element_by_css_selector("#go_next_type")).select_by_value("1")
    #上传报告
    driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[2]/input').send_keys(
        key_trans.get_root_path() + "/test_data/QC_Report.doc")
    #提交
    driver.find_element_by_css_selector('[type="submit"]').click()
    sleep(1)
    # try:
    #     driver.switch_to.alert.accept()
    #     driver.switch_to.alert.accept()
    # except:
    #     pass
    acceptAlert(driver)
    sleep(1)
    key_trans.switch_to_cur_win_1(driver)
    print('质检不合格进创建成功')



def unqualified_quality_finish(driver):
    '''病例资料待完善 口内照不合格'''
    try:
        #点击新病例阶段
        driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
        sleep(1)
        #点击收货记录排序
        #driver.find_element_by_css_selector('[sugar="slot59"]').click()
        driver.find_element_by_xpath("//*[contains(text(),'口内照')]/../../td[1]/span").click()
        #点击口内照编辑
        driver.find_element_by_id('edit_button').click()
        # 实例化一个Select类的对象
        selector = Select(driver.find_element_by_id("is_qualified_c"))
        selector.select_by_value("2")  # 通过value属性值进行选择
        sleep(1)
        driver.find_element_by_id('remark_c').send_keys('照片不合格')
        #点击保存
        driver.find_element_by_css_selector('[accesskey="a"]').click()
    except Exception as e:
        print('异常错误口内照编辑：',e)



def quality_inspection_qualified(driver):
    '''质检合格'''
    try:
        # 点击新病例阶段
        driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
        sleep(1)
        # # 点击收货记录排序
        # driver.find_element_by_css_selector('[sugar="slot59"]').click()
        driver.find_element_by_xpath("//*[contains(text(),'口内照')]/../../td[1]/span").click()
        sleep(1)
        # 点击口内照编辑
        driver.find_element_by_id('edit_button').click()
        # 实例化一个Select类的对象
        selector = Select(driver.find_element_by_id("is_qualified_c"))
        selector.select_by_value("1")  # 通过value属性值进行选择
        sleep(1)
        # 点击保存
        driver.find_element_by_css_selector('[accesskey="a"]').click()
        # 点击病例号
        driver.find_element_by_xpath('//*[@id="DEFAULT"]/tbody/tr[2]/td[2]/a').click()
        # 点击质检任务单
        driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        driver.find_element_by_css_selector("#qualified_tasks").click()
        key_trans.switch_to_win(driver, 1)
        driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/th[1]/input').get_attribute("tooth_bit_18")
        driver.find_element_by_xpath('/html/body/form/input[2]').click()
        sleep(3)
        acceptAlert(driver)

            # driver.switch_to.alert.accept()
            # sleep(1)
            # print('关闭第一个弹框')
            # driver.switch_to.alert.accept()
            # print('关闭第二个弹框')
            # driver.switch_to.alert.accept()
            # print('关闭第三个个弹框')

        print('质检合格创建成功')
    except:
        pass
    key_trans.switch_to_cur_win(driver)
    sleep(3)

def create_No_Treatment(driver,casecode,ods):
    '''不收治'''
    # #切换到当前窗口
    # switch_to_cur_win_ifchange(driver)
    driver.close()
    all_win = driver.window_handles
    driver.switch_to.window(all_win[len(all_win)-1])
    sleep(1)
    # 点击新病例阶段
    driver.find_element_by_css_selector('[sugar="slot13b"],[sugar="slot14b"]').click()
    sleep(1)
    driver.find_element_by_xpath("//*[contains(text(),'口内照')]/../../td[1]/span").click()
    sleep(1)
    #点击口内照编辑
    driver.find_element_by_id('edit_button').click()
    # 实例化一个Select类的对象
    selector = Select(driver.find_element_by_id("is_qualified_c"))
    selector.select_by_value("1")  # 通过value属性值进行选择
    sleep(1)
    # 点击保存
    driver.find_element_by_css_selector('[accesskey="a"]').click()
    all_win = driver.window_handles

    driver.switch_to.window(all_win[1])
    # 点击病例号
    driver.find_element_by_xpath('//*[@id="DEFAULT"]/tbody/tr[2]/td[2]/a').click()
    # 点击质检任务单
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_tasks_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#qualified_tasks").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_xpath('/html/body/form/table[2]/tbody/tr[2]/th[1]/input').get_attribute("tooth_bit_18")
    driver.find_element_by_xpath('/html/body/form/input[2]').click()
    #driver.switch_to.alert.accept()
    acceptAlert(driver)
    database_manual_tooth_throwing(casecode)
    all_win = driver.window_handles
    driver.switch_to.window(all_win[len(all_win) - 1])
    currentWin = driver.current_window_handle
    print('当前窗口currentWin：',currentWin)
    driver.refresh()
    sleep(3)
    #点击病例编号
    driver.find_element_by_id("ea_case_ea_tasks_1ea_case_ida").click()
    sleep(3)
    #链接到MTS
    driver.find_element_by_id("btn_link_mts").click()
    sleep(2)
    all_win = driver.window_handles
    print(all_win)
    driver.switch_to.window(all_win[len(all_win)-1])
    sleep(60)
    driver.find_element_by_id('search_form_submit').click()
    #点击任务单编号
    driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[3]/b/a').click()
    sleep(1)
    all_win = driver.window_handles
    print(all_win)
    driver.switch_to.window(all_win[len(all_win) - 1])
    #点击任务单改派
    driver.find_element_by_id('change_task_designer_window').click()
    sleep(1)
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_id('users_1').send_keys('时红梅')
    sleep(1)
    #选择负责人
    driver.find_element_by_xpath('//*[@id="yui-ac-container"]/div/div[2]/ul/li').click()
    sleep(3)
    driver.find_element_by_css_selector('[type="submit"]').click()
    driver.switch_to.window(all_win[len(all_win) - 1])
    sleep(2)
    #点击开始任务
    driver.find_element_by_id('start_task').send_keys(ods['ddm'])
    print( '''后面手动操作：
    点击开始任务，复制一个DDM文件，放入本地文件夹，并重命名格式为“F1_xxx.DDM”，点击完成	任务单完成
    点击方案筛选编码，点击任务单改派	修改为当前MTS用户
    点不收治按钮	不收治完成
    stl格式：caseid_bite(biterecord)_（U或L）_upload.stl
    ddm格式：F1_xxx.DDM
    设计方案点立即发送
''')
    '''后面手动操作：
    点击开始任务，复制一个DDM文件，放入本地文件夹，并重命名格式为“F1_xxx.DDM”，点击完成	任务单完成
    点击方案筛选编码，点击任务单改派	修改为当前MTS用户
    点不收治按钮	不收治完成
    stl格式：caseid_bite(biterecord)_（U或L）_upload.stl
    ddm格式：F1_xxx.DDM
'''
    sleep(10000)
    #点击不收治
    driver.find_element_by_id('no_treatment_window').click()

    sleep(30000)


def create_Word_scheme(driver):
    '''文字方案'''
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_css_selector("#ea_stage_ea_proposal_1_创建_button").click()
    Select(driver.find_element_by_css_selector("#difficulty_c")).select_by_value("3")
    Select(driver.find_element_by_css_selector("#jaw_c")).select_by_value("3")
    driver.find_element_by_css_selector("#forecast_upper_jaw_step_c").send_keys("10")
    driver.find_element_by_css_selector("#forecast_low_jaw_step_c").send_keys("10")
    driver.find_element_by_css_selector("#quote_c").send_keys("1000")
    driver.find_element_by_css_selector("#conformation_price_c").send_keys("10000")

    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    driver.find_element_by_css_selector("#do_submit").click()
    # driver.switch_to.alert.accept()
    # driver.switch_to.alert.accept()
    acceptAlert(driver)
    sleep(4)
    driver.quit()

def finish_phase1(driver):
    '''结束当前病例的阶段'''
    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    driver.find_element_by_css_selector("#ea_case_ea_stage_1_edit_1").click()
    Select(driver.find_element_by_css_selector("#is_produce_c")).select_by_value("1")
    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    sleep(4)

def finish_phase2(driver,maxRetry=3):
    '''结束当前病例的阶段'''
    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    if maxRetry<=0:
        raise Exception('尝试3次结束阶段，仍然失败')

    def endphase():
        driver.find_element_by_css_selector("#ea_case_ea_stage_1_edit_1").click()
        Select(driver.find_element_by_css_selector("#is_produce_c")).select_by_value("1")
        driver.find_element_by_css_selector("#SAVE_HEADER").click()
        sleep(4)
        js = "var action=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        sleep(20)
        driver.refresh()
        endPhase=driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[2]/span').text
        if endPhase=='是':
            print("结束阶段成功,阶段状态为：",endPhase)
        else:
            raise Exception('结束阶段失败，重试！！！')

    try:
        endphase()
    except:
        print('结束阶段失败')
        sleep(1)
        return finish_phase2(driver,maxRetry-1)

def offline_new_guijiao(driver,patientname,institutions,doctorname):
    '''线下硅胶新病例'''
    sleep(5)
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#accounts_c").send_keys(institutions)
    driver.find_element_by_css_selector("#contacts_c").send_keys(doctorname)
    driver.find_element_by_css_selector("#btn_patients_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_xpath('//*[@id="addformlink"]/input').click()
    driver.find_element_by_css_selector("#name").send_keys(patientname)
    driver.find_element_by_css_selector("#ea_patients_popupcreate_save_button").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    key_trans.switch_to_cur_win(driver)
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    select = Select(driver.find_element_by_css_selector("#express_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#barcode_u_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#barcode_l_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(6)

def offline_new_photo(driver,patientname,institutions,doctorname):
    '''线下新病例口内照不合格'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#accounts_c").send_keys(institutions)
    driver.find_element_by_css_selector("#contacts_c").send_keys(doctorname)
    driver.find_element_by_css_selector("#btn_patients_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_xpath('//*[@id="addformlink"]/input').click()
    driver.find_element_by_css_selector("#name").send_keys(patientname)
    driver.find_element_by_css_selector("#ea_patients_popupcreate_save_button").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[2]/a').click()
    key_trans.switch_to_cur_win(driver)
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("11")
    select = Select(driver.find_element_by_css_selector("#is_qualified_c"))
    select.select_by_value("2")
    driver.find_element_by_id("remark_c").send_keys("我觉得不合格，请重新上传")
    sleep(3)
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(5)
    driver.find_element_by_css_selector("#send_receipt").click()
    sleep(5)
    #driver.switch_to.alert.accept()
    acceptAlert(driver)


def offline_middle_guijiao(driver ,crmusercode):
    '''线下中期硅胶'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    key_trans.switch_to_cur_win(driver)
    select =Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("15")
    select = Select(driver.find_element_by_css_selector("#material_detail_type_c"))
    select.select_by_value("153")
    select = Select(driver.find_element_by_css_selector("#express_type_c"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_css_selector("#is_metal_tray_c"))
    select.select_by_value("1")
    driver.find_element_by_css_selector("#barcode_u_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#barcode_l_c").send_keys(random.randint(1111111111111, 9999999999999))
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    sleep(4)

def offline_middle_photo1(driver ,crmusercode):
    '''线下中期口内照'''
    driver.find_element_by_link_text("病例管理").click()
    driver.find_element_by_link_text("收货记录").click()
    driver.find_element_by_xpath('//*[@id="shortcuts"]/span/span[1]/a/span').click()
    driver.find_element_by_css_selector("#btn_case_id_c").click()
    key_trans.switch_to_win(driver, 1)
    driver.find_element_by_css_selector("#name_advanced").send_keys(crmusercode)
    sleep(3)
    driver.find_element_by_css_selector("#search_form_submit").click()
    driver.find_element_by_xpath('/html/body/table[4]/tbody/tr[3]/td[1]/a').click()
    key_trans.switch_to_cur_win(driver)
    select = Select(driver.find_element_by_css_selector("#material_type_c"))
    select.select_by_value("11")
    select = Select(driver.find_element_by_css_selector("#is_qualified_c"))
    select.select_by_value("2")
    driver.find_element_by_id("remark_c").send_keys("中期口内照不合格，请重新上传")
    driver.find_element_by_css_selector("#SAVE_FOOTER").click()
    #driver.find_element_by_css_selector("#send_receipt").click()
    # sleep(4)
    # driver.switch_to.alert.accept()