import libs.keywords_trans as key_trans
from time import sleep
import re
import os
import json
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 获取病例编号
def to_get_casecode(driver, iortho_url, from_state=None):
    if "patient/detail" not in driver.current_url:
        open_patient_detail(driver, iortho_url, from_state)
    casecode = get_casecode(driver)
    driver.close()
    key_trans.switch_to_cur_win(driver)
    return casecode


# 进去患者详情 from_state 从哪里搜索病例 1：星标 2：待处理 3：待提交 4：治疗中 5：已完成 6：已存档
def open_patient_detail(driver, iortho_url, from_state=None):
    if from_state is None:
        from_state = 4
    key_trans.switch_to_cur_win(driver, lambda: driver.execute_script("window.open('{}')".format(iortho_url)))
    sleep(2)
    key_trans.get_element(driver, "body > div.iortho-header > div > div > div> div> div>span[text]=病例").click()
    sleep(1)
    key_trans.get_element(driver, ".case-list-tab:nth-child(%d)" % from_state).click()
    key_trans.switch_to_cur_win(driver, lambda: key_trans.get_element(driver,".case-list-items case-list-item:nth-child(2)").click())


# 修改指定路径的文件名称，并将路径文件存储在列表中 目标文件夹；num是阶段
def rename_file(crm_casecode, dir=None):
    if dir is None:
        dir = "singleDDM"
    ods = []
    filepath_1 = os.path.join(key_trans.get_root_path(), "test_data", dir)
    filelist = os.listdir(filepath_1)
    pre_path = "{}_{}".format(crm_casecode, random.randint(1, 1000000))
    for filepath in filelist:
        olddir = os.path.join(filepath_1, filepath)
        filetype = os.path.splitext(filepath)[1]
        if "V6" in filepath:
            newdir = os.path.join(filepath_1, pre_path + "_V6" + filetype)
            os.rename(olddir, newdir)
        else:
            newdir = os.path.join(filepath_1, pre_path + filetype)
            os.rename(olddir, newdir)
        if filetype == ".json":
            get_new_json(newdir, crm_casecode)
        ods.append(newdir)
    return ods


