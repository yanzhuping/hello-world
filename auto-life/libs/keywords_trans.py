from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from libs.fun_case import logincrm_or_cds
from libs.fun_case import login_iortho
from libs.fun_case import check_crm_record
from libs.test_utils import *
from libs.create_3d import *
from libs.process_3d import Process3D
import filecmp
import base64
from libs.global_vars import *
from xpinyin import Pinyin
from selenium.common.exceptions import TimeoutException
from libs.functionality_set import *
import math
from libs.simple_case import *


# 处理关键字input
def input_handler(mainhandler, case=None):
    g_config = mainhandler.g_config
    val = str(case.get("val"))
    id = case.get("id")
    driver = mainhandler.driver
    input_val = format_digit_str(val)
    selector = case.get("selector")
    if case.get("selector") == '[ng-model="$ctrl.case_base.patientName"]' and val == "":
        input_val = readDataFromMySQL(g_config)
        mainhandler.patient_name = input_val
        deleteDataFromMySQL(g_config)
    if val.find("random") != -1:
        input_val = random.choice(choice_file(val.split("_")[0]))
    get_element(driver, selector).send_keys(input_val)
    check_loading_is_hide(driver)
    # 图片文件上传之后保存到本地 后面校验对比用
    if val.find("photo_random") != -1 and val != "photo_random:0":
        selector = selector.replace("#", ".")
        selector = selector.replace("others", "other")
        img_selector = "{} angel-image img".format(selector)
        photo_type_name = get_photo_type_name(driver, selector)
        save_photo_to_local(driver, img_selector, "{}-{}.png".format(id, photo_type_name))
    if val.find("stl_random") != -1 and val != "stl_random:0":
        save_stl_data(mainhandler, selector, id)


# 处理关键字clear
def clear_handler(mainhandler, case=None):
    get_element(mainhandler.driver, case.get("selector")).clear()


# 处理关键字click
def click_handler(mainhandler, case=None):
    driver = mainhandler.driver
    switch_to_cur_win_ifchange(driver, lambda: get_element(mainhandler.driver, case.get("selector")).click())
    check_loading_is_hide(driver)


# 处理关键字immediate_click 立刻点击(不会等待元素出现，有就点击，没有就不点击)
def immediate_click_handler(mainhandler, case=None):
    immediate_click(mainhandler.driver, case.get("selector"))


# 登录crm
def logincrm_handler(mainhandler, case=None):
    logincrm_or_cds(mainhandler.driver, mainhandler.g_config, "crm_url")


# 登录iOrtho
def login_iortho_handler(mainhandler, case=None):
    login_iortho(mainhandler.driver, mainhandler.g_config, case)


# 处理sleep关键字
def sleep_handler(mainhandler, case=None):
    val = case.get("val")
    num = val if val is not None and val != "" else 1
    sleep(num)


# 处理url关键字
def url_handler(mainhandler, case=None):
    open_url(mainhandler.driver, case.get("val"), mainhandler.g_config)


# 新病例暂存校验
def save_check_handler(mainhandler, case):
    sleep(1)
    driver = mainhandler.driver
    failed_count = 0
    error_msg = ""
    for store_case in mainhandler.case_store.get(case.get("id")):
        store_case_val = store_case.get("val")
        store_case_keywords = store_case.get("keywords")
        store_case_selector = store_case.get("selector")
        store_case_id = store_case.get("id")
        if store_case_selector == "" or store_case_val == "" or store_case_keywords in NOT_CHECK_KEYLIST or store_case_val=='iframe':
            continue
        if store_case_val == "next_page" or store_case_val == "after_click":
            get_element(driver, store_case_selector).click()
            continue
        if store_case_val == "pre_click":
            get_element(driver, store_case_selector).click()
        if isinstance(store_case_val, str) and (store_case_val == "photo_random" or store_case_val.find("photo_random:1") != -1):
            selector_temp = store_case_selector.replace("#", ".")
            selector_temp = selector_temp.replace("others", "other")
            photo_type_name = get_photo_type_name(driver, selector_temp)
            # 新建时保存的照片名
            pre_filename = "{}-{}.png".format(store_case_id, photo_type_name)
            # check时保存的照片名
            check_filename = "{}-{}_check.png".format(store_case_id, photo_type_name)
            # img的选择器
            img_selector = "{} angel-image img".format(selector_temp)
            # 将照片保存到本地
            save_photo_to_local(driver, img_selector, check_filename)
            check_result = img_hash_compare(os.path.join(SAVE_CHECK_PATH, pre_filename), os.path.join(SAVE_CHECK_PATH, check_filename))
        elif isinstance(store_case_val, str) and (store_case_val == "stl_random" or store_case_val.find("stl_random:1") != -1):
            value, index = get_stl_val(driver, store_case_selector)
            check_result = mainhandler.case_variable[store_case_id].get("stl"+index) == value
        else:
            check_result = check_case(mainhandler.driver, store_case)
        if not check_result:
            e_msg = f'{store_case.get("id")} {store_case.get("desc")}: 校验失败\n'
            print(e_msg)
            failed_count = failed_count+1
            error_msg = error_msg+e_msg
    if failed_count != 0:
        raise Exception(error_msg)
    else:
        print("-------暂存全部校验成功------")


