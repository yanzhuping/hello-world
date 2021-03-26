# from telnetlib import EC

import pymysql
from time import sleep
from time import strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def process_orders(driver):
    '''3D全设计确认后，将订单变成执行中，并复制订单号'''
    nowdate=strftime('%Y-%m-%d')
    sleep(2)
    # 点击新病例阶段
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    print('111111111111111111')
    try:
        sleep(1)
        #点击生产加工单单号
        driver.find_element_by_xpath(
            '//*[@id="list_subpanel_ea_stage_ea_production_1"]/table/tbody/tr[3]/td[1]/span/a').click()
        # driver.find_element_by_xpath('//*[@id="list_subpanel_ea_stage_ea_production_1"]/table/tbody/tr[7]/td[1]/span/a').click()
    except Exception as e:
        print('1异常情况：', e)
    orderid = driver.find_element_by_id("name").text
    print(orderid)
    driver.find_element_by_id("edit_button").click()
    driver.find_element_by_id("expire_date_c").click()
    driver.find_element_by_id("expire_date_c").clear()
    driver.find_element_by_id("expire_date_c").send_keys(nowdate)
    driver.find_element_by_id("SAVE_HEADER").click()
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        #执行定时器脚本
        js=r'window.open("http://crm-web-sit.eainc.com/crm/auto_erp.php")'
        driver.execute_script(js)
        sleep(10)
        print('执行crm定时器脚本auto_erp.php成功')
        # #关闭当前窗口
        # driver.close()
        driver.switch_to_window(driver.window_handles[0])
        driver.find_element_by_id('send_production').click()
        sleep(1)
        acceptAlert(driver)
    # except:
    #     js='window.open("crm-web.sh-sit.eainc.com/crm/auto_erp.php")'
    #     driver.execute_script(js)
    #     sleep(10)
    #     driver.switch_to_window(driver.window_handles[0])
    # try:
    #     driver.set_page_load_timeout(10)
    #     driver.find_element_by_id("logout_link").click()
    except Exception as e:
        # driver.execute_script("window.stop()")
        print('2异常情况：', e)

    return orderid
def acceptAlert(driver):
    '''有时候有多个alert连续存在'''
    i=0
    j=0
    while i<3:
        i=i+1
        try:
            sleep(1)
            alert = driver.switch_to.alert
            if alert:
                sleep(1.5)
                alert.accept()
                j+=1
                print('关闭几次alert：', j)
        except:
            pass
        sleep(0.5)
def process_orders_1(driver):
    '''3D全设计确认后，将订单变成执行中，并复制订单号'''
    nowdate=strftime('%Y-%m-%d')
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_stage_ea_production_1"]/table/tbody/tr[4]/td[1]/span/a').click()
    orderid=driver.find_element_by_id("name").text
    print(orderid)
    #进入生产加工单编辑模块
    driver.find_element_by_id("edit_button").click()
    driver.find_element_by_id("expire_date_c").click()
    driver.find_element_by_id("expire_date_c").clear()
    driver.find_element_by_id("expire_date_c").send_keys(nowdate)
    driver.find_element_by_id("SAVE_HEADER").click()
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    try:
        driver.find_element_by_id('send_production').click()
        driver.switch_to.alert.accept()
        sleep(1.5)
        driver.switch_to.alert.accept()
    except:
        js='window.open("crm-web.sit.eainc.com/crm/auto_erp.php")'
        driver.execute_script(js)
        sleep(10)
        driver.switch_to_window(driver.window_handles[0])
    try:
        driver.set_page_load_timeout(10)
        driver.find_element_by_id("logout_link").click()
    except:
        driver.execute_script("window.stop()")
    return orderid



# def unstarted_production(driver,orderid):
#     '''未开启生产'''
#     driver.find_element_by_id("productionOrders").click()  #导航的“未开启生产
#     driver.find_element_by_name("productNum_1").clear()
#     driver.find_element_by_name("productNum_1").send_keys(orderid)  #输入生产加工单编码
#     driver.find_element_by_id("search-1").click() #检索
#     sleep(2)
#     driver.find_element_by_name("page-select-1").click() #选中
#     driver.find_element_by_class_name("btn.btn-primary.turnNextLevel").click()
#     sleep(1)
#     driver.find_element_by_class_name("confirm").click()
#     sleep(1)

