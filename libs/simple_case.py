from time import sleep,ctime
from random import choice
from crm_style.function import upload_photos
from libs.test_utils import readDataFromMySQL,deleteDataFromMySQL
from libs.global_vars import *
import libs.keywords_trans as key_trans
import os
import time


def champion_A6_1(driver,g_config):
    '''冠军版A6本阶段使用A6'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(2)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_css_selector('[lay-ymd="2000-1-7"]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('mainsuit9').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTarget8').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('A6').click()
    driver.find_element_by_id('A6_1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 14, driver, 'pic-1')
    sleep(1)

    driver.find_element_by_id("hasSiliconA61").click()
    driver.find_element_by_id("hasSiliconA611").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    sleep(10)
    print("创建的病例名称：", patientname)

def champion_A6_2(driver,g_config):
    '''冠军版A6后续阶段使用A6'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(2)"]').click()
    # driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('mainsuit9').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTarget8').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('A6').click()
    driver.find_element_by_id('A6_2').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    print("创建的病例名称：", patientname)
    sleep(10)

def champion_A6_3(driver,g_config):
    '''冠军版非A6'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(2)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('mainsuit9').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTarget8').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')
    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    print("创建的病例名称：", patientname)
    sleep(10)

def stand(driver,g_config):
    '''标准版'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(10)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(1)"]').click()
    # #driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    sleep(1)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_css_selector('[lay-ymd="2000-1-7"]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(5)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')


    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()
    #点击3shape
    driver.find_element_by_css_selector('[for="hasSilicon61"],[for="hasSilicon6"]').click()
    #切换ifame
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="iortho_3shape_select"]'))
    sleep(2)
    driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[3]/div[2]/div[3]/div[4]/div[1]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.confirmSelect()"]').click()
    driver.switch_to.parent_frame()
    #点击邮件发送
    #driver.find_element_by_css_selector('[ng-click="$ctrl.checkModel(5)"]').click()
    sleep(2)
    # driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.changeNav($ctrl.verifyMarkObj.index+1)"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    sleep(10)
    print("创建的病例名称：",patientname)
    return patientname

def stand_detail(driver,g_config):
    '''标准版'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(1)"]').click()
    # #driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    sleep(1)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_css_selector('[lay-ymd="2000-1-7"]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')
    sleep(1)
    upload_photos('xguan', 2, driver, 'pic-2')

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()
    #点击3shape
    driver.find_element_by_css_selector('[for="hasSilicon6"],[for="hasSilicon61"]').click()
    #切换ifame
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="iortho_3shape_select"]'))
    sleep(2)
    driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[3]/div[2]/div[3]/div[4]/div[1]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.confirmSelect()"]').click()
    driver.switch_to.parent_frame()
    #点击邮件发送
    #driver.find_element_by_css_selector('[ng-click="$ctrl.checkModel(5)"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    #隐士等待点击弹框
    try:
        print(ctime())
        driver.implicitly_wait(30)
        sleep(5)
        # 关闭提交成功x
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]').click()
        sleep(3)
        all_handles = driver.window_handles
        print(all_handles)
        # 点击病例列表case
        driver.find_element_by_css_selector('[ng-mouseenter="$ctrl.mouseEnterHandler()"]').click()
        sleep(4)
        print(all_win,cur_win)
        all_win = driver.window_handles
        # 打印当前操作界面的句柄
        cur_win = driver.current_window_handle
        print('current_handle', cur_win)
        driver.implicitly_wait(5)  # 如果找到了就继续，否则2秒等待
        # 拿到新窗口句柄
        newhandle = [handle for handle in all_win if handle not in all_handles]
        # 打印新窗口
        print('newhandle', newhandle[0])
        # 切换到新窗口
        driver.switch_to.window(newhandle[0])
        time.sleep(5)
        # 打印新窗口的title
        print('新窗口的title：', driver.title)
        # index = all_win.index(cur_win)
        # driver.switch_to.window(all_win[index + 1])
        #driver.find_element_by_css_selector('[ng-click="$ctrl.accpet()"]').click()
        if len(driver.window_handles)>1:
            key_trans.close_tab(driver, len(driver.window_handles)-1)
            print('新建病例后当前总窗口数目：',driver.window_handles)
            print('新窗口的title：', driver.title)
    except Exception as e:
        print(e)
    finally:
        print(ctime())
    return patientname

def stand_es(driver,g_config):
    '''标准版'''
    sleep(2)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    sleep(1)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_css_selector('[lay-ymd="2000-1-7"]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()
    #点击3shape
    driver.find_element_by_css_selector('[for="hasSilicon6"],[for="hasSilicon61"]').click()
    #切换ifame
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="iortho_3shape_select"]'))
    sleep(2)
    driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[3]/div[2]/div[3]/div[4]/div[1]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.confirmSelect()"]').click()
    driver.switch_to.parent_frame()
    #点击邮件发送
    #driver.find_element_by_css_selector('[ng-click="$ctrl.checkModel(5)"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    # sleep(18)
    return patientname

def stand_cbct(driver,g_config):
    '''标准版'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(1)"]').click()
    # #driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    sleep(1)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_css_selector('[lay-ymd="2000-1-7"]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()
    #点击cbct
    driver.find_element_by_id('toothRootDesign0').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()
    #点击3shape
    driver.find_element_by_css_selector('[for="hasSilicon6"],[for="hasSilicon61"]').click()
    #切换ifame
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="iortho_3shape_select"]'))
    sleep(2)
    driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[3]/div[2]/div[3]/div[4]/div[1]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.confirmSelect()"]').click()
    driver.switch_to.parent_frame()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    print('-----------')
    print(all_win,cur_win)
    driver.find_element_by_css_selector('[for="cbct"]').click()
    # # 当前打开的所有窗口
    # windows = driver.window_handles
    # # 转换到最新打开的窗口
    # driver.switch_to.window(windows[-1])
    sleep(2)
    print(key_trans.get_root_path())
    print(key_trans.get_root_path()+"/test_data/cbct/shm1.zip")

    driver.find_element_by_css_selector('[ng-click="$ctrl.uploadFile()"]').send_keys(key_trans.get_root_path()+"/test_data/cbct/shm1.zip")

    sleep(180)
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    print(all_win,cur_win)
    print('-----------')
    #点击完成
    driver.find_element_by_css_selector('[for="cbct"]').click()
    driver.switch_to.parent_frame()

    #点击邮件发送
    #driver.find_element_by_css_selector('[ng-click="$ctrl.checkModel(5)"]').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    # sleep(18)
    return patientname