# 修改json文件中的指定键对应的值
def get_new_json(filepath, crm_casecode, json_key=None):
    if json_key is None:
        json_key = "CaseInfo"
    key_ = json_key.split(".")
    key_length = len(key_)
    with open(filepath, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        i = 0
        a = json_data
        value = "{'CaseID': %s, 'Name': '目标位'}" % crm_casecode
        while i < key_length:
            if i + 1 == key_length:
                a[key_[i]] = value
                i = i + 1
            else:
                a = a[key_[i]]
                i = i + 1
        f.close()
        with open(filepath, 'w', encoding='utf-8') as f1:
            json.dump(json_data, f1, ensure_ascii=False)
        f1.close()


# 获取患者详情页的url，并提取病例序号，以备后用
def get_casecode(driver):
    strr = driver.current_url
    pat = re.compile(r"C(\d{11})")
    result = pat.search(strr).group()
    return result


# 搜索患者
def searchPatient(driver, crm_casecode):
    key_trans.wait_for_ele(driver, "#grouptab_0")
    key_trans.get_element(driver, "#grouptab_0").click()
    key_trans.get_element(driver, u"#moduleTab_0_病例").click()
    # 有“基本搜索”按钮的话点击
    key_trans.immediate_click(driver, "#basic_search_link")
    driver.find_element_by_xpath('//*[@id="ea_patients_ea_case_1_name_basic"]').clear()
    driver.find_element_by_css_selector("#accounts_ea_case_1_name_basic").clear()
    driver.find_element_by_css_selector("#contacts_ea_case_1_name_basic").clear()
    driver.find_element_by_css_selector("#name_basic").clear()
    driver.find_element_by_css_selector("#name_basic").send_keys(crm_casecode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[4]/b/a').click()


# 上传stl和ddm
def uploadStlAndDdm(driver, ods, phase=None):
    # 切换至iframe嵌套
    driver.refresh()
    sleep(2)
    driver.switch_to.frame("otherPage")
    if phase is None:
        phase_ele = driver.find_element_by_css_selector(".todo-tasklist-list:last-child")
    else:
        phase_ele = driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div' % phase)
    photo_list = key_trans.choice_file("photo")
    i = 0
    while i < 3:
        i = i+1
        # try:
        phase_ele.click()
        # 上传咬合stl
        driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
        driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
        sleep(1)
        driver.find_element_by_css_selector("#ddmType").send_keys(photo_list[0])
        driver.find_element_by_css_selector("#ddmType").send_keys(photo_list[1])
        driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
        sleep(2)

        # 上传DDM文件
        driver.find_element_by_css_selector(".i18n_historyshow_ddm").click()
        driver.find_element_by_xpath('//*[@id="collapse_3_4"]/div/a[1]').click()
        sleep(2)
        driver.find_element_by_css_selector("#ddmType").send_keys(ods[0])
        driver.find_element_by_xpath('//*[@id="fileupload"]/div[1]/div[1]/button[1]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="fileUploadModal"]/div[3]/button').click()
        sleep(2)
        break
        # except:
        #     print("文件上传失败，重新上传")
        #     driver.refresh()
        #     sleep(2)
        #     driver.switch_to.frame("otherPage")
        #     phase_ele.click()
        #     driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
        #     driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
        #     sleep(2)
        #     driver.find_element_by_xpath('//*[@id="STLdataID"]/tbody/tr[1]/td[4]/a[1]').click()
        #     driver.switch_to.alert.accept()
        #     driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
        #     driver.find_element_by_xpath('//*[@id="STLdataID"]/tbody/tr/td[4]/a[1]').click()
        #     driver.switch_to.alert.accept()


def dsignScheme(driver):
    # 切换到前一个窗口
    key_trans.switch_to_win(driver, -1)
    # 设计方案
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    sleep(1.5)
    driver.find_element_by_xpath('//*[@id="ea_stage_ea_design_1_创建_button"]').click()
    sleep(2)

    Select(driver.find_element_by_css_selector("#jaw_c")).select_by_value("3")

    Select(driver.find_element_by_css_selector("#case_design_type_c")).select_by_value("3")

    Select(driver.find_element_by_css_selector("#difficulty_c")).select_by_value("3")

    Select(driver.find_element_by_css_selector("#design_type_c")).select_by_value("1")

    driver.find_element_by_css_selector("#SAVE_HEADER").click()
    sleep(1)
    try:
        result = EC.alert_is_present()(driver)
        if result:
            result.accept()
            sleep(1)
            driver.find_element_by_css_selector("#SAVE_HEADER").click()
            result2 = EC.alert_is_present()(driver)
            if result2:
                result2.accept()
                sleep(1.5)
                driver.find_element_by_css_selector("#SAVE_HEADER").click()
    except:
        pass


def uploadOds(driver, ods, phase=None):
    key_trans.switch_to_win(driver, 1)
    driver.refresh()
    sleep(2)
    # 上传ods，即4个文件
    driver.switch_to.frame("otherPage")
    if phase is None:
        phase_ele = driver.find_element_by_css_selector(".todo-tasklist-list:last-child")
    else:
        phase_ele = driver.find_element_by_xpath('//*[@id="phase-%d"]/div[1]/div' % phase)
    phase_ele.click()
    driver.find_element_by_css_selector("#i18n_historyshow_3Ddesign").click()
    sleep(4)
    driver.find_element_by_css_selector("#ODSTitle>ul>li:last-child").click()
    driver.find_element_by_css_selector(".ODSSolutionBody>div:last-child .ODSSolutionBodyFoot button").click()
    sleep(2)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[1])
    sleep(0.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[2])
    sleep(0.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[3])
    sleep(0.5)
    driver.find_element_by_css_selector("#filesInput").send_keys(ods[4])
    sleep(0.5)
    driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button[1]').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="ODSUploadModal"]/div[3]/button').click()


def acceptAlert(driver):
    # 再次回到CRM
    key_trans.switch_to_win(driver, -1)
    # sleep(1)
    driver.find_element_by_css_selector("#operation").click()
    # 处理警告弹窗
    driver.switch_to.alert.accept()
    sleep(3)
    try:
        driver.switch_to.alert.accept()
        sleep(2)
    except:
        pass
    driver.find_element_by_css_selector("#do_submit").click()
    driver.switch_to.alert.accept()
    sleep(3)
    driver.switch_to.alert.accept()
    sleep(3)
    driver.find_element_by_css_selector("#send_design").click()
    driver.switch_to.alert.accept()
    sleep(3)
