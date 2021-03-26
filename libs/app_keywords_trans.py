from time import sleep
import os
import re
import json

from selenium.common.exceptions import NoSuchElementException

from libs.test_utils import *
from libs.app_test_utils import *
from libs.global_vars import *
import math
import subprocess
import datetime
import time
import threading
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.keys import Keys

from xpinyin import Pinyin

from PIL import Image

from libs.keywords_trans import link_to_cds, get_cds_image, save_file, img_hash_compare
screenShortName = ''
partScreenShortName = ''


#获取元素定位
def finEleBy(driver, selector):
    if selector.startswith('~'):
        return driver.find_element_by_accessibility_id(selector[1:])
    elif selector.find("/") == -1:
        if selector.find('#') == -1 and selector.find(
                '.') == -1 and selector.find('[') == -1:
            selector = '#' + selector
        print(selector)
        return driver.find_element_by_css_selector(selector)
    else:
        print('xpath')
        return driver.find_element_by_xpath(selector)


# 查找元素尝试5次
def testEle(mainhandler, selector, isExit=True, maxRetry=6):
    print('查找元素中')
    if maxRetry <= 0:
        print("尝试找寻6次，但仍未找到元素，终止程序")
        if isExit:
            os._exit(0)
            print("继续寻找下一个元素", os._exit(0))
        return

    def wait_until_in_view():
        _selector = selector
        ele = finEleBy(mainhandler.driver, _selector)
        if ele.is_displayed():
            print(33333)
            return ele
        else:
            print(f"不在视野内，sleep{6 - maxRetry}秒")
            sleep(6 - maxRetry)
            raise Exception('should retry')

    try:
        return wait_until_in_view()
    except:
        sleep(6 - maxRetry)
        print(f"元素{selector}找不到，sleep{6 - maxRetry}秒")
        return testEle(mainhandler, selector, isExit, maxRetry - 1)


##一直查找元素
def getEle(driver, selector):
    try:
        ele = finEleBy(driver, selector)
        if ele.is_displayed():
            return ele
        else:
            raise Exception('should retry')
    except:
        sleep(1)
        print(f"方法：getEle,元素{selector}找不到")
        return getEle(driver, selector)


#登录
def app_login_handler(mainhandler, case=None):
    try:
        username = testEle(mainhandler, "//*[@resource-id='_username']")
        username.set_value(mainhandler.g_config.get("iortho_username"))
        pwd = testEle(mainhandler, "//*[@resource-id='_password']")
        pwd.set_value(mainhandler.g_config.get("iortho_password"))
        btn = testEle(mainhandler, "//*[@resource-id='_btn_login']")
        btn.click()
    except:
        print("登录失败")
        pass


#登录
def app_ios_login_handler(mainhandler, case=None):
    username = mainhandler.driver.find_element_by_css_selector('#_username')

    print(username)
    username.send_keys(mainhandler.g_config.get("iortho_username"))

    pwd = mainhandler.driver.find_element_by_css_selector('#_password')
    pwd.send_keys(mainhandler.g_config.get("iortho_password"))
    btn = mainhandler.driver.find_element_by_css_selector('#_btn_login')
    btn.click()


#click点击事件
def app_click_handler(mainhandler, case=None):
    starttime = datetime.datetime.now()
    idnum = case.get("id")
    idselector = case.get("selector")
    getEle(mainhandler.driver, idselector).click()
    endtime=datetime.datetime.now()
    time_subtraction = endtime - starttime
    print(
        f"id:{idnum}，click_selector:{idselector},time_subtraction:{time_subtraction}"
    )


#点击切换窗口
def app_click_num_handler(mainhandler, case=None):
    starttime = datetime.datetime.now()
    idnum = case.get("id")
    idselector = case.get("selector")
    driver = mainhandler.driver
    app_switch_to_cur_win_ifchange(
        driver,
        lambda: testEle(mainhandler.driver, case.get("selector")).click())

    endtime = datetime.datetime.now()
    time_subtraction = endtime - starttime
    print(
        f"id:{idnum}，click_selector:{idselector},time_subtraction:{time_subtraction}"
    )

#切换窗口
def app_switch_to_cur_win_ifchange(driver, exec_fun=None):
    if exec_fun is not None:
        exec_fun()
    pre_win_num = len(driver.window_handles)
    all_win = driver.window_handles
    cur_win_num = len(all_win)
    if cur_win_num != pre_win_num:
        driver.switch_to.window(all_win[cur_win_num - 1])