def child(driver,g_config):
    '''儿童版'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(10)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterChildCase(5)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit1').click()
    driver.find_element_by_id('treatTarget1').click()
    driver.find_element_by_id('treatTooth1').click()
    # driver.find_element_by_id('teenagers-tooth-55-0').click()
    # driver.find_element_by_id('teenagers-tooth-65-0').click()
    # driver.find_element_by_id('teenagers-tooth-85-0').click()
    # driver.find_element_by_id('teenagers-tooth-75-0').click()
    # driver.find_element_by_id('teenagers-tooth-18-0').click()
    # driver.find_element_by_id('teenagers-tooth-48-0').click()
    # driver.find_element_by_id('teenagers-tooth-28-0').click()
    # driver.find_element_by_id('teenagers-tooth-38-0').click()
    driver.find_element_by_id('sagittal1').click()
    driver.find_element_by_id('midline3').click()
    driver.find_element_by_id('noPulltooth0').click()
    driver.find_element_by_id('muscleTrainer0').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')
    sleep(1)

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    print("创建的病例名称：", patientname)
    sleep(10)

def child_A6(driver,g_config):
    '''儿童版A6'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(10)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterChildCase(5)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit1').click()
    driver.find_element_by_id('mainsuit6').click()
    driver.find_element_by_id('treatTarget1').click()
    driver.find_element_by_id('treatTarget8').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('A6').click()
    # driver.find_element_by_id('teenagers-tooth-55-0').click()
    # driver.find_element_by_id('teenagers-tooth-65-0').click()
    # driver.find_element_by_id('teenagers-tooth-85-0').click()
    # driver.find_element_by_id('teenagers-tooth-75-0').click()
    # driver.find_element_by_id('teenagers-tooth-18-0').click()
    # driver.find_element_by_id('teenagers-tooth-48-0').click()
    # driver.find_element_by_id('teenagers-tooth-28-0').click()
    # driver.find_element_by_id('teenagers-tooth-38-0').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('noPulltooth0').click()
    driver.find_element_by_id('muscleTrainer0').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 14, driver, 'pic-1')
    sleep(1)

    driver.find_element_by_id("hasSiliconA61").click()
    driver.find_element_by_id("hasSiliconA611").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    print("创建的病例名称：", patientname)
    sleep(10)