# 处理include关键字 导入其他用例
def include_handler(mainhandler, case):
    val = case.get("val")
    case_list = mainhandler.case_store.get(val)
    opt_level = int(mainhandler.t_opt.get("level", -1))
    for include_case in case_list:
        case_level = include_case.get("level")
        if opt_level == -1 or opt_level == case_level:
            # 根据keywords触发相应的函数
            globals().get(include_case.get("keywords") + "_handler")(mainhandler, include_case)
            # 检查有没有loading层覆盖 有的话等待loading消失
            check_loading_is_hide(mainhandler.driver)


# 处理create3d关键字 为病例创建3D方案
def create3d_handler(mainhandler, case):
    driver = mainhandler.driver
    dir_name = None
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        dir_name = val.get("dir_name")
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(mainhandler.driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    ods = rename_file(casecode, dir_name)
    searchPatient(driver, casecode)
    key_trans.switch_to_cur_win(driver, lambda: driver.find_element_by_css_selector("#pause_tasks_open").click())
    uploadStlAndDdm(driver, ods)
    dsignScheme(driver)
    uploadOds(driver, ods)
    acceptAlert(driver)
    close_tab(driver, 2)
    # goto_case_detail(driver, mainhandler.g_config.get("iortho_url"), casecode)
    # wait_for_3d_ele(driver)
    # close_tab(driver)

# 处理process3d关键字
def process3d_handler(mainhandler, case):
    switch_to_cur_win(mainhandler.driver)
    casecode = to_get_casecode(mainhandler.driver, mainhandler.g_config.get("iortho_url"), 2)
    process3d = Process3D(mainhandler, casecode, case.get("id"))
    # 下面是3d的一整套流程 后面再整理
    process3d.test_f()
    process3d.test_g()
    process3d.test_h()
    process3d.test_i()
    process3d.test_j()
    process3d.test_k()
    process3d.test_l()
    process3d.test_m()
    process3d.test_n()
    process3d.test_o()
    process3d.test_p()
    process3d.test_q()
    process3d.test_r()


# 处理wait_for关键字 等待某个元素出现
def wait_for_handler(mainhandler, case):
    selector = case.get("selector")
    val = str(case.get("val"))
    is_hidden = None
    is_need_refresh = None
    if val != "":
        val = eval(val)
        is_hidden = val.get("hidden")
        is_need_refresh = val.get("refresh")
    driver = mainhandler.driver
    wait_for_ele(driver, selector, is_need_refresh, is_hidden)


# 屏幕截图
def screenshot_handler(mainhandler, case):
    selector = case.get("selector")
    case_id = case.get("id")
    val = case.get("val")

    if val and val != 1:
        full_page_screenshot(mainhandler.driver, os.path.join(get_root_path(), "test_report", "screenshot", case_id, "{}.png".format(val)), selector)
    else:
        full_page_screenshot(mainhandler.driver, os.path.join(get_root_path(), "test_report", "screenshot", "save_check", case_id + ".png"), selector)


def check_cds_image_handler(mainhandler, case):
    driver = mainhandler.driver
    case_id = case.get("id")
    val = case.get("val")
    crm_casecode = ""
    if val != "":
        val_dict = eval(val)
        crm_casecode = val_dict.get("crm_casecode")
    if crm_casecode == "":
        crm_casecode = to_get_casecode(mainhandler.driver, mainhandler.g_config.get("iortho_url"))
    link_to_cds(driver, mainhandler.g_config, crm_casecode)
    driver.find_element_by_css_selector("#PHOTO a").click()
    driver.find_element_by_css_selector("#photo-0").click()
    sleep(.5)
    cds_photo_dict = get_cds_image(driver, "#viewPhotoThumbnail .col-xs-4")
    driver.find_element_by_css_selector("#myModalPhoto > div.modal-footer > button.btn.btn-default."
                                        "closePhotoModel.i18n_historyshow_close").click()
    sleep(.5)
    driver.find_element_by_css_selector("#XRAY a").click()
    sleep(.5)
    xray_ele = driver.find_element_by_css_selector("#photo-1")
    cds_image_all=cds_photo_dict
    if xray_ele.is_displayed():
        xray_ele.click()
        sleep(.5)
        cds_xray_dict = get_cds_image(driver, "#viewXRayThumbnail .col-xs-4")
        cds_image_all={**cds_photo_dict, **cds_xray_dict}
        driver.find_element_by_css_selector("#myModalXRay .i18n_historyshow_close").click()
        sleep(.5)
    # 比较文件差异
    compare_save_check_file(driver, cds_image_all, case_id)


# 校验cds加工单
def check_cds_prescription_handler(mainhandler, case):
    driver = mainhandler.driver
    driver.find_element_by_css_selector("#CASEDATA .i18n_historyshow_order").click()
    sleep(.5)
    driver.find_element_by_css_selector("#photo-7 .i18n_historyshow_browse").click()
    sleep(1)
    driver.find_element_by_css_selector("#casedataID .iframe_outer a").click()
    switch_to_cur_win(driver)
    driver.execute_script('document.querySelector(".check-success .product-info").remove()')
    cds_text = driver.find_element_by_css_selector(".check-success").text
    cds_text = cds_text.replace("(如选择无法确定复诊周期，则所有临床操作将设计在第1步)", "").replace("20. 特殊说明:","")
    cds_text = re.sub(r"[\s\n:：，, 、-]", "", cds_text)
    open_patient_detail(driver, mainhandler.g_config.get("iortho_url"))

    # sleep(120)  # 测试cds校验是否准确，需要改变iortho查看

    check_case_selector = u"timezone-input>div[button-content='查看病例']:not(.ng-hide)"
    wait_for_ele(driver, check_case_selector)
    driver.find_element_by_css_selector(check_case_selector).click()
    switch_to_cur_win(driver)
    sleep(2)
    # 去除iortho和cds的差异
    driver.execute_script('document.querySelector(".check-success>.title").remove();'
                          'document.querySelector(".check-success>.photos>.section-title").remove();'
                          'document.querySelector(".check-success>.photos>.section-body").innerHTML=document.querySelector(".check-success>.photos>.section-body>.key-value-box:last-child").innerHTML;'
                          'var extends_ele=document.querySelector(".photos .section-body .extends");'
                          'if(extends_ele)extends_ele.remove();'
                          )
    iortho_text = driver.find_element_by_css_selector(".check-success").text
    iortho_text = re.sub(r"[\s\n:：，, 、-]", "", iortho_text)
    iortho_text = iortho_text.replace("20. 特殊说明: ","")
    cds_text_len = len(cds_text)
    iortho_text_len = len(iortho_text)
    compile_len = 20
    num = math.ceil(iortho_text_len/compile_len)
    error_msg = ""

    for i in range(num):
        len_temp = compile_len*(i+2)
        end_len = iortho_text_len if len_temp > iortho_text_len else len_temp
        iortho_text_temp = iortho_text[compile_len*(i+1):end_len]
        end_len = cds_text_len if len_temp > cds_text_len else len_temp
        cds_text_temp = cds_text[compile_len*(i+1):end_len]
        if iortho_text_temp != cds_text_temp:
            error_msg = f"{error_msg} 差异：cds（{cds_text_temp}）,iortho（{iortho_text_temp}）\n"
            break
            # cds_text = cds_text.replace(cds_text_temp,iortho_text_temp)
            # cds_text_len = len(cds_text)
    close_tab(driver, 4)
    if error_msg != "":
        raise Exception(error_msg)
    else:
        print("cds加工单校验成功")

# 关闭浏览器标签页关键字
def close_tab_handler(mainhandler, case):
    val = case.get("val")
    num = 1
    if val != '' and (isinstance(val, float) or isinstance(val, str)):
        num = int(val)
    close_tab(mainhandler.driver, num)


# 打开进入患者详情页
def goto_case_detail_handler(mainhandler, case):
    goto_case_detail(mainhandler.driver, mainhandler.g_config.get("iortho_url"), format_digit_str(case.get("val")))

#通过病例列表进入患者详情页
def click_into_detail_handler(mainhandler,case):
    open_patient_detail(mainhandler.driver, mainhandler.g_config.get("iortho_url"), case.get("val"))
    check_loading_is_hide(mainhandler.driver)


# 切换到iframe\alert\窗口
def switch_to_handler(mainhandler, case):
    driver = mainhandler.driver
    val = case.get("val")
    if val == "iframe":
        driver.switch_to.frame(get_element(driver, case.get("selector")))
    if val == "alert":
        wait = WebDriverWait(driver, 10)
        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()
    if val == "win":
        change_num = val.split(":")[1]
        val = -1 if change_num is None or change_num == "" else int(change_num)
        switch_to_win(mainhandler.driver, val)


def switch_to_mainframe_handler(mainhandler, case):
    mainhandler.driver.switch_to.default_content()


def check_crm_record_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    if "crm/index.php" not in driver.current_url:
        logincrm_or_cds(mainhandler.driver, mainhandler.g_config, "crm_url")
    searchPatient(driver, casecode)
    check_crm_record(driver, case.get("val"))
    close_tab(driver, 1)


def check_detail_img_handler(mainhandler, case):
    pass


def link_to_cds_handler(mainhandler, case):
    driver = mainhandler.driver
    val = case.get("val")
    casecode=""
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None and casecode!="":
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    link_to_cds(driver, mainhandler.g_config, casecode)

def link_to_record_handler(mainhandler, case):
    driver=mainhandler.driver
    casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    if "crm/index.php" not in driver.current_url:
        logincrm_or_cds(mainhandler.driver, mainhandler.g_config, "crm_url")
    searchPatient(driver, casecode)
    i = 0
    while i < 2:
        img_ele = key_trans.get_element(driver,
                                        "#list_subpanel_ea_case_ea_tasks_1 tbody tr:nth-child(2)>th:nth-child(5) img")
        if img_ele.get_attribute("src").find("arrow_down.gif") == -1:
            img_ele.click()
        else:
            break
    key_trans.get_element(driver, "#list_subpanel_ea_case_ea_tasks_1 tbody tr:nth-child(3)>td:nth-child(2) a").click()
    sleep(2)
    # 有可能需要点两下
    i = 0
    while i < 2:
        img_ele = key_trans.get_element(driver,
                                        "#list_subpanel_ea_stage_ea_receipt_1 tbody tr:nth-child(2)>th:nth-child(6) img")
        if img_ele.get_attribute("src").find("arrow_down.gif") == -1:
            img_ele.click()
        else:
            break
    link_ele=driver.execute_script('var list=document.querySelectorAll("#list_subpanel_ea_stage_ea_receipt_1>table>tbody tr:nth-child(2)~tr");'
                                    'var link_ele;'
                                    'list.forEach(function(v){'
                                        'var first_td=v.firstElementChild;'
                                        'if(first_td.nextElementSibling.firstElementChild.innerText=="口内照"){'
                                        '    link_ele=first_td.firstElementChild.firstElementChild;'
                                        '}'
                                    '});'
                                   'return link_ele;'
                                   )
    link_ele.click()
    sleep(5)
# #######----crm相关的功能集合---###############################################################################


# 处理质检不合格关键字
def unqualified_quality_inspection_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    unqualified_quality_inspection(driver)


#处理质检合格关键字
def quality_inspection_qualified_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    quality_inspection_qualified(driver)

#处理不收治关键字
def not_treated_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    create_No_Treatment(driver)

#处理文字方案关键字
def text_plan_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    create_Word_scheme(driver)

#结束当前阶段关键字
def finish_phase_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    finish_phase(driver)

#线下病例选择硅胶关键字
def offline_new_guijiao_handler(mainhandler, case):
    driver = mainhandler.driver
    patientname=None
    val = case.get("val")
    if val != "":
        val = eval(val)
        patientname = val.get("patientname")
    if patientname is None:
        patientname ="线下"+ str(random.randint(11111,99999))
    logincrm_handler(mainhandler, case)
    offline_new_guijiao(driver,patientname,mainhandler.g_config.get("institutions"),mainhandler.g_config.get("doctorname"))

#线下病例新建选择口内照关键字
def offline_new_photo_handler(mainhandler, case):
    driver = mainhandler.driver
    patientname=None
    val = case.get("val")
    if val != "":
        val = eval(val)
        patientname = val.get("patientname")
    if patientname is None:
        patientname ="线下"+ str(random.randint(11111,99999))
    logincrm_handler(mainhandler, case)
    offline_new_photo(driver,patientname,mainhandler.g_config.get("institutions"),mainhandler.g_config.get("doctorname"))

#线下病例中期选择硅胶关键字
def offline_middle_guijiao_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    finish_phase(driver)
    offline_middle_guijiao(driver, casecode)

#线下病例中期选择口内照关键字
def offline_middle_photo_handler(mainhandler, case):
    driver = mainhandler.driver
    casecode = None
    val = case.get("val")
    if val != "":
        val = eval(val)
        casecode = val.get("crm_casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler, case)
    searchPatient(driver, casecode)
    finish_phase(driver)
    offline_middle_photo(driver, casecode)


#--------simple case-------------------------------------------------------------------
#简单的冠军版A6
def create_newcase_champion_a6_1_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    champion_A6_1(driver, g_config)

#冠军版A6后续使用A6
def create_newcase_champion_a6_2_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    champion_A6_2(driver, g_config)

#冠军版非A6
def create_newcase_champion_a6_3_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    champion_A6_3(driver, g_config)

#标准版
def create_newcase_stand_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    stand(driver, g_config)

#儿童版
def create_newcase_child_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    child(driver, g_config)

#儿童版A6
def create_newcase_child_a6_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    child_A6(driver, g_config)

#儿童版+冠军版
def create_newcase_childAndchampion_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    child_champion(driver, g_config)

#儿童版+冠军版A6
def create_newcase_childAndchampion_a6_handler(mainhandler,case):
    driver=mainhandler.driver
    g_config=mainhandler.g_config
    child_champion_A6(driver, g_config)

#---------------------------------------------------------------------------------------


# ----assert_handler--------------------------------------------------------------------
def assert_is_checked_handler(driver, selector, assert_val, desc):
    if get_element(driver, selector).is_selected() != assert_val:
        raise Exception(f"{desc} {selector} 校验失败")
    else:
        print(f"{desc} {selector} 校验成功")

# 处理assert  text关键字 断言元素的文本
def assert_text_handler(driver, selector, assert_val, desc):
    if get_element(driver, selector).text != assert_val:
        raise Exception(f"{desc} {selector} 校验失败")
    else:
        print(f"{desc} {selector} 校验成功")


# 处理assert ele_count关键字 断言元素的个数
def assert_ele_count_handler(driver, selector, assert_val, desc):
    if len(driver.find_element_by_css_selector(selector)) != str(assert_val):
        raise Exception(f"{desc} {selector} 校验失败")
    else:
        print(f"{desc} {selector} 校验成功")

# 处理assert ele_exist关键字 断言元素是否存在
def assert_ele_exist_handler(driver, selector, assert_val, desc):
    try:
        ele = get_element(driver, selector)
        if ele and ele.is_displayed() != False and assert_val == False:
            raise Exception(f"{desc} {selector} 校验失败")
        else:
            print(f"{desc} {selector} 校验成功")
    except TimeoutException:
        # 获取元素超时
        if assert_val == True:
            raise Exception(f"{desc} {selector} 校验失败")
        else:
            print(f"{desc} {selector} 校验成功")


#  处理assert关键字
def assert_handler(mainhandler, case):
    val = case.get("val")
    selector = case.get("selector")
    desc = case.get("desc")
    assert_key, assert_val = val.split(":")
    if assert_val in ['True','False']:
        assert_val=True if assert_val=='True' else False
    globals().get(f"assert_{assert_key}_handler")(mainhandler.driver, selector, assert_val, desc)

#############################################################################################


# 关闭tab页并且切换到前一个tab num:需要关闭的窗口数量
def close_tab(driver, num=0):
    check_loading_is_hide(driver)
    for i in range(num):
        driver.close()
        switch_to_cur_win(driver)


# 上传照片时取当前选择器下方的文字作为照片名 如正面像、侧面像等
def get_photo_type_name(driver, selector):
    selector_temp = selector+"+span"
    p = Pinyin()
    if "other" in selector:
        return f"{p.get_pinyin(u'其他','')}_{selector.split('-')[1]}"
    else:
        span_text = driver.find_element_by_css_selector(selector_temp).text
        return p.get_pinyin(span_text.replace("*", ""), '')


# 校验save_check目录下的文件iortho和cds的对比
def compare_save_check_file(driver, img_url_dict, case_id):
    filelist = list_dir(SAVE_CHECK_PATH)
    failed_count = 0
    error_msg = ""
    for filepath in filelist:
        filename = os.path.split(filepath)[1]
        if case_id in filename and re.search(r"_check|_cds|_detail", filename) is None:
            short_name = filename.split(".")[0]
            photo_type_name = short_name.split("-")[1]
            img_url = img_url_dict.get(photo_type_name)
            cds_img_filepath = os.path.join(SAVE_CHECK_PATH, short_name + "_cds.png")
            save_file(driver, cds_img_filepath, img_url)
            result = img_hash_compare(filepath, cds_img_filepath, 8)
            if result is False:
                print("{} 校验失败".format(photo_type_name))
                failed_count = failed_count + 1
                error_msg = f"{error_msg}{photo_type_name} 校验失败\n"

    if failed_count != 0:
        raise Exception(error_msg)
    else:
        print("-----cds_image全部校验成功-----")


# 获取cds照片对应的元素选择器 key是照片类型的文字（正面像、。。。）
def get_cds_image(driver, selector):
    ele_list = driver.find_elements_by_css_selector(selector)
    img_url_list = {}
    # 记录“其他”照片的index
    other_num = 0
    p = Pinyin()
    for index, element in enumerate(ele_list):
        # 照片属于哪个类型 正面像、侧面像还是。。。
        ele_name = driver.execute_script("return arguments[0].querySelector('.caption>h5:nth-child(3)')",element)
        photo_type_name = ele_name.text.split("类型：")[1]
        if photo_type_name.find("下颌前伸位口内") > -1:
            photo_type_name=photo_type_name.replace("面像", "位像")

        photo_type_name = p.get_pinyin(photo_type_name, '')
        if 'qita' in photo_type_name:
            photo_type_name = f"{photo_type_name}_{other_num}"
            other_num = other_num + 1
        sleep(.5)
        img_url_list[photo_type_name] = driver.execute_script("arguments[0].scrollIntoView();return arguments[0].querySelector('.main_img img').getAttribute('src')", element)

    return img_url_list


def open_url(driver, url, g_config=None):
    if url is not None:
        if url in ("iortho_url", "crm_url", "cds_url"):
            url = g_config.get(url)
        switch_to_cur_win(driver, lambda: driver.execute_script("window.open('{}')".format(url)))


# 均值哈希算法得到图片hash值然后做比较 # 容错值默认暂定为5
def img_hash_compare(filename1, filename2, e_value=5):
    num = cmpHash(aHash(cv2.imread(filename1)), aHash(cv2.imread(filename2)))
    return num <= e_value


def save_stl_data(mainhandler, selector, id):
    driver = mainhandler.driver
    value, index = get_stl_val(driver, selector)
    if mainhandler.case_variable.get(id) is None:
        mainhandler.case_variable[id] = {}
    if value != "" and value is not None:
        mainhandler.case_variable[id]["stl"+index] = value


# 获取stl input框显示的值
def get_stl_val(driver, selector):
    value=""
    index = selector.split("stl_")[1]
    try:
        ele = driver.execute_script(f"return document.querySelector('{selector}').parentNode.previousElementSibling;")
        wait_for_value(ele)
        value = driver.execute_script("arguments[0].scrollIntoView();return arguments[0].value", ele)
    except:
        pass
    print(value)
    return value, index


# 保存照片到本地，用于后续校验
def save_photo_to_local(driver, selector, filename):
    src = get_ele_src(driver, selector)
    filepath = os.path.join(SAVE_CHECK_PATH, filename)
    save_file(driver, filepath, src)


# 获取元素的src
def get_ele_src(driver, selector):
    wait_for_ele(driver, selector)
    sleep(1.5)
    ele = "document.querySelector('{}')".format(selector)
    driver.execute_script(f"{ele}.scrollIntoView();")
    return driver.execute_script(f"return {ele}.getAttribute('src')")


# 读取JS代码
def get_script(path):
    with open(path, 'r', encoding='utf-8') as f:
        js_script = f.read()
        return js_script


def save_file(driver, filename, image_url):
    driver.execute_script(get_script(os.path.join(get_root_path(), "libs", "downloadUtils.js")))
    result = driver.execute_async_script(get_script(os.path.join(get_root_path(), "libs", "downloadUtils.js"))
                                         + ";getFile('{}')".format(image_url))
    with open(filename, 'wb') as f:
        f.write(base64.b64decode(result.split(",")[1]))
    # cds的照片等比例缩放到高度153 和iortho一致
    if "_cds" in filename:
        resize_img(ori_img=filename, dst_img=filename, dst_h=153)


# 比较文件差异
def cmp_file(filepath1, filepath2):
    return filecmp.cmp(filepath1, filepath2)


def wait_for_3d_ele(driver):
    wait_for_ele(driver, ".web-design-list-item .web-design-list-item-tag[text]=待确认", True)


def immediate_click(driver, selector):
    driver.implicitly_wait(0)
    try:
        get_element(driver, selector, True).click()
        driver.implicitly_wait(10)
    except:
        driver.implicitly_wait(10)


# 通过病例编号进入到病例详情页
def goto_case_detail(driver, iortho_url, casecode):
    driver.get("{0}/#/patient/detail/null/{1}/content/null/{1}".format(
        iortho_url, casecode))


# 等待元素出现或者消失  val="hidden"时是等待元素消失
def wait_for_ele(driver, selector, is_need_refresh=None, is_hidden=None):
    # print("等待 {} 元素{}".format(selector, "消失" if is_hidden else "出现"))
    wait = WebDriverWait(driver, 120, 3)
    if is_hidden:
        wait.until(EC.invisibility_of_element(get_element(driver, selector, True)))
    else:
        global wait_to_get_selector_opt
        wait_to_get_selector_opt["is_need_refresh"] = is_need_refresh
        wait_to_get_selector_opt["selector"] = selector
        wait.until(do_get_ele)


# 等待某个元素有值
def wait_for_value(element, timeout=60):
    start = 0
    while start <= timeout:
        text = element.get_attribute("value")
        if text != "" and text is not None:
            break
        sleep(1)


# 刷新并且获取元素
def do_get_ele(driver):
    driver.implicitly_wait(0)
    if wait_to_get_selector_opt.get("is_need_refresh"):
        driver.refresh()
        sleep(2)
    ele = get_element(driver, wait_to_get_selector_opt.get("selector"), True)
    if ele:
        driver.implicitly_wait(10)
    return ele


# 校验用例执行后的结果，如果是input就对比操作值，如果是click就比较页面元素是否被选中
def check_case(driver, case):
    keywords = case.get("keywords")
    val = case.get("val")
    selector = case.get("selector")
    # 有些选择器是label 要定位到它for的那个input元素才能知道是不是selected
    re_obj = re.compile(r'for=\"(.+)\"').search(selector)
    if re_obj is not None:
        selector = f"#{re_obj.group(1)}"
    # 某些click关键却要校验input的值 需要在excel中的操作值中写上val:期望值 比如：val:2000-01-01
    is_s_val = isinstance(val, str) and val.startswith("val")
    val = format_digit_str(val)

    if keywords == 'input' or is_s_val:
        if is_s_val:
            val = val.split("val:")[1]
        return val == get_element(driver, selector).get_attribute('value')
    elif keywords == 'click':
        is_selected = get_element(driver, selector).is_selected()
        return (val != "0" and is_selected) or (val == "0" and not is_selected)


# 切换到当前窗口
def switch_to_cur_win(driver, exec_fun=None):
    if exec_fun is not None:
        exec_fun()
    all_win = driver.window_handles
    all_win_num = len(all_win)
    driver.switch_to.window(all_win[all_win_num-1])


# 切换到当前窗口
def switch_to_cur_win_ifchange(driver, exec_fun=None):
    pre_win_num = len(driver.window_handles)
    if exec_fun is not None:
        exec_fun()
    all_win = driver.window_handles
    cur_win_num = len(all_win)
    if cur_win_num != pre_win_num:
        driver.switch_to.window(all_win[cur_win_num - 1])


# 切换到指定窗口 change_num 负数表示前第几个窗口，正数表示后第几个窗口
def switch_to_win(driver, change_num):
    all_win = driver.window_handles
    cur_win = driver.current_window_handle
    index = all_win.index(cur_win)
    driver.switch_to.window(all_win[index+change_num])


# 获取测试数据中的照片
def choice_file(dir):
    photolist = []
    filepath_1 = os.path.join(get_root_path(), 'test_data', dir)
    filelist=os.listdir(filepath_1)
    for file in filelist:
        fullname = os.path.join(filepath_1, file)
        photolist.append(fullname)
    return photolist


# 获取页面元素
def get_element(driver, selector, is_immedite=None):
    check_loading_is_hide(driver)
    wait = WebDriverWait(driver, 4, 0.5)
    text = None
    # 支持选择器中带文本 比如：div>span[text]=病例 正常选择器中是没有这种写法的
    if selector.find("[text]=") > -1:
        selector, text = selector.split("[text]=")
    if selector.startswith("/"):
        if is_immedite:
            elements = driver.find_elements_by_xpath(selector)
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, selector)))
    else:
        if is_immedite:
            elements = driver.find_elements_by_css_selector(selector)
        else:
            elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
    if len(elements) > 0 and text is not None:
        for ele in elements:
            if ele.text == text:
                return ele
        return None
    return elements[0] if elements is not None and len(elements) > 0 else None