#tap点击事件
def app_tap_handler(mainhandler,
                    case=None,
                    check=False,
                    need_screenshort=False):
    val = case.get('val')
    if need_screenshort == True and val == 'next_page':
        screenshot_app(mainhandler, case, check)
        # pic_masaic()
    starttime = datetime.datetime.now()
    selector = case.get("selector")
    idnum = case.get("id")
    el = getEle(mainhandler.driver, selector)
    endtime = datetime.datetime.now()
    time_subtraction = endtime - starttime
    if selector.find("[for=") != -1:
        el.click()
    mainhandler.driver.execute_script(
        "arguments[0].dispatchEvent(new CustomEvent('tap', {detail: {},bubbles: true,cancelable: true}));",
        el)
    print(
        f"id:{idnum}，tap_selector:{selector},time_subtraction:{time_subtraction}"
    )


def app_tap_ignore_handler(mainhandler, case=None):
    selector = case.get("selector")
    val = case.get('val')
    el = testEle(mainhandler, selector, False)
    if not el:
        return

    mainhandler.driver.execute_script(
        "arguments[0].dispatchEvent(new CustomEvent('tap', {detail: {},bubbles: true,cancelable: false}));",
        el)


#click点击事件--找不到元素可以忽略
def app_click_ignore_handler(mainhandler, case=None):
    starttime = datetime.datetime.now()
    idnum = case.get("id")
    idselector = case.get("selector")
    testEle1 = testEle(mainhandler, idselector, False)
    if testEle1 is not None:
        testEle1.click()
    endtime = datetime.datetime.now()
    time_subtraction = endtime - starttime
    print(
        f"id:{idnum}，selector:{idselector},time_subtraction:{time_subtraction}"
    )


# 处理sleep关键字
def app_sleep_handler(mainhandler, case=None):
    val = case.get("val")
    num = val if val is not None and val != "" else 1
    sleep(int(num))


#输入框input事件
def app_input_handler(mainhandler, case=None):
    g_config = mainhandler.g_config
    val = str(case.get("val"))
    id = case.get("id")
    driver = mainhandler.driver
    input_val = format_digit_str(val)
    selector = case.get("selector")
    if val == 'patientName':
        input_val = readDataFromMySQL(g_config)
        mainhandler.patient_name = input_val
        deleteDataFromMySQL(g_config)

    getEle(mainhandler.driver, selector).send_keys(input_val)
    mainhandler.driver.hide_keyboard()


#搜索框input事件
def app_search_input_handler(mainhandler, case=None):
    g_config = mainhandler.g_config
    val = str(case.get("val"))
    id = case.get("id")
    driver = mainhandler.driver
    input_val = format_digit_str(val)
    selector = case.get("selector")
    if val == 'patientName':
        input_val = readDataFromMySQL(g_config)
        mainhandler.patient_name = input_val
        deleteDataFromMySQL(g_config)

    getEle(mainhandler.driver, selector).send_keys(input_val)


#app自动化按键 4返回
def keyevent_handler(mainhandler,case=None,val=4):
    if case.get("val")!='':
        val = format_digit_str(str(case.get("val")))
    driver = mainhandler.driver
    driver.keyevent(val)
    print(val,'手机控制键')
    ctxs = mainhandler.driver.contexts
    print(f'当前窗口{ctxs}')



#输入框texarea事件
def app_textarea_handler(mainhandler, case=None):
    selector = case.get("selector")
    val = case.get("val")
    el = testEle(mainhandler, selector)
    mainhandler.driver.execute_script(
        "var setValue = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;setValue.call(arguments[0], arguments[1])",
        el, val)
    mainhandler.driver.execute_script(
        "arguments[0].dispatchEvent(new CustomEvent('input', {detail: {},bubbles: true,cancelable: true}));",
        el)

    # js = f"var element = document.getElementById('{selector}');"
    # mainhandler.driver.execute_script(js + "var event = new Event('input', { bubbles: true });element.dispatchEvent(event);")


#向上滑动处理
def swipeUp_handler(mainhandler, case=None):
    if case.get("val") != '':
        swipeUp(mainhandler.driver, int(case.get("val")))
    else:
        swipeUp(mainhandler.driver)


# 向下滑动处理
def swipeDown_handler(mainhandler, case=None):
    if case.get("val") != '':
        swipeDown(mainhandler.driver, int(case.get("val")))
    else:
        swipeDown(mainhandler.driver)


