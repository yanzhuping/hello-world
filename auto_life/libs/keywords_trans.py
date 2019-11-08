from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from libs.fun_case import logincrm_or_cds
from libs.fun_case import login_iortho
from libs.test_utils import *
from libs.create_3d import *
from libs.process_3d import Process3D
import filecmp
import base64
from libs.global_vars import *
from xpinyin import Pinyin
from selenium.common.exceptions import TimeoutException


# 处理关键字input
def input_handler(mainhandler, case=None):
    g_config = mainhandler.g_config
    val = str(case.get("val"))
    id = case.get("id")
    driver = mainhandler.driver
    input_val = str(int(val)) if isinstance(val, float) else val
    selector = case.get("selector")
    if case.get("selector") == '[ng-model="$ctrl.case_base.patientName"]' and val == "":
        input_val = readDataFromMySQL(g_config)
        mainhandler.patient_name = input_val
        deleteDataFromMySQL(g_config)
    if val in ("photo_random", "stl_random"):
        input_val = random.choice(choice_file(val.split("_")[0]))
    get_element(driver, selector).send_keys(input_val)
    check_loading_is_hide(driver)
    # 图片文件上传之后保存到本地 后面校验对比用
    if val == "photo_random":
        selector = selector.replace("#", ".")
        selector = selector.replace("others", "other")
        img_selector = "{} angel-image img".format(selector)
        photo_type_name = get_photo_type_name(driver, selector)
        save_photo_to_local(driver, img_selector, "{}-{}.png".format(id, photo_type_name))
    if val == "stl_random":
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
    login_iortho(mainhandler.driver, mainhandler.g_config)


# 处理sleep关键字
def sleep_handler(mainhandler, case=None):
    sleep(case.get("val"))


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
        if store_case_selector == "" or store_case_val == "" or store_case_keywords in NOT_CHECK_KEYLIST:
            continue
        if store_case_val == "next_page" or store_case_val == "after_click":
            get_element(driver, store_case_selector).click()
            continue
        if store_case_val == "pre_click":
            get_element(driver, store_case_selector).click()
        if store_case_val == "photo_random":
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
        elif store_case_val == "stl_random":
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
    goto_case_detail(driver, mainhandler.g_config.get("iortho_url"), casecode)
    wait_for_3d_ele(driver)


# 处理process3d关键字
def process3d_handler(mainhandler, case):
    switch_to_cur_win(mainhandler.driver)
    casecode = to_get_casecode(mainhandler.driver, mainhandler.g_config.get("iortho_url"), 2)
    process3d = Process3D(mainhandler, casecode, case.get("id"))
    # 下面是3d的一整套流程 后面再整理
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
    logincrm_or_cds(driver, mainhandler.g_config, "crm_url")
    searchPatient(driver, crm_casecode)
    key_trans.switch_to_cur_win(driver, lambda: driver.find_element_by_css_selector("#pause_tasks_open").click())
    driver.switch_to.frame("otherPage")
    driver.find_element_by_css_selector(".todo-tasklist-list:last-child").click()
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
    if xray_ele.is_displayed():
        xray_ele.click()
        sleep(.5)
        cds_xray_dict = get_cds_image(driver, "#viewXRayThumbnail .col-xs-4")
        driver.find_element_by_css_selector("#myModalXRay .i18n_historyshow_close").click()
        sleep(.5)
    # 比较文件差异
    compare_save_check_file(driver, {**cds_photo_dict, **cds_xray_dict}, case_id)


# 校验cds加工单
def check_cds_prescription_handler(mainhandler, case):
    driver = mainhandler.driver
    driver.find_element_by_css_selector("#CASEDATA .i18n_historyshow_order").click()
    sleep(.5)
    driver.find_element_by_css_selector("#photo-7 .i18n_historyshow_browse").click()
    sleep(.5)
    driver.find_element_by_css_selector("#casedataID tr:last-child td:first-child a").click()
    switch_to_cur_win(driver)
    driver.execute_script('document.querySelector(".check-success .product-info").remove()')
    cds_text = driver.find_element_by_css_selector(".check-success").text
    cds_text = cds_text.replace("(如选择无法确定复诊周期，则所有临床操作将设计在第1步)", "")
    cds_text = re.sub(r"[\s\n:：，, ]", "", cds_text)
    open_patient_detail(driver, mainhandler.g_config.get("iortho_url"))
    check_case_selector = u"timezone-input>div[button-content='查看病例']:not(.ng-hide)"
    wait_for_ele(driver, check_case_selector)
    driver.find_element_by_css_selector(check_case_selector).click()
    switch_to_cur_win(driver)
    sleep(2)
    # 去除iortho和cds的差异
    driver.execute_script('document.querySelector(".check-success>.title").remove();'
                          'document.querySelector(".check-success>.photos>.section-title").remove();'
                          'document.querySelector(".check-success>.photos>.section-body").innerHTML=document.querySelector(".check-success>.photos>.section-body>.key-value-box:last-child").innerHTML;'
                          'document.querySelector(".photos .section-body .extends").remove()'
                          )
    iortho_text = driver.find_element_by_css_selector(".check-success").text
    iortho_text = re.sub(r"[\s\n:：，, ]", "", iortho_text)
    if iortho_text != cds_text:
        raise Exception("cds加工单校验失败")
    else:
        print("cds加工单校验成功")
    close_tab(driver, 4)