def connect_to_the_database(orderid):
    '''发货连接数据库'''
    db = pymysql.Connect(host="192.168.37.108", port=3306, user="erpdb_sh_sit",passwd="erpdb_sh_sit", db="erpdb_sh_sit", charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)
    sql_1 = "update erp_order set is_sent_to_mes='1' where produce_Id= '%s'"%(orderid)
    cursor.execute(sql_1)
    sql_2 = "update erp_order set produce_state='04' where produce_Id= '%s'" % (orderid)
    cursor.execute(sql_2)
    db.commit()
    db.close()
def find_msgType_database(caseid):
    db = pymysql.Connect(host="192.168.37.113", port=3306, user="opm_sh_sit",passwd="opm_sh_sit", db="opm_sh_sit", charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)
    sql="SELECT msgType FROM `opm_statetidingsinitial` where crmCaseCode='%s' ORDER BY actionDate desc limit 3"%(caseid)

    print(sql)
    cursor.execute(sql)
    sleep(10)
    results = cursor.fetchall()
    return str(results)

def find_msgType_crmUserCode(crmUserCode):
    db = pymysql.Connect(host="192.168.37.113", port=3306, user="opm_sh_sit", passwd="opm_sh_sit", db="opm_sh_sit",
                         charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)
    sql = "SELECT msgType FROM `opm_statetidingsinitial` where crmUserCode='%s' ORDER BY actionDate desc limit 1" % (
        crmUserCode)

    print(sql)
    cursor.execute(sql)
    sleep(10)
    results = cursor.fetchall()
    return str(results)

    #i=0
    # try:
    #     while i <40:
    #         sleep(10)
    #         print(f'{i}查询等待10s')
    #         results = cursor.fetchall()
    #         print('循环外消息结果：',results)
    #         #assertcrms=[]
    #         print(results)
    #         if results!=():
    #             sleep(10)
    #             print('等待10s后，循环内消息结果：', results)
    #             results = cursor.fetchall()
    #             return str(results)
    #             # for result in results:
    #             #     assertcrms.append(result[0])
    #             # return assertcrms
    #         else:
    #             i+=1
    # except Exception as e:
    #     print('未获取到消息报错',e)
    # #results = cursor.fetchall()
    # return results[0]

def database_manual_tooth_throwing(caseid):
    '''连接数据库,数据库手动抛牙'''
    db = pymysql.Connect(host="erp-db.sh-sit.eainc.com", port=3306, user="mes",passwd="mes", db="msm_sh_sit", charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)

    sql_1= "SELECT task_id FROM `msm_model_task_parameter` WHERE _value LIKE '%s' order by task_id desc"%(caseid)
    print(sql_1)
    sleep(60)
    for i in range(10):
        cursor.execute(sql_1)
        results = cursor.fetchall()
        print(i,results)
        if results :
            break
        else:
            sleep(5)
    try:
        task_id=results[0][0]
        sql_2 = "UPDATE msm_model_task SET task_status ='error' WHERE task_id IN('%s')" % (task_id)
        print(sql_2)
        cursor.execute(sql_2)
        sql_3 = "INSERT INTO `msm_send_message`(`task_id`, `message_type`, `status`, `create_time`) VALUES ('%s', 'autosegment_mq', 0, NOW());" % (
            task_id)
        # 执行sql语句
        cursor.execute(sql_3)
        # 提交到数据库执行
        db.commit()

    except Exception as e:
        print("错误类型是： ",e)
        # Rollback in case there is any error
        db.rollback()
    db.commit()
    db.close()