#元素滑动到视图内处理
def swipeElement_down_handler(mainhandler,
                              case=None,
                              check=False,
                              need_screenshort=False):
    starttime = datetime.datetime.now()
    idnum = case.get("id")
    idselector = case.get("selector")
    selector = case.get("selector")
    if selector.find('#') == -1 and selector.find('.') == -1 and selector.find(
            '[for=') == -1:
        selector = '#' + selector
    val = case.get('val')
    if need_screenshort and val:
        if selector.find('pic') != -1:
            sleep(20)
        screenshot_app(mainhandler, case, check)
    print(selector)
    mainhandler.driver.execute_script(
        f"return document.querySelector('{selector}').scrollIntoView()")
    endtime = datetime.datetime.now()
    time_subtraction = endtime - starttime
    print(
        f"id:{idnum}，selector:{idselector},time_subtraction:{time_subtraction}"
    )


def app_login_iortho_handler(mainhandler, case=None):
    password = ""
    username = ""
    val = ""
    if case is not None:
        val = str(case.get("val"))
    if val != "":
        val = eval(val)
        username = val.get("username")
        password = val.get("password")
        print(username, password)
    try:
        username1 = testEle(mainhandler, "//*[@resource-id='_username']",False)
        print('-------',username1)
        if username1 is None:
            print(username1,'直接登录')
            pass
        else:
            username1.set_value(username if username != "" else mainhandler.
                                g_config.get("iortho_username"))
            pwd = testEle(mainhandler, "//*[@resource-id='_password']",False)
            pwd.set_value(password if password != "" else mainhandler.g_config.
                          get("iortho_password"))
            btn = testEle(mainhandler, "//*[@resource-id='_btn_login']")
            btn.click()
    except Exception as e:
        print('异常:', e)


def app_scroll_handler(mainhandler, case=None):
    idnum = case.get("id")
    val = str(case.get("val"))
    selector = case.get("selector")
    ele = mainhandler.driver.find_element_by_id(selector)
    sleep(1)
    mainhandler.driver.swipe(ele.location['x'] + ele.size['width'] / 2,
                             (ele.location['y'] + ele.size['height']) * 0.9,
                             ele.location['x'] + ele.size['width'] / 2,
                             (ele.location['y'] + ele.size['height']) * 0.2,
                             200)
    print(f"scroll,selector:{selector},{ele.location},{ele.size}")
    sleep(2)
#移动元素
def drag_and_drop_random_handler(mainhandler, case=None):
    id = case.get('id')
    val = str(case.get("val"))
    selector = case.get("selector")
    print("val:" + val)
    print("selector:" + selector)

    if (mainhandler.driver.desired_capabilities.get('platformName') ==
            'Android'):
        start = getEle(mainhandler.driver, selector).size
        #start=mainhandler.driver.find_element_by_xpath(selector)
        print('start坐标:',start)
        # print('通过xpath定位方法获取当前元素坐标：',start.location)
        end = getEle(mainhandler.driver, val)
        print('结束位置：',end)
        # end1=(start.location['x'] ) / 2
        # end2=(start.location['y'] ) / 2
        # end1,end2=swipeUp(mainhandler.driver)
        # end1=int(end1)
        # end2=int(end2)
        # print('end1',end1)
        # print('end2:',end2)
        #print('拖动后的坐标',int(end1).int(end2))
        action = TouchAction(mainhandler.driver)
        action.press(start).move_to(end).release().perform()
    else:
        params = {
            'duration':
            1.0,
            'fromX':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{selector}').getBoundingClientRect().left"
            ) + 1,
            'fromY':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{selector}').getBoundingClientRect().bottom"
            ) - 1,
            'toX':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{val}').getBoundingClientRect().left"
            ) + 1,
            'toY':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{val}').getBoundingClientRect().bottom"
            ) - 1
        }

        mainhandler.driver.execute_script("mobile: dragFromToForDuration",
                                          params)