# 关闭浏览器标签页关键字
def close_tab_handler(mainhandler, case):
    val = case.get("val")
    num = 1
    if isinstance(val, float):    #将浮点数转换成整型
        num = str(int(val))
    close_tab(mainhandler.driver, num)

# ----assert_handler--------------------------------------------------------------------


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
        if ele and assert_val == "False":
            raise Exception(f"{desc} {selector} 校验失败")
        else:
            print(f"{desc} {selector} 校验成功")
    except TimeoutException:
        # 获取元素超时
        if assert_val == "True":
            raise Exception(f"{desc} {selector} 校验失败")
        else:
            print(f"{desc} {selector} 校验成功")


#  处理assert关键字
def assert_handler(mainhandler, case):
    val = case.get("val")
    selector = case.get("selector")
    desc = case.get("desc")
    assert_key, assert_val = val.split(":")
    globals().get(f"assert_{assert_key}_handler")(mainhandler.driver, selector, assert_val, desc)

#############################################################################################


# 关闭tab页并且切换到前一个tab num:需要关闭的窗口数量
def close_tab(driver, num=0):
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
        if case_id in filename and "_check" not in filename and "_cds" not in filename:
            short_name = filename.split(".")[0]
            photo_type_name = short_name.split("-")[1]
            img_url = img_url_dict.get(photo_type_name)
            cds_img_filepath = os.path.join(SAVE_CHECK_PATH, short_name + "_cds.png")
            save_file(driver, cds_img_filepath, img_url)
            result = img_hash_compare(filepath, cds_img_filepath, 5)
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
    for index, _ in enumerate(ele_list):
        # 照片属于哪个类型 正面像、侧面像还是。。。
        ele_name = driver.find_element_by_css_selector(f"{selector}:nth-child({index+2}) .caption>h5:nth-child(3)")
        photo_type_name = p.get_pinyin(ele_name.text.split("类型：")[1], '')
        if 'qita' in photo_type_name:
            photo_type_name = f"{photo_type_name}_{other_num}"
            other_num = other_num + 1
        img_url_list[photo_type_name] = get_ele_src(driver, f"{selector}:nth-child({index+2}) .main_img img")
    return img_url_list


def open_url(driver, url, g_config=None):
    if url is not None:
        if url in ("iortho_url", "crm_url", "cds_url"):
            url = g_config.get(url)
        switch_to_cur_win(driver, lambda: driver.execute_script("window.open('{}')".format(url)))


# 均值哈希算法得到图片hash值然后做比较 # 容错值默认暂定为3
def img_hash_compare(filename1, filename2, e_value=3):
    num = cmpHash(aHash(cv2.imread(filename1)), aHash(cv2.imread(filename2)))
    return num <= e_value


def save_stl_data(mainhandler, selector, id):
    driver = mainhandler.driver
    value, index = get_stl_val(driver, selector)
    if mainhandler.case_variable.get(id) is None:
        mainhandler.case_variable[id] = {}
    mainhandler.case_variable[id]["stl"+index] = value


# 获取stl input框显示的值
def get_stl_val(driver, selector):
    index = selector.split("stl_")[1]
    selector = f'[ng-model*=\"fileUrl\"][ng-model$=\"{index}\"]'
    wait_for_ele(driver, selector)
    ele = f"document.querySelector('{selector}')"
    value = driver.execute_script("{0}.scrollIntoView();return {0}.value".format(ele))
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
    wait = WebDriverWait(driver, 60, 3)
    if is_hidden:
        wait.until(EC.invisibility_of_element(get_element(driver, selector, True)))
    else:
        global wait_to_get_selector_opt
        wait_to_get_selector_opt["is_need_refresh"] = is_need_refresh
        wait_to_get_selector_opt["selector"] = selector
        wait.until(do_get_ele)


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
    # 某些click关键却要校验input的值 需要在excel中的操作值中写上val:期望值 比如：val:2000-01-01
    is_s_val = isinstance(val, str) and val.startswith("val")
    if keywords == 'input' or is_s_val:
        if is_s_val:
            val = val.split("val:")[1]
        if isinstance(val, float):
            val = str(int(val))
        return val == get_element(driver, case.get("selector")).get_attribute('value')
    elif keywords == 'click':
        return get_element(driver, case.get("selector")).is_selected()


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
    wait = WebDriverWait(driver, 15, 0.5)
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
    wait = WebDriverWait(driver, 40, 0.5)
    loading_ele = driver.execute_script("return document.querySelector('.iortho-global-loading')")
    percent_ele = driver.execute_script("return document.querySelector('#fileupload_loadingImg')")
    popover = driver.execute_script("return document.querySelector(\"[ng-show=\'$ctrl.popoverShow\']\")")
    if percent_ele is not None:
        wait.until(EC.staleness_of(percent_ele))
    if loading_ele is not None:
        wait.until(EC.staleness_of(loading_ele))
    if popover is not None:
        wait.until(EC.invisibility_of_element(popover))




