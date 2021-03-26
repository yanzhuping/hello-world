from time import sleep
from crm_style.function import *
from random import choice
import random
from selenium.webdriver.support.select import Select

# def login_iortho(driver,username,password,url):
#     print("执行登录")
#     '''登陆iortho'''
#     driver.get(url)
#     # driver.switch_to.frame("the-real-login-page")
#     driver.find_element_by_id("_username").clear()
#     driver.find_element_by_id("_username").send_keys(username)
#     driver.find_element_by_id("_password").clear()
#     driver.find_element_by_id("_password").send_keys(password)
#     driver.find_element_by_id("_btn_login").click()
#     sleep(2)
#     driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
#     sleep(3)
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
#
# def champion_A6_1(driver,g_config):
#     '''冠军版A6本阶段使用A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('mainsuit8').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTarget7').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('A6').click()
#     driver.find_element_by_id('A6_1').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo',14,driver,'pic-1')
#
#
#     driver.find_element_by_id("hasSiliconA61").click()
#     driver.find_element_by_id("hasSiliconA611").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
#     sleep(10)
#
# def champion_A6_2(driver,g_config):
#     '''冠军版A6后续阶段使用A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('mainsuit8').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTarget7').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('A6').click()
#     driver.find_element_by_id('A6_2').click()
#     driver.find_element_by_id('facetype1').click()
#     driver.find_element_by_id('sagittalRight1').click()
#     driver.find_element_by_id('sagittalLeft1').click()
#     driver.find_element_by_id('midline2').click()
#     driver.find_element_by_id('antinail1').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 8, driver, 'pic-1')
#
#     driver.find_element_by_id("hasSilicon1").click()
#     driver.find_element_by_id("hasSilicon2").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
#     sleep(10)

#创建病例的方法使用lib.simple_Case,便于管理
# def login_iortho(driver,username,password,url):
#     print("执行登录")
#     '''登陆iortho'''
#     driver.get(url)
#     # driver.switch_to.frame("the-real-login-page")
#     driver.find_element_by_id("_username").clear()
#     driver.find_element_by_id("_username").send_keys(username)
#     driver.find_element_by_id("_password").clear()
#     driver.find_element_by_id("_password").send_keys(password)
#     driver.find_element_by_id("_btn_login").click()
#     sleep(2)
#     # driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
#     # sleep(3)
#     # driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()