# 拖模拟bar
def drag_class_handler(mainhandler, case=None):
    id = case.get('id')
    val = str(case.get("val"))
    selector = case.get("selector")
    print("val:" + val)
    print("selector:" + selector)
    if (mainhandler.driver.desired_capabilities.get('platformName') ==
            'Android'):
        start = getEle(mainhandler.driver, selector)
        end = getEle(mainhandler.driver, val)
        # size = mainhandler.driver.get_window_size()
        # # 获取屏幕宽度 width
        # width = size['width'] - 200
        # # 获取屏幕高度 height
        # height = size['height']+30
        # print(width,height)
        action = TouchAction(mainhandler.driver)
        action.press(start).move_to(end).release().perform()
    else:
        params = {
                'duration':
                1.0,
                'fromX':
                mainhandler.driver.execute_script(
                    f"return document.querySelector('{selector}').getBoundingClientRect().left"
                ) + 1,
                'fromY':
                mainhandler.driver.execute_script(
                    f"return document.querySelector('{selector}').getBoundingClientRect().bottom"
                ) +15,
                'toX':
                mainhandler.driver.execute_script(
                    f"return document.querySelector('{val}').getBoundingClientRect().left"
                ) + 1,
                'toY':
                mainhandler.driver.execute_script(
                    f"return document.querySelector('{val}').getBoundingClientRect().bottom"
                ) - 1
            }
        mainhandler.driver.execute_script("mobile: dragFromToForDuration",
                                            params)

#照片拖拽
def drag_and_drop_handler(mainhandler, case=None):
    id = case.get('id')
    val = str(case.get("val"))
    selector = case.get("selector")
    print("val:" + val)
    print("selector:" + selector)
    if (mainhandler.driver.desired_capabilities.get('platformName') ==
            'Android'):
        start = getEle(mainhandler.driver, selector)
        end = getEle(mainhandler.driver, val)
        # mainhandler.driver.drag_and_drop(start, end)
        action = TouchAction(mainhandler.driver)
        action.press(start).move_to(end).release().perform()
    else:
        params = {
            'duration':
            1.0,
            'fromX':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{selector}').getBoundingClientRect().left"
            ) + 1,
            'fromY':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{selector}').getBoundingClientRect().bottom"
            ) - 1,
            'toX':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{val}').getBoundingClientRect().left"
            ) + 1,
            'toY':
            mainhandler.driver.execute_script(
                f"return document.querySelector('#{val}').getBoundingClientRect().bottom"
            ) - 1
        }

        mainhandler.driver.execute_script("mobile: dragFromToForDuration",
                                          params)

def screenshort_handler(mainhandler, case=None, check=False):
    for store_case in mainhandler.case_store.get(case.get("id")):
        print(store_case)
        store_case_val = store_case.get("val")
        store_case_keywords = store_case.get("keywords")
        store_case_selector = store_case.get("selector")
        store_case_id = store_case.get("id")
        store_case_desc = store_case.get('desc')
        if store_case_val == "next_page":
            print(f"校验执行操作'{store_case_desc}'")
            globals().get(store_case_keywords + "_handler")(mainhandler,
                                                            store_case, check,
                                                            True)
            continue
        elif store_case_keywords == "swipeElement_down":
            if store_case_val:
                need_screenshort = True
            else:
                need_screenshort = False

            if need_screenshort == False:
                sleep(5)
            print(f"校验执行操作'{store_case_desc}'")
            globals().get(store_case_keywords + "_handler")(mainhandler,
                                                            store_case, check,
                                                            need_screenshort)
        else:
            continue


# 屏幕截图
def screenshot_app(mainhandler, case, check=False):
    case_id = case.get("id")
    val = case.get("val")
    p = Pinyin()
    suffix = ''
    prefix = ''
    global screenShortName
    global partScreenShortName
    if check:
        suffix = "_check.png"
    else:
        suffix = ".png"
    if val == 'next_page':
        if partScreenShortName == '':
            extra = ''
        else:
            extra = '_' + partScreenShortName.split(',')[1]
        prefix = p.get_initials(case_id, '') + p.get_pinyin(val, '') + extra
        partScreenShortName = ''
    else:
        prefix = p.get_initials(case_id, '') + p.get_pinyin(val, '')
        partScreenShortName = partScreenShortName + ',' + prefix
    filename = prefix + suffix
    if check == False:
        screenShortName = screenShortName + ',' + prefix
    print(f'screenShortName:{screenShortName}')
    mainhandler.driver.get_screenshot_as_file(
        os.path.join(APP_SAVE_CHECK_PATH, filename))


