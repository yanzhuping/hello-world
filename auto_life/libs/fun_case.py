import libs.keywords_trans as key_trans
from time import sleep


# 登录crm或者cds
def logincrm_or_cds(driver, g_config, url_key):
    try:
        driver.set_page_load_timeout(5)
        driver.get(g_config.get(url_key))
    except:
        driver.execute_script("window.stop()")
    try:
        driver.find_element_by_css_selector("#username").send_keys(g_config.get("crm_username"))
        driver.find_element_by_css_selector("#password").send_keys(g_config.get("crm_password"))
        driver.find_element_by_css_selector(".btn-submit").click()
    except:
        pass


def login_iortho(driver, g_config):
    try:
        driver.get(g_config.get("iortho_url"))
        sleep(1)
        driver.maximize_window()
        driver.switch_to.frame("the-real-login-page")
        driver.find_element_by_id("_username").send_keys(g_config.get("iortho_username"))
        driver.find_element_by_id("_password").send_keys(g_config.get("iortho_password"))
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
