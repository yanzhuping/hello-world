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
    try:
        driver.close()
        key_trans.switch_to_cur_win(driver)
    except Exception as e:
        print('异常状态：',e)
    return casecode

#获取病例姓名
def to_get_casename(driver, iortho_url, from_state=None):
    if "patient/detail" not in driver.current_url:
        open_patient_detail(driver, iortho_url, from_state)
    casename = driver.find_element_by_class_name("detail-info-data-name-30.ng-binding").text
    driver.close()
    key_trans.switch_to_cur_win(driver)
    return casename


# 进去患者详情 from_state 从哪里搜索病例 1：星标 2：待处理 3：待提交 4：治疗中 5：已完成 6：已存档
def open_patient_detail(driver, iortho_url, from_state=None):
    if from_state is None:
        from_state = 4
    key_trans.switch_to_cur_win(driver, lambda: driver.execute_script("window.open('{}')".format(iortho_url)))
    sleep(3)
    try:
        key_trans.get_element(driver, "body > div.iortho-header > div > div > div> div> div>span[text]=病例").click()
    except:
        pass
    sleep(1)
    key_trans.get_element(driver, ".case-list-tab:nth-child(%d)" % from_state).click()
    key_trans.switch_to_cur_win(driver, lambda: key_trans.get_element(driver,".case-list-items case-list-item:nth-child(2)").click())


# 修改指定路径的文件名称，并将路径文件存储在列表中 目标文件夹；num是阶段
def rename_file(crm_casecode, dir=None):
    if dir is None:
        dir = "singleDDM"
    doc_list = []
    doc_dict = {"ddm": "", "ods": "", "v6_ods": "", "json": "", "doc": ""}
    filepath_1 = os.path.join(key_trans.get_root_path(), "test_data", dir)
    filelist = os.listdir(filepath_1)
    pre_path = "{}_{}".format(crm_casecode, random.randint(1, 1000000))
    # pre_path=f'{crm_casecode}'
    for filepath in filelist:
        olddir = os.path.join(filepath_1, filepath)
        filetype = os.path.splitext(filepath)[1]
        if "V6" in filepath:
            newdir = os.path.join(filepath_1, pre_path + "_V6" + filetype)
            os.rename(olddir, newdir)
        if "ddm" in filepath:
            newdir = os.path.join(filepath_1, pre_path + filetype)
            os.rename(olddir, newdir)
        else:
            newdir = os.path.join(filepath_1, pre_path + filetype)
            os.rename(olddir, newdir)
        if filetype == ".json":
            get_new_json(newdir, crm_casecode)
        doc_list.append(newdir)

    for ods_1 in doc_list:
        ods_2 = ods_1.split('.')[1]
        if ods_2 == 'ddm':
            ddm = ods_1
            print(ods_1)
            doc_dict['ddm']=ddm
        elif ods_2 == 'ods':
            if ods_1.find('V6') > -1:
                v6 = ods_1
                doc_dict['v6_ods'] = v6
            else:
                ods = ods_1
                doc_dict['ods'] = ods
        elif ods_2 == 'json':
            json = ods_1
            doc_dict['json'] = json
        elif ods_2 == 'docx' or ods_2 == 'doc':
            doc=ods_1
            doc_dict['doc'] = doc
    return doc_dict

#修改制定路径stl文件名字
def rename_file_stl(crm_casecode):
    path=r"C:\\Users\\angelalign\\CDS\\"



# 修改json文件中的指定键对应的值
def get_new_json(filepath, crm_casecode, json_key=None):
    if json_key is None:
        json_key = "CaseInfo"
    key_ = json_key.split(".")
    key_length = len(key_)
    def _readFile(encoding):
        with open(filepath, 'r', encoding=encoding) as f:
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
            with open(filepath, 'w', encoding=encoding) as f1:
                json.dump(json_data, f1, ensure_ascii=False)
            f1.close()
    try:
        _readFile("utf-8")
    except:
        _readFile("gbk")



# 获取患者详情页的url，并提取病例序号，以备后用
def get_casecode(driver):
    strr = driver.current_url
    pat = re.compile(r"C(\d{11})")
    result = pat.search(strr).group()
    return result


# 搜索患者
def searchPatient(driver, crm_casecode):
    key_trans.wait_for_ele(driver, "#grouptab_0" ,True)
    key_trans.get_element(driver, "#grouptab_0").click()
    sleep(0.5)
    key_trans.get_element(driver, u"#moduleTab_0_病例").click()
    # 有“基本搜索”按钮的话点击
    key_trans.immediate_click(driver, "#basic_search_link")
    driver.find_element_by_xpath('//*[@id="ea_patients_ea_case_1_name_basic"]').clear()
    driver.find_element_by_css_selector("#accounts_ea_case_1_name_basic").clear()
    driver.find_element_by_css_selector("#contacts_ea_case_1_name_basic").clear()
    driver.find_element_by_css_selector("#name_basic").clear()
    driver.find_element_by_css_selector("#name_basic").send_keys(crm_casecode)
    driver.find_element_by_css_selector("#search_form_submit").click()
    casename=driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[7]/a').text
    sleep(2)
    driver.find_element_by_xpath('//*[@id="MassUpdate"]/table/tbody/tr[3]/td[4]/b/a').click()
    return casename