#合成截图
def pic_masaic():
    global partScreenShortName
    nameList = partScreenShortName.split(',')
    base_mat = np.atleast_2d(
        Image.open(os.path.join(APP_SAVE_CHECK_PATH, nameList[1] + '.png')))
    for name in nameList[2:]:
        if name == '':
            continue
        filename = os.path.join(APP_SAVE_CHECK_PATH, name + '.png')
        mat = np.atleast_2d(Image.open(filename))  # 打开截图并转为二维矩阵
        base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
        # os.remove(filename)
    path = os.path.join(APP_SAVE_CHECK_PATH,
                        '_'.join(partScreenShortName.split(',')) + '.png')
    Image.fromarray(base_mat).save(path)
    partScreenShortName = ''


# 子进程处理
def shell_handler(mainhandler, case=None):
    val = str(case.get("val"))
    global shell_data
    output = ''
    ret, output = subprocess.getstatusoutput(val)
    for line in output.split('\n'):
        if line.startswith('return msg'):
            shell_data = json.loads(line[10:])
            print(shell_data)
    print('ret')
    print(ret)
    if ret == 0:
        print("success", ret)
    else:
        print("fail", ret)
        raise Exception("子进程失败")


# 判断元素是否应该展示
def assert_ele_exist_handler(driver, selector, assert_val, desc, mainhandler):
    try:
        ele = ''
        if selector.startswith('~'):
            ele =  driver.find_element_by_accessibility_id(selector[1:])
        elif selector.find("/") == -1:
            if selector.find('#') == -1 and selector.find(
                    '.') == -1 and selector.find('[') == -1:
                selector = '#' + selector
            print(selector)
            ele = driver.find_element_by_css_selector(selector)
        else:
            print('xpath')
            ele= driver.find_element_by_xpath(selector)
        if ele and ele.is_displayed() != False and assert_val == False:
            # 当前元素展示且不应该展示
            raise Exception(f"当前元素展示且不应该展示{desc} {selector} {assert_val}校验失败")
        else:
            print(f"元素{ele}，展示：{ele.is_displayed()}")
            if ele.is_displayed() != assert_val:
                #元素隐藏
                raise Exception(f"当前元素隐藏且不应该展示{desc} {selector} {assert_val}校验失败")
            else:
                # 当前元素展示且应该展示
                print(f"当前元素展示且应该展示{desc} {selector} {assert_val}校验成功")
    except NoSuchElementException:
        # 获取元素超时且应该展示
        if assert_val == True:
            raise Exception(f"获取元素超时且应该展示{desc} {selector} {assert_val} 校验失败")
        else:
            # 没获取到元素
            print(f" 没获取到元素{desc} {selector} {assert_val} 校验成功")


# 判断元素是否被选中
def assert_is_checked_handler(driver, selector, assert_val, desc, mainhandler):
    if testEle(driver, selector).is_selected() != assert_val:
        raise Exception(f"{desc} {selector} 校验失败")
    else:
        print(f"{desc} {selector} 校验成功")


# 判断文本内容是否正确
def assert_text_handler(driver, selector, assert_val, desc, mainhandler):
    if testEle(driver, selector).text != assert_val:
        raise Exception(f"{desc} {selector} 校验失败")
    else:
        print(f"{desc} {selector} 校验成功")


def assert_handler(mainhandler, case):
    val = case.get("val")
    selector = case.get("selector")
    desc = case.get("desc")
    assert_key, assert_val = val.split(":")
    if assert_val in ['True', 'False']:
        assert_val = True if assert_val == 'True' else False
    globals().get(f"assert_{assert_key}_handler")(mainhandler.driver, selector,
                                                  assert_val, desc,
                                                  mainhandler)


# 切换context
def get_webview_handler(mainhandler, case):
    try:
        print(case.get("level"))
        ctxs = mainhandler.driver.contexts
        print(ctxs, case.get("val"))
        val = case.get("val")
        if (val == 'native'):
            mainhandler.driver.switch_to.context(ctxs[0])
        else:
            mainhandler.driver.switch_to.context(ctxs[-1])

        # # sleep(1)
        # print(f'当前webview{ mainhandler.driver.current_context}')
        # print(f'当前webview{ mainhandler.driver.current_window_handle}')
    except Exception as e:
        print('切换窗口异常', e)
# 切换sale模拟窗口
def get_webview_sale_handler(mainhandler, case):
    try:
        ctxs = mainhandler.driver.contexts
        print(ctxs, case.get("val"))
        val = case.get("val")

        if (val == 'native'):
            mainhandler.driver.switch_to.context(ctxs[0])
        else:
            mainhandler.driver.switch_to.context(ctxs[1])

        # # sleep(1)
        # print(f'sale当前webview{ mainhandler.driver.current_context}')
        # print(f'sale当前webview{ mainhandler.driver.current_window_handle}')
    except Exception as e:
        print('切换窗口异常', e)