# 检查有没有loading层覆盖 有的话等待loading消失
def check_loading_is_hide(driver):
    sleep(.5)
    try:
        wait = WebDriverWait(driver, 40, 0.5)
        loading_ele = driver.execute_script("return document.querySelector('.iortho-global-loading')")
        percent_ele = driver.execute_script("return document.querySelector('#fileupload_loadingImg')")
        popover = driver.execute_script("return document.querySelector(\"[ng-show=\'$ctrl.popoverShow\']\")")
        save_tips = driver.execute_script("return document.querySelector('.page-teenagers-save')")
        datebase_notice = driver.execute_script("return document.querySelector('.database-notice-box')")

        if percent_ele is not None:
            wait.until(EC.staleness_of(percent_ele))
        if loading_ele is not None:
            wait.until(EC.staleness_of(loading_ele))
        if popover is not None:
            wait.until(EC.invisibility_of_element(popover))
        if save_tips is not None:
            wait.until(EC.invisibility_of_element(save_tips))
        if datebase_notice is not None:
            sleep(.5)
            driver.find_element_by_css_selector(".database-notice-box .submit").click()
            sleep(1)
    except:
        pass


def link_to_cds(driver, g_config, crm_casecode):
    logincrm_or_cds(driver, g_config, "crm_url")
    searchPatient(driver, crm_casecode)
    key_trans.switch_to_cur_win(driver, lambda: driver.find_element_by_css_selector("#pause_tasks_open").click())
    driver.switch_to.frame("otherPage")
    driver.find_element_by_css_selector(".todo-tasklist-list:last-child").click()