#搜索医生
def searchdoctor(driver, doctorname=None,doctorcode=None):
    key_trans.wait_for_ele(driver, "#grouptab_1" ,True)
    key_trans.get_element(driver, "#grouptab_1").click()
    sleep(0.5)
    key_trans.get_element(driver, u"#moduleTab_1_医生").click()
    # 有“基本搜索”按钮的话点击
    key_trans.immediate_click(driver, "#basic_search_link")
    driver.find_element_by_css_selector('#search_name_basic').clear()
    try:
        driver.find_element_by_css_selector('#search_name_basic').send_keys(doctorname)
    except:
        pass

    driver.find_element_by_css_selector("#phone_mobile_basic").clear()
    driver.find_element_by_css_selector("#email_basic").clear()
    driver.find_element_by_css_selector("#code_c_basic").clear()
    try:
        driver.find_element_by_css_selector("#code_c_basic").send_keys(doctorcode)
    except:
        pass
    driver.find_element_by_css_selector("#search_form_submit").click()
    sleep(2)


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

    # try:
    phase_ele.click()
    # 上传咬合stl
    driver.find_element_by_css_selector(".i18n_historyshow_occlusionstl").click()
    driver.find_element_by_xpath('//*[@id="collapse_3_3"]/div/a[1]').click()
    sleep(1)

    # sit环境
    driver.find_element_by_xpath('//span[@id="picker"]/div[2]/input').send_keys(photo_list[0])
    driver.find_element_by_xpath('//span[@id="picker"]/div[2]/input').send_keys(photo_list[1])
    sleep(3)
    driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[1]').click()
    driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[3]/button').click()
    print('stl上传成功')
    # 上传DDM文件
    driver.find_element_by_xpath('//*[@id="DDM"]/div[1]/h4/a/span[1]').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="collapse_3_4"]/div/a[1]').click()
    sleep(3)
    # sit
    driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[2]').click()
    sleep(1)
    driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['ddm'])
    sleep(2)
    driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[1]').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[3]/button').click()
    print('ddm上传成功')



def dsignScheme(driver):
    # 切换到前一个窗口
    key_trans.switch_to_win(driver, -1)
    # 设计方案
    driver.find_element_by_xpath(
        '//*[@id="list_subpanel_ea_case_ea_stage_1"]/table/tbody/tr[3]/td[1]/span/a').click()
    print("ooooo")
    sleep(1.5)
    js = "var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    print("11111")
    sleep(2)
    driver.find_element_by_id('ea_stage_ea_design_1_创建_button').click()
    print("22222")
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
    try:
        # driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['v6_ods'])
        sleep(0.5)
        driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['json'])
        sleep(0.5)
        driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['doc'])
        sleep(0.5)
        driver.find_element_by_xpath("//span[@id='picker']/div[2]/input").send_keys(ods['ods'])
        sleep(3)
        driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[2]/div/button[1]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="webuploadModal"]/div[3]/button').click()
        sleep(2)
    except:
        # driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['v6_ods'])
        sleep(0.5)
        driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['json'])
        sleep(0.5)
        driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['doc'])
        sleep(0.5)
        driver.find_element_by_xpath("//*[@id='filesInput']").send_keys(ods['ods'])
        sleep(3)
        driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button/span').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="odsupload"]/div[1]/div[1]/button/span').click()
        sleep(2)



def acceptAlert(driver):
    '''有时候有多个alert连续存在'''
    i=0
    while i<3:
        i=i+1
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            if alert:
                alert.accept()
        except:
            pass
        sleep(0.5)

def submit3d(driver):
    key_trans.switch_to_win(driver, -1)
    driver.find_element_by_css_selector("#operation").click()
    acceptAlert(driver)
    driver.find_element_by_css_selector("#do_submit").click()
    acceptAlert(driver)
    driver.find_element_by_css_selector("#send_design").click()
    acceptAlert(driver)
    sleep(3)

def getOdsFile(phase,type,update):
    typeList = ("A7","A8","IPR")
    phase_ = update and phase+"-update" or phase
    if phase is None and type is None:
        return "singleDDM"
    return "case_demo_3d\\"+typeList[int(type)-1]+"\\"+phase_


if __name__ == '__main__':
    print(rename_file("C01001404009", dir=None))