# def champion_A6_1(driver,g_config):
#     '''冠军版A6本阶段使用A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('mainsuit8').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTarget7').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('A6').click()
#     driver.find_element_by_id('A6_1').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo',14,driver,'pic-1')
#
#
#     driver.find_element_by_id("hasSiliconA61").click()
#     driver.find_element_by_id("hasSiliconA611").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
#     sleep(10)
#
# def champion_A6_2(driver,g_config):
#     '''冠军版A6后续阶段使用A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('mainsuit8').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTarget7').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('A6').click()
#     driver.find_element_by_id('A6_2').click()
#     driver.find_element_by_id('facetype1').click()
#     driver.find_element_by_id('sagittalRight1').click()
#     driver.find_element_by_id('sagittalLeft1').click()
#     driver.find_element_by_id('midline2').click()
#     driver.find_element_by_id('antinail1').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 8, driver, 'pic-1')
#
#     driver.find_element_by_id("hasSilicon1").click()
#     driver.find_element_by_id("hasSilicon2").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
#     sleep(10)
#
# def champion_A6_3(driver,g_config):
#     '''冠军版非A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[1]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('facetype1').click()
#     driver.find_element_by_id('sagittalRight1').click()
#     driver.find_element_by_id('sagittalLeft1').click()
#     driver.find_element_by_id('midline2').click()
#     driver.find_element_by_id('antinail1').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 8, driver, 'pic-1')
#
#     driver.find_element_by_id("hasSilicon1").click()
#     driver.find_element_by_id("hasSilicon2").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
#     sleep(10)
#
# def stand(driver,g_config):
#     '''标准版'''
#     print("运行这个方法")
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[2]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit3').click()
#     driver.find_element_by_id('mainsuit6').click()
#     driver.find_element_by_id('treatTarget3').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('facetype1').click()
#     driver.find_element_by_id('sagittalRight1').click()
#     driver.find_element_by_id('sagittalLeft1').click()
#     driver.find_element_by_id('midline2').click()
#     driver.find_element_by_id('antinail1').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo',8,driver,'pic-1')
#     sleep(1)
#
#     driver.find_element_by_id("hasSilicon1").click()
#     driver.find_element_by_id("hasSilicon2").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/adult-new-case/div[2]/div/button[3]').click()
#     sleep(18)
#     driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]').click()
#     sleep(2)
#
# def child(driver,g_config):
#     '''儿童版'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[3]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('teenagers-tooth-55-0').click()
#     driver.find_element_by_id('teenagers-tooth-65-0').click()
#     driver.find_element_by_id('teenagers-tooth-85-0').click()
#     driver.find_element_by_id('teenagers-tooth-75-0').click()
#     driver.find_element_by_id('teenagers-tooth-18-0').click()
#     driver.find_element_by_id('teenagers-tooth-48-0').click()
#     driver.find_element_by_id('teenagers-tooth-28-0').click()
#     driver.find_element_by_id('teenagers-tooth-38-0').click()
#     driver.find_element_by_id('sagittal1').click()
#     driver.find_element_by_id('midline3').click()
#     driver.find_element_by_id('noPulltooth0').click()
#     driver.find_element_by_id('muscleTrainer0').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 8, driver, 'pic-1')
#     sleep(1)
#
#     driver.find_element_by_id("hasSilicon1").click()
#     driver.find_element_by_id("hasSilicon2").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
#     sleep(20)
#
# def child_A6(driver,g_config):
#     '''儿童版A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[3]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('mainsuit5').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTarget7').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('A6').click()
#     driver.find_element_by_id('teenagers-tooth-55-0').click()
#     driver.find_element_by_id('teenagers-tooth-65-0').click()
#     driver.find_element_by_id('teenagers-tooth-85-0').click()
#     driver.find_element_by_id('teenagers-tooth-75-0').click()
#     driver.find_element_by_id('teenagers-tooth-18-0').click()
#     driver.find_element_by_id('teenagers-tooth-48-0').click()
#     driver.find_element_by_id('teenagers-tooth-28-0').click()
#     driver.find_element_by_id('teenagers-tooth-38-0').click()
#     driver.find_element_by_id('midline2').click()
#     driver.find_element_by_id('noPulltooth0').click()
#     driver.find_element_by_id('muscleTrainer0').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 14, driver, 'pic-1')
#     sleep(1)
#
#     driver.find_element_by_id("hasSiliconA61").click()
#     driver.find_element_by_id("hasSiliconA611").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
#     sleep(10)
#
# def child_champion(driver,g_config):
#     '''儿童+冠军版'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[4]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('teenagers-tooth-55-0').click()
#     driver.find_element_by_id('teenagers-tooth-65-0').click()
#     driver.find_element_by_id('teenagers-tooth-85-0').click()
#     driver.find_element_by_id('teenagers-tooth-75-0').click()
#     driver.find_element_by_id('teenagers-tooth-18-0').click()
#     driver.find_element_by_id('teenagers-tooth-48-0').click()
#     driver.find_element_by_id('teenagers-tooth-28-0').click()
#     driver.find_element_by_id('teenagers-tooth-38-0').click()
#     driver.find_element_by_id('sagittal1').click()
#     driver.find_element_by_id('midline3').click()
#     driver.find_element_by_id('noPulltooth0').click()
#     driver.find_element_by_id('muscleTrainer0').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 8, driver, 'pic-1')
#     sleep(1)
#
#     driver.find_element_by_id("hasSilicon1").click()
#     driver.find_element_by_id("hasSilicon2").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/popover[2]/div[1]/div[2]/button').click()
#
#     sleep(10)
#
# def child_champion_A6(driver,g_config):
#     '''儿童版+冠军版A6'''
#     driver.find_element_by_xpath(
#         '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[4]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     patientname=readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="required-1"]/input').send_keys(patientname)
#     driver.find_element_by_id('female').click()
#     driver.find_element_by_css_selector('#required-2 > div:nth-child(2) > div').click()
#     driver.find_element_by_css_selector('#required-2 > div.teenagers-info-orgs-box > ul > li:nth-child(1)').click()
#     driver.find_element_by_id('patientBirthdate').click()
#     driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/table/tbody/tr[1]/td[7]').click()
#     driver.find_element_by_id("ansyl").click()
#     driver.find_element_by_id("chyj").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     driver.find_element_by_id('mainsuit0').click()
#     driver.find_element_by_id('mainsuit5').click()
#     driver.find_element_by_id('treatTarget0').click()
#     driver.find_element_by_id('treatTarget7').click()
#     driver.find_element_by_id('treatTooth1').click()
#     driver.find_element_by_id('A6').click()
#     driver.find_element_by_id('teenagers-tooth-55-0').click()
#     driver.find_element_by_id('teenagers-tooth-65-0').click()
#     driver.find_element_by_id('teenagers-tooth-85-0').click()
#     driver.find_element_by_id('teenagers-tooth-75-0').click()
#     driver.find_element_by_id('teenagers-tooth-18-0').click()
#     driver.find_element_by_id('teenagers-tooth-48-0').click()
#     driver.find_element_by_id('teenagers-tooth-28-0').click()
#     driver.find_element_by_id('teenagers-tooth-38-0').click()
#     driver.find_element_by_id('midline2').click()
#     driver.find_element_by_id('noPulltooth0').click()
#     driver.find_element_by_id('muscleTrainer0').click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     sleep(4)
#
#     upload_photos('photo', 14, driver, 'pic-1')
#     sleep(1)
#
#     driver.find_element_by_id("hasSiliconA61").click()
#     driver.find_element_by_id("hasSiliconA611").click()
#
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[2]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/div[2]/div/button[3]').click()
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-teenagers/popover[2]/div[1]/div[2]/button').click()
#     sleep(10)