#仅仅到cds页面
def switch_to_cds_handler(mainhandler, case):
    driver = mainhandler.driver
    case_id = case.get("id")
    val = case.get("val")
    crm_casecode = ""
    if val != "":
        val_dict = eval(val)
        crm_casecode = val_dict.get("crm_casecode")
    if crm_casecode == "":
        crm_casecode = to_get_casecode(mainhandler.driver, mainhandler.g_config.get("iortho_url"))
    logincrm_or_cds(driver, mainhandler.g_config, "crm_url")
    searchPatient(driver, crm_casecode)
    key_trans.switch_to_cur_win(driver, lambda: driver.find_element_by_css_selector("#pause_tasks_open").click())
    driver.switch_to.frame("otherPage")
    driver.find_element_by_css_selector(".todo-tasklist-list:last-child").click()

#将页面拖动到底部
def page_drag_end_handler(mainhandler, case):
    selector=case.get("selector")
    print(selector)

    driver = mainhandler.driver
    if selector !=None and selector !="":
        if selector.startswith("/"):

            js=f"document.evaluate('{selector}', document).iterateNext().scrollTop=10000"
            print(js)
        else:

            js=f"document.querySelector('{selector}').scrollTop=10000"
    else:

        js = "document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    sleep(1)

#将当前页面拖到最底部
def page_drag_end1_handler(mainhandler, case):
    driver = mainhandler.driver
    js = "var action=document.documentElement.scrollTop=100000"
    driver.execute_script(js)
    sleep(1)