def database_root_fusion_throwing(caseid):
    '''连接数据库,数据库牙根融合消息'''
    db = pymysql.Connect(host="erp-db.sh-sit.eainc.com", port=3306, user="mes",passwd="mes", db="msm_sh_sit", charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)

    sql_1= "SELECT task_id FROM `msm_model_task_parameter` WHERE _value LIKE '%s' order by task_id desc"%(caseid)
    print(sql_1)
    sleep(60)
    for i in range(10):
        cursor.execute(sql_1)
        results = cursor.fetchall()
        print(i,results)
        if results :
            break
        else:
            sleep(5)
    try:
        task_id=results[0][0]
        sql_2 = "UPDATE msm_model_task SET task_status ='error' WHERE task_id IN('%s')" % (task_id)
        print(sql_2)
        cursor.execute(sql_2)
        sql_3 = "INSERT INTO `msm_send_message`(`task_id`, `message_type`, `status`, `create_time`) VALUES ('%s', 'generateRoot', 0, NOW());" % (
            task_id)
        # 执行sql语句
        cursor.execute(sql_3)
        # 提交到数据库执行
        db.commit()

    except Exception as e:
        print("错误类型是： ",e)
        # Rollback in case there is any error
        db.rollback()
    db.commit()
    db.close()
def database_torque_compensation(caseid):
    '''连接数据库,转矩补偿'''
    db = pymysql.Connect(host="erp-db.sh-sit.eainc.com", port=3306, user="mes",passwd="mes", db="msm_sh_sit", charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)

    sql_1= "SELECT task_id FROM `msm_model_task_parameter` WHERE _value LIKE '%s' order by task_id desc"%(caseid)
    print(sql_1)
    sleep(60)
    for i in range(10):
        cursor.execute(sql_1)
        results = cursor.fetchall()
        print(i,results)
        if results :
            break
        else:
            sleep(5)
    try:
        task_id=results[0][0]
        sql_2 = "UPDATE msm_model_task SET task_status ='error' WHERE task_id IN('%s')" % (task_id)
        print(sql_2)
        cursor.execute(sql_2)
        sql_3 = "INSERT INTO `msm_send_message`(`task_id`, `message_type`, `status`, `create_time`) VALUES ('%s', 'compensationMq', 0, NOW());" % (
            task_id)
        # 执行sql语句
        cursor.execute(sql_3)
        # 提交到数据库执行
        db.commit()

    except Exception as e:
        print("错误类型是： ",e)
        # Rollback in case there is any error
        db.rollback()
    db.commit()
    db.close()


def login_erp(driver):
    '''登录erp系统'''
    try:
        driver.set_page_load_timeout(15)
        driver.get("http://erp-web.sh-sit.eainc.com:8080/erp/erpweb/HTML/index.html")
        driver.find_element_by_css_selector(".log_out").click()
        driver.set_page_load_timeout(10)
    except:
        pass
    try:
        driver.find_element_by_css_selector("#username").send_keys("zhengyan")
        driver.find_element_by_css_selector("#password").send_keys("123456")
        driver.find_element_by_css_selector(".btn-submit").click()
        sleep(3)
        driver.refresh()
        print('zhengyan登录erp系统成功')
    except Exception as e:
        driver.execute_script("window.stop()")
        print('异常情况：',e)