# def comfos_case(driver,username,password,url,g_config):
#     driver.get(url)
#     sleep(1)
#     driver.find_element_by_id("_username").send_keys(username)
#     driver.find_element_by_id("_password").send_keys(password)
#     driver.find_element_by_id("_btn_login").click()
#     sleep(2)
#     driver.find_element_by_xpath('//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[2]').click()
#     driver.switch_to.window(driver.window_handles[1])
#     sleep(1.5)
#     patientname = readDataFromMySQL(g_config)
#     deleteDataFromMySQL(g_config)
#     driver.find_element_by_xpath('//*[@id="info_page_form"]/div/form/div/div[1]/div[1]/ul/li[1]/input').send_keys(patientname)
#
#     driver.find_element_by_id('sexm').click()
#     driver.find_element_by_id('birthdate').send_keys("2019-10-26")
#     driver.find_element_by_xpath('//*[@id="info_page_form"]/div/form/div/div[1]/div[1]/ul/li[3]/label/span[2]').click()
#     Select(driver.find_element_by_css_selector("#info_page_form > div > form > div > div.content_form.relative > div.instInfo > ul > li > div.select_down.ng-scope > select")).select_by_value("0")
#     driver.find_element_by_xpath('//*[@id="info_page_form"]/div/form/div/div[3]/img[2]').click()
#     driver.find_element_by_xpath('//*[@id="options_page_form"]/div/div/div[1]/ul/li/label').click()
#     driver.find_element_by_xpath('//*[@id="options_page_form"]/div/div/div[2]/img[2]').click()
#     driver.find_element_by_xpath('//*[@id="options_page_form"]/div/div/div[2]/img[2]').click()
#
#     photos=driver.find_element_by_name('photo')
#     a=0
#     while a<12:
#         a=a+1
#         photos.send_keys(choice(choice_file('photo')))
#         photos.clear()
#         sleep(0.5)
#         # 定义变量
#     source_xpath = '//*[@id="one"]/imagephotos/div[1]/img'
#     target_list = []
#     target_list.append(driver.find_element_by_id("1"))
#     target_list.append(driver.find_element_by_id("2"))
#     target_list.append(driver.find_element_by_id("3"))
#     target_list.append(driver.find_element_by_id("4"))
#     target_list.append(driver.find_element_by_id("5"))
#     target_list.append(driver.find_element_by_id("6"))
#     target_list.append(driver.find_element_by_id("7"))
#     target_list.append(driver.find_element_by_id("8"))
#     # 拖拽图片
#     choose_pic(driver, source_xpath, target_list, 10,80)
#
#     print(">>>照片拖拽完成......")
#
#     driver.find_element_by_xpath('//*[@id="photo_page_form"]/div/div/div[2]/img[2]').click()
#     driver.find_element_by_xpath('//*[@id="ray_page_form"]/div/div[2]/img[2]').click()
#
#     driver.find_element_by_xpath('//*[@id="scroll0"]/div/div[1]/div/label').click()
#     driver.find_element_by_xpath('//*[@id="scroll1"]/div[1]/div[1]/div/label').click()
#     driver.find_element_by_xpath('//*[@id="scroll2"]/div/div[1]/label').click()
#     driver.find_element_by_xpath('//*[@id="scroll7"]/div[1]/div[2]/label').click()
#     driver.find_element_by_xpath('//*[@id="scroll7"]/div[2]/div[2]/label').click()
#     driver.find_element_by_id('zx_3d').click()
#     driver.find_element_by_id('booleanCorrection').click()
#     driver.find_element_by_id('booleanMaxillary').click()
#     driver.find_element_by_xpath('//*[@id="process_page_form"]/div/div[2]/img[2]').click()
#     driver.find_element_by_xpath('//*[@id="result_page_form"]/div/div/div[1]/div/ul[1]/li[1]/div/label').click()
#     driver.find_element_by_xpath('//*[@id="result_page_form"]/div/div/div[2]/div/input[2]').click()
#     sleep(10)