def switch_to_cur_win_handler(mainhandler, case):
    all_win = mainhandler.driver.window_handles
    all_win_num = len(all_win)
    mainhandler.driver.switch_to.window(all_win[all_win_num - 1])
    print(f'所有的window{all_win}')
    print(f'当前webview{ mainhandler.driver.current_window_handle}')


# 读取JS代码
# def get_script(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         js_script = f.read()
#         return js_script

# 获取元素的src
# def get_ele_src(driver, selector):
#     print(selector)
#     # wait_for_ele(driver, selector)
#     # sleep(1.5)s
#     ele = "document.querySelector('{}')".format(selector)
#     driver.execute_script(f"{ele}.scrollIntoView();")
#     return driver.execute_script(f"return {ele}.getAttribute('src')")

# def save_file(driver, filename, image_url):
#     print("image_url")
#     print(image_url)
#     driver.execute_script(
#         get_script(os.path.join(get_root_path(), "libs", "downloadUtils.js")))
#     result = driver.execute_async_script(
#         get_script(os.path.join(get_root_path(), "libs", "downloadUtils.js")) +
#         ";getFile('{}')".format(image_url))
#     with open(filename, 'wb') as f:
#         f.write(base64.b64decode(result.split(",")[1]))
#     # cds的照片等比例缩放到高度153 和iortho一致
#     if "_cds" in filename:
#         resize_img(ori_img=filename, dst_img=filename, dst_h=153)


# 差值哈希算法得到图片hash值然后做比较 # 容错值默认暂定为5
def app_img_hash_compare(filename1, filename2, e_value=5):
    return is_the_same_image(cv2.imread(filename1), cv2.imread(filename2))

    # print(num)
    # return num <= e_value



#暂存数据检测对比
def save_check_handler(mainhandler, case):
    sleep(1)
    driver = mainhandler.driver
    failed_count = 0
    error_msg = ""
    screenshort_handler(mainhandler, case, True)
    sleep(10)
    for name in screenShortName.split(','):
        if name == '':
            continue
        path1 = os.path.join(APP_SAVE_CHECK_PATH, name + '.png')
        path2 = os.path.join(APP_SAVE_CHECK_PATH, name + '_check.png')
        print(path1)
        print(path2)
        check_result = app_img_hash_compare(path1, path2)
        if check_result == False:
            failed_count = failed_count + 1

    if failed_count != 0:
        raise Exception('校验失败')
    else:
        print("-------暂存全部校验成功------")


def app_save_photo(driver, case_id):
    p = Pinyin()
    name_list = {
        '1-1': '侧面像',
        '1-2': '正面像',
        '1-3': '微笑像',
        '1-4': '上牙列像',
        '1-5': '下牙列像',
        '1-6': '口内右侧位像',
        '1-7': '口内正位像',
        '1-8': '口内左侧位像',
        '1-101': '前牙覆合覆盖像',
        '2-1': '全颌曲面断层片',
        '2-2': '头颅侧位定位片',
        '1-201': '下颌前伸位侧面像',
        '1-202': '下颌前伸位正面像',
        '1-205': '下颌前伸位口内右侧位像',
        '1-203': '下颌前伸位口内正位像',
        '1-204': '下颌前伸位口内左侧位像',
        '1-206': '下颌前伸位前牙覆合覆盖像',
    }
    els = driver.execute_script(
        f"return document.querySelectorAll('.photos .section-body .key-image-box')"
    )
    for el in els:
        iel = el.find_elements_by_css_selector('.image-box .image-box-wrapper')
        for i in iel:
            atttype = i.get_attribute('data-atttype')
            atttag = i.get_attribute('data-atttag')
            count = int(atttag)
            if atttype == '1' and count >= 9:
                photo_type_name = f"{p.get_pinyin(u'其他','')}_{count-9}"
            else:
                print('atttype', atttype)
                print('atttag', atttag)
                name_key = name_list.get(atttype + '-' + atttag)
                print('name_key', name_key)
                photo_type_name = p.get_pinyin(name_key, '')
            filename = "{}-{}.png".format(case_id, photo_type_name)
            img_el = i.find_element_by_css_selector('.angel-image img')
            img_src = img_el.get_attribute('src')
            print('img_src', img_src)
            save_app_photo_to_local(driver, img_src, filename)