# def pump_shell_marking(driver,orderid):
#     '''抽壳打标'''
#     driver.find_element_by_id("shellMarking").click()
#     sleep(1)
#     driver.find_element_by_name("productNum_2").clear()
#     driver.find_element_by_name("productNum_2").send_keys(orderid)
#     driver.find_element_by_id("search-2").click()
#     sleep(2)
#     driver.find_element_by_xpath('//*[@id="content_shellMarking"]/form/div/div[3]/div[4]/button').click()
#     sleep(1.5)
#     driver.find_element_by_class_name("confirm").click()
#     sleep(1.5)
#
# def product_inspection(driver,orderid):
#     '''产品检验'''
#     driver.find_element_by_id("openProduction").click()
#     driver.find_element_by_name("productNum_3").clear()
#     driver.find_element_by_name("productNum_3").send_keys(orderid)
#     driver.find_element_by_id("search-3").click()
#     sleep(2)
#     driver.find_element_by_xpath('//*[@id="dataTable-3"]/tbody/tr/td[2]/a').click()
#     sleep(1)
#     driver.find_element_by_id("test_step_upper").send_keys('1')
#     driver.find_element_by_name("test_step_lower").send_keys('1')
#     driver.find_element_by_name("test_num").send_keys('2')
#     driver.find_element_by_xpath('//*[@id="alignerDiv"]/div[1]/div/button[1]').click()
#     driver.find_element_by_name("checkInformation").click()
#     driver.find_element_by_xpath('//*[@id="myModal"]/div/div/div[3]/div/div[5]/button').click()
#     sleep(1.5)
#     driver.find_element_by_class_name("confirm").click()
#     sleep(1.5)
#
# def outsourcing(driver,orderid):
#     '''外包'''
#     driver.find_element_by_id("deliverGoods").click()
#     driver.find_element_by_name("productNum_4").clear()
#     driver.find_element_by_name("productNum_4").send_keys(orderid)
#     driver.find_element_by_id("search-4").click()
#     driver.find_element_by_name("deliver_printing").click()
#     sleep(1.5)
#     driver.find_element_by_class_name("confirm").click()
#     sleep(1.5)
#
# def audit(driver,orderid):
#     '''审核'''
#     driver.find_element_by_id("release").click()
#     driver.find_element_by_css_selector("[value='%s']"%orderid).click()
#     driver.find_element_by_xpath('//*[@id="content_release"]/form/div/div[1]/div/button').click()
#     sleep(1.5)
#     driver.find_element_by_class_name("confirm").click()
#     sleep(1.5)
#
# # def logout(driver,username,password):
#     '''退出erp并登陆贺燕的账号'''
#     try:
#         driver.find_element_by_xpath('//*[@id="narbar"]/ul/li[22]/div[2]/a').click()
#         driver.set_page_load_timeout(10)
#     except:
#         driver.execute_script("window.stop()")
#     driver.find_element_by_css_selector("#username").send_keys(username)
#     driver.find_element_by_css_selector("#password").send_keys(password)
#     driver.find_element_by_css_selector(".btn-submit").click()
#
# def approved(driver,orderid):
#     '''放行'''
#     driver.find_element_by_id("release").click()
#     driver.find_element_by_css_selector("[value='%s']" % orderid).click()
#     driver.find_element_by_xpath('//*[@id="content_release"]/form/div/div[2]/div/button').click()
#     sleep(1.5)
#     driver.find_element_by_class_name("confirm").click()
#     sleep(1)

def put_in_storage(driver,orderid):
    '''成品入库'''
    try:
        driver.find_element_by_id("productInStock").click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="produceId"]').send_keys(orderid)
        sleep(1)
        driver.find_element_by_id('inStockBtn').click()
        sleep(1.5)
        # driver.find_element_by_class_name("confirm").click()
        # sleep(1)
        print('成品入库成功')
    except Exception as e:
        print('入库异常：',e)

def outbound(driver,orderid):
    '''出库'''
    try:
        driver.find_element_by_id("productOutStock").click()
        driver.find_element_by_id("outProduceId").send_keys(orderid)
        driver.find_element_by_xpath('//*[@id="singleOutStock"]/form/div[10]/div/button').click()
        sleep(1.5)
        # driver.find_element_by_class_name("confirm").click()
        print('成品出库成功')
    except Exception as e:
        print('出库异常：',e)

if __name__ == '__main__':
    #print('c4'in find_msgType_database('C01001352551'))
    #print(find_msgType_database('C01001394063'))
    # database_manual_tooth_throwing('BC01000038449')
    # database_torque_compensation('C01001460326')
    # database_root_fusion_throwing('C01001460326')
    # #print(type(find_msgType_database('C01001352551')))
    # print(find_msgType_crmUserCode('D202009180002'))
    print(connect_to_the_database('M20210315000010'))