#将页面拖动到最顶部
def page_drag_top_handler(mainhandler, case):
    driver = mainhandler.driver
    js = "var action=document.documentElement.scrollTop=0"
    driver.execute_script(js)
    sleep(1)

def create3d_auto_handler(mainhandler):
    driver = mainhandler.driver
    t_opt = mainhandler.t_opt
    dir_name = getOdsFile(t_opt.get("phase"),t_opt.get("type"),t_opt.get("update"))
    casecode = t_opt.get("casecode")
    if casecode is None:
        login_iortho_handler(mainhandler)
        casecode = to_get_casecode(mainhandler.driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler)
    ods = rename_file(casecode, dir_name)
    sleep(5)
    searchPatient(driver, casecode)
    key_trans.switch_to_cur_win(driver, lambda: driver.find_element_by_css_selector("#pause_tasks_open").click())
    uploadStlAndDdm(driver, ods)
    dsignScheme(driver)
    uploadOds(driver, ods)
    acceptAlert(driver)
    # close_tab(driver, 2)
    # goto_case_detail(driver, mainhandler.g_config.get("iortho_url"), casecode)
    # wait_for_3d_ele(driver)

#结束当前阶段关键字
def finish_phase_auto_handler(mainhandler):
    driver = mainhandler.driver
    casecode = mainhandler.t_opt.get("casecode")
    if casecode is None:
        casecode = to_get_casecode(driver, mainhandler.g_config.get("iortho_url"))
    logincrm_handler(mainhandler)
    sleep(5)
    searchPatient(driver, casecode)
    finish_phase(driver)
# 刷新
def refresh_handler(mainhandler, case):
    driver = mainhandler.driver

    driver.refresh()
    sleep(2)