# 保存照片到本地，用于后续校验
def save_app_photo_to_local(driver, img_src, filename):
    filepath = os.path.join(SAVE_CHECK_PATH, filename)
    save_file(driver, filepath, img_src)


def check_cds_img_handler(mainhandler, case):

    case_id = case.get('id')

    app_save_photo(mainhandler.driver, case_id)
    # 比较文件差异
    app_compare_save_check_file(mainhandler.driver, case_id)


# 校验save_check目录下的文件iortho和cds的对比
def app_compare_save_check_file(driver, case_id):
    filelist = list_dir(SAVE_CHECK_PATH)
    failed_count = 0
    error_msg = ""
    for filepath in filelist:
        filename = os.path.split(filepath)[1]
        if case_id in filename and re.search(r"_check|_cds|_detail",
                                             filename) is None:
            short_name = filename.split(".")[0]
            print("short_name")
            print(short_name)
            cds_img_filepath = os.path.join(SAVE_CHECK_PATH,
                                            short_name + "_cds.png")
            result = img_hash_compare(filepath, cds_img_filepath, 8)
            if result is False:
                print("{} 校验失败".format(short_name))
                failed_count = failed_count + 1
                error_msg = f"{error_msg}{short_name} 校验失败\n"

    if failed_count != 0:
        raise Exception(error_msg)
    else:
        print("-----cds_image全部校验成功-----")


# 校验cds加工单
def check_cds_prescription_handler(mainhandler, case):
    driver = mainhandler.driver
    app_cds_text = shell_data.get('app_cds_text')
    print(f'app_cds_text:{app_cds_text}')
    # 去除iortho和cds的差异
    driver.execute_script(
        'document.querySelector(".check-success>.title").remove();'
        'document.querySelector(".check-success>case-short-code").remove();'
        'document.querySelector(".check-success>.photos>.section-title").remove();'
        'document.querySelector(".check-success>.photos>.section-body").innerHTML=document.querySelector(".check-success>.photos>.section-body>.key-value-box:last-child").innerHTML;'
        'var extends_ele=document.querySelector(".photos .section-body .extends");'
        'if(extends_ele)extends_ele.remove();')
    iortho_text = driver.execute_script(
        f'return document.querySelector(".check-success").innerText')
    iortho_text = re.sub(r"[\s\n:：，, 、-]", "", iortho_text)
    print(f'iortho_text:{iortho_text}')
    iortho_text = app_cds_text.replace("20. 特殊说明: ", "")

    cds_text_len = len(app_cds_text)
    iortho_text_len = len(iortho_text)
    compile_len = 20
    num = math.ceil(iortho_text_len / compile_len)
    error_msg = ""

    for i in range(num):
        len_temp = compile_len * (i + 2)
        end_len = iortho_text_len if len_temp > iortho_text_len else len_temp
        iortho_text_temp = iortho_text[compile_len * (i + 1):end_len]
        end_len = cds_text_len if len_temp > cds_text_len else len_temp
        cds_text_temp = app_cds_text[compile_len * (i + 1):end_len]
        if iortho_text_temp != cds_text_temp:
            error_msg = f"{error_msg} 差异：cds（{cds_text_temp}）,iortho（{iortho_text_temp}）\n"
            break
    if error_msg != "":
        raise Exception(error_msg)
    else:
        print("cds加工单校验成功")

def quit_app_handler(mainhandler,case):
    mainhandler.driver.quit()
    print(case.get("val"))
    if (mainhandler.driver.desired_capabilities.get('platformName') ==
            'Android'):
        mainhandler.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_android)
    else:
        mainhandler.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_ios)
    sleep(3)
    print("app退出成功")

def switch_to_alert_handler(mainhandler,case):
    current = mainhandler.driver.current_context
    print('alert 同意')
    ctxs = mainhandler.driver.contexts
    mainhandler.driver.switch_to.context(ctxs[0])
    sleep(1)
    print(f'当前webview { mainhandler.driver.current_context}')
    mainhandler.driver.switch_to_alert().accept()
    sleep(1)
    if current.find('NATIVE')==-1:
        mainhandler.driver.switch_to.context(ctxs[-1])
    sleep(2)
    print(f'当前webview { mainhandler.driver.current_context}')
    print(f'当前webview { mainhandler.driver.current_window_handle}')
