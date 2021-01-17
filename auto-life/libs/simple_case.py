from time import sleep
from random import choice
from crm_style.function import upload_photos
from libs.test_utils import readDataFromMySQL,deleteDataFromMySQL


def champion_A6_1(driver,g_config):
    '''冠军版A6本阶段使用A6'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('mainsuit8').click()
    driver.find_element_by_id('treatTarget0').click()
    driver.find_element_by_id('treatTarget7').click()
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
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    sleep(10)

def champion_A6_2(driver,g_config):
    '''冠军版A6后续阶段使用A6'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
    # driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('mainsuit8').click()
    driver.find_element_by_id('treatTarget0').click()
    driver.find_element_by_id('treatTarget7').click()
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
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    sleep(10)

def champion_A6_3(driver,g_config):
    '''冠军版非A6'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('treatTarget0').click()
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
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    sleep(10)

def stand(driver,g_config):
    '''标准版'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[2]').click()
    # driver.switch_to.window(driver.window_handles[1])
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('treatTarget0').click()
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
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
    sleep(18)

def child(driver,g_config):
    '''儿童版'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[3]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('treatTarget0').click()
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
    sleep(10)

def child_A6(driver,g_config):
    '''儿童版A6'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[3]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('mainsuit5').click()
    driver.find_element_by_id('treatTarget0').click()
    driver.find_element_by_id('treatTarget7').click()
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
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    sleep(10)

def child_champion(driver,g_config):
    '''儿童+冠军版'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[4]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('treatTarget0').click()
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

    sleep(10)

def child_champion_A6(driver,g_config):
    '''儿童版+冠军版A6'''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[4]').click()
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index + 1])
    patientname=readDataFromMySQL(g_config)
    deleteDataFromMySQL(g_config)
    driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
    driver.find_element_by_id('female').click()
    driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
    driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
    driver.find_element_by_id('patientBirthdate').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
    driver.find_element_by_id("ansyl").click()
    driver.find_element_by_id("chyj").click()

    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
    sleep(4)

    driver.find_element_by_id('mainsuit0').click()
    driver.find_element_by_id('mainsuit5').click()
    driver.find_element_by_id('treatTarget0').click()
    driver.find_element_by_id('treatTarget7').click()
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
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
    driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/popover[2]/div[1]/div[2]/button').click()
    sleep(10)