#新建儿童版K1病例
def child_K1(driver,g_config):
    '''儿童版K1'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterChildCase(8)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit1').click()
    driver.find_element_by_id('treatTarget1').click()
    driver.find_element_by_id('treatTooth1').click()
    # driver.find_element_by_id('teenagers-tooth-55-0').click()
    # driver.find_element_by_id('teenagers-tooth-65-0').click()
    # driver.find_element_by_id('teenagers-tooth-85-0').click()
    # driver.find_element_by_id('teenagers-tooth-75-0').click()
    # driver.find_element_by_id('teenagers-tooth-18-0').click()
    # driver.find_element_by_id('teenagers-tooth-48-0').click()
    # driver.find_element_by_id('teenagers-tooth-28-0').click()
    # driver.find_element_by_id('teenagers-tooth-38-0').click()
    driver.find_element_by_id('sagittal1').click()
    driver.find_element_by_id('midline3').click()
    driver.find_element_by_id('noPulltooth0').click()
    driver.find_element_by_id('muscleTrainer0').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')
    sleep(1)

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    print("创建的病例名称：", patientname)
    sleep(10)







def child_champion(driver,g_config):
    '''儿童+冠军版'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterChildCase(7)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit1').click()
    driver.find_element_by_id('treatTarget1').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('teenagers-tooth-55-0').click()
    driver.find_element_by_id('teenagers-tooth-65-0').click()
    driver.find_element_by_id('teenagers-tooth-85-0').click()
    driver.find_element_by_id('teenagers-tooth-75-0').click()
    driver.find_element_by_id('teenagers-tooth-18-0').click()
    driver.find_element_by_id('teenagers-tooth-48-0').click()
    driver.find_element_by_id('teenagers-tooth-28-0').click()
    driver.find_element_by_id('teenagers-tooth-38-0').click()
    driver.find_element_by_id('sagittal1').click()
    driver.find_element_by_id('midline3').click()
    driver.find_element_by_id('noPulltooth0').click()
    driver.find_element_by_id('muscleTrainer0').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')
    sleep(1)

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/popover[2]/div[1]/div[2]/button').click()
    print("创建的病例名称：", patientname)
    sleep(10)

def child_champion_A6(driver,g_config):
    '''儿童版+冠军版A6'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterChildCase(7)"]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit1').click()
    driver.find_element_by_id('mainsuit6').click()
    driver.find_element_by_id('treatTarget1').click()
    driver.find_element_by_id('treatTarget8').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('A6').click()
    driver.find_element_by_id('teenagers-tooth-55-0').click()
    driver.find_element_by_id('teenagers-tooth-65-0').click()
    driver.find_element_by_id('teenagers-tooth-85-0').click()
    driver.find_element_by_id('teenagers-tooth-75-0').click()
    driver.find_element_by_id('teenagers-tooth-18-0').click()
    driver.find_element_by_id('teenagers-tooth-48-0').click()
    driver.find_element_by_id('teenagers-tooth-28-0').click()
    driver.find_element_by_id('teenagers-tooth-38-0').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('noPulltooth0').click()
    driver.find_element_by_id('muscleTrainer0').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 14, driver, 'pic-1')
    sleep(1)

    driver.find_element_by_id("hasSiliconA61").click()
    driver.find_element_by_id("hasSiliconA611").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/popover[2]/div[1]/div[2]/button').click()
    print("创建的病例名称：", patientname)
    sleep(10)

def comfos(driver,g_config):
    '''comfos'''
    sleep(2)
    driver.find_element_by_xpath('//*[text()="病例"]').click()
    sleep(3)
    driver.find_element_by_css_selector(
        '[translate="caselist.new_patient"]').click()
    driver.find_element_by_css_selector(
        '[ng-click="$ctrl.enterNewCase(21)"]').click()
    # #driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    sleep(1)
    driver.find_element_by_id('female').click()
    sleep(1)
    driver.find_element_by_css_selector('[placeholder="请选择医疗机构"]').click()
    sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="required-2"]/div[2]/ul/li[1]/span').click()
    except:
        pass
    sleep(2)
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_css_selector('[lay-ymd="2000-1-7"]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit3').click()
    driver.find_element_by_id('treatTarget3').click()
    driver.find_element_by_id('treatTooth1').click()
    driver.find_element_by_id('facetype1').click()
    driver.find_element_by_id('sagittalRight1').click()
    driver.find_element_by_id('sagittalLeft1').click()
    driver.find_element_by_id('midline2').click()
    driver.find_element_by_id('antinail1').click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    upload_photos('photo', 8, driver, 'pic-1')

    driver.find_element_by_id("hasSilicon1").click()
    driver.find_element_by_id("hasSilicon2").click()
    #点击3shape
    driver.find_element_by_css_selector('[for="hasSilicon61"]').click()
    #切换ifame
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@class="iortho_3shape_select"]'))
    sleep(2)
    driver.find_element_by_xpath('/html/body/ui-view/div/new-order/dialog-threeshap/div/div[3]/div[2]/div[3]/div[4]/div[1]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.confirmSelect()"]').click()
    driver.switch_to.parent_frame()
    #点击邮件发送
    #driver.find_element_by_css_selector('[ng-click="$ctrl.checkModel(5)"]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(5)
    # driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    driver.find_element_by_css_selector('[ng-click="$ctrl.checkA6Submit()"]').click()
    print("创建的病例名称：", patientname)
    sleep(10)
    return patientname