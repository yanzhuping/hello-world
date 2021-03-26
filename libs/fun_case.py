import libs.keywords_trans as key_trans
from time import sleep
import re


# 登录crm或者cds
def logincrm_or_cds(driver, g_config, url_key):
    try:
        driver.set_page_load_timeout(30)
        driver.get(g_config.get(url_key))
    except:
        driver.execute_script("window.stop()")
        print("22")
    try:
        driver.find_element_by_css_selector("#username").send_keys(g_config.get("crm_username"))
        driver.find_element_by_css_selector("#password").send_keys(g_config.get("crm_password"))
        driver.find_element_by_css_selector(".btn-submit").click()
        sleep(5)
        driver.refresh()
        print("33")
    except:
        print("44")
        pass


def login_iortho(driver, g_config,case=None):
    username=""
    password=""
    val=''
    if case is not None:
        val=str(case.get("val"))
    if val!="":
        val=eval(val)
        username=val.get("username")
        password=val.get("password")
    try:
        driver.get(g_config.get("iortho_url"))
        sleep(1)
        driver.maximize_window()
        # driver.switch_to.frame("the-real-login-page")
        driver.find_element_by_id("_username").send_keys(username if username!="" else g_config.get("iortho_username"))
        driver.find_element_by_id("_password").send_keys(password if password!="" else g_config.get("iortho_password"))
        # driver.find_element_by_id("_btn_login").click()
        driver.find_element_by_id("_btn_login").click()
        sleep(3)
    except:
        pass


# cds搜索患者
def search_patient_in_cds(driver, g_config, crm_casecode):
    logincrm_or_cds(driver, g_config, "cds_url")
    driver.find_element_by_css_selector("#case_ID").send_keys(crm_casecode)
    driver.find_element_by_css_selector("#search").click()
    key_trans.wait_for_ele(driver, "#patient_list a")
    driver.find_element_by_css_selector("#patient_list a").click()
    driver.switch_to.frame("otherPage")
    driver.find_element_by_css_selector(".todo-tasklist-list:last-child").click()


# 查看病例下载照片
# def download_case_image(driver):
#     key_trans.get_element("body > div.iortho-header > div > div > div> div> div>span[text]=病例").click()
#     key_trans.get_element(driver, ".case-list-tab:nth-child(4)").click()

# 自动创建3D
def create_3d_auto(driver):
    ods=rename_file(self.caseid,get_dir())
    print(">>>开始登录crm，请耐心等候......" + "\n")
    logincrm_or_cds(driver.driver, driver.g_config, "crm_url");


# 校验crm收货记录
def check_crm_record(driver, expect_data):
    # 有可能需要点两下
    i = 0
    while i < 2:
        img_ele = key_trans.get_element(driver, "#list_subpanel_ea_case_ea_tasks_1 tbody tr:nth-child(2)>th:nth-child(5) img")
        if img_ele.get_attribute("src").find("arrow_down.gif") == -1:
            img_ele.click()
        else:
            break
    key_trans.get_element(driver, "#list_subpanel_ea_case_ea_tasks_1 tbody tr:nth-child(3)>td:nth-child(2) a").click()
    sleep(2)
    key_trans.get_element(driver, "#list_subpanel_ea_stage_ea_receipt_1 [name='listViewStartButton']").click()
    crm_record_text = ""
    while True:
        text_temp = driver.execute_script("return document.querySelector('#list_subpanel_ea_stage_ea_receipt_1').innerText")
        crm_record_text = crm_record_text + re.sub(r"\s", "", text_temp)
        next_ele = key_trans.get_element(driver, "#list_subpanel_ea_stage_ea_receipt_1 [name='listViewNextButton'] img")
        if next_ele.get_attribute("src").find("next_off") != -1:
            break
        next_ele.click()
        sleep(2)
    expect_data_dict = eval(expect_data)
    res_msg = ""
    for key in expect_data_dict:
        crm_r_len = len(re.compile(r'%s' % key).findall(crm_record_text))
        if crm_r_len != expect_data_dict.get(key):
            res_msg = f"{res_msg}crm'{key}'数量为{crm_r_len},excel期望值为{expect_data_dict.get(key)}不一致  "

    if res_msg != "":
        raise Exception(res_msg)
    else:
        print("crm收货记录校验成功")
