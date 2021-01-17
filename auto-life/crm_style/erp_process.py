#发货流程
import pymysql
from time import sleep
from time import strftime
from selenium.webdriver.common.keys import Keys


def process_orders(driver):
    '''3D全设计确认后，将订单变成执行中，并复制订单号'''
    nowdate=strftime('%Y-%m-%d')
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    driver.find_element_by_xpath('//*[@id="list_subpanel_ea_stage_ea_production_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    orderid=driver.find_element_by_id("name").text
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
        driver.find_element_by_id('send_production').click()
        driver.switch_to.alert.accept()
        sleep(1.5)
        driver.switch_to.alert.accept()
    except:
        js='window.open("http://crm-web.sh-sit.eainc.com/crm/auto_erp.php")'
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
    '''连接数据库'''
    db = pymysql.Connect(host="192.168.37.108", port=3306, user="erpdb_sh_sit",passwd="erpdb_sh_sit", db="erpdb_sh_sit", charset='utf8')
    cursor = db.cursor()
    # sql = "update erp_order set is_sent_to_mes='0',flow_way='CASE' where produce_Id= '%s'"%(orderid)
    sql_1 = "update erp_order set is_sent_to_mes='1' where produce_Id= '%s'"%(orderid)
    cursor.execute(sql_1)
    sql_2 = "update erp_order set produce_state='04' where produce_Id= '%s'" % (orderid)
    cursor.execute(sql_2)
    db.commit()
    db.close()

def login_erp(driver):
    '''登录erp系统'''
    try:
        driver.set_page_load_timeout(10)
        driver.get("http://erp-web.sh-sit.eainc.com:8080/erp/erpweb/HTML/index.html")
    except:
        driver.execute_script("window.stop()")
    driver.find_element_by_css_selector("#username").send_keys("zhengyan")
    driver.find_element_by_css_selector("#password").send_keys("123456")
    driver.find_element_by_css_selector(".btn-submit").click()
    sleep(3)
    driver.refresh()

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

    driver.find_element_by_id("productInStock").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="produceId"]').send_keys(orderid)
    sleep(1)
    driver.find_element_by_id('inStockBtn').click()
    sleep(1.5)
    # driver.find_element_by_class_name("confirm").click()
    # sleep(1)

def outbound(driver,orderid):
    '''出库'''
    driver.find_element_by_id("productOutStock").click()
    driver.find_element_by_id("outProduceId").send_keys(orderid)
    driver.find_element_by_xpath('//*[@id="singleOutStock"]/form/div[10]/div/button').click()
    sleep(1.5)
    # driver.find_element_by_class_name("confirm").click()

if __name__ == '__main__':
    connect_to_the_database('M20200805000024')