# from libs.test_utils import *
from time import sleep
from libs.test_utils import *
from libs.app_test_utils import *
from libs.keywords_trans import create3d_handler
import math
import subprocess

#app_enter
def app_enter_handler(mainhandler,case=None):
    mainhandler.driver.implicitly_wait(5)
    while True:
        allow_button_id = 'com.android.packageinstaller:id/permission_allow_button'
        try:
            l = mainhandler.driver.find_elements_by_id(allow_button_id)
            l[0].click()
            mainhandler.driver.implicitly_wait(2)
        except:
            break

    mainhandler.driver.implicitly_wait(2)
    mainhandler.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[4]/android.view.View[2]').click()
    mainhandler.driver.find_element_by_xpath(
        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]').click()
    while True:
        allow_button_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[5]'
        try:
            mainhandler.driver.find_element_by_xpath(allow_button_xpath).click()
            mainhandler.driver.implicitly_wait(2)
        except:
            break


def app_login_handler(mainhandler,case=None):
    try:
        sleep(10)
        mainhandler.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.EditText").send_keys(mainhandler.g_config.get("iortho_username"))
        mainhandler.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.widget.EditText").send_keys(mainhandler.g_config.get("iortho_password"))
        mainhandler.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.Button').click()
        sleep(3)
    except:
        pass

def app_click_handler(mainhandler,case=None):
    mainhandler.driver.find_element_by_xpath(case.get("selector")).click();

# 处理sleep关键字
def app_sleep_handler(mainhandler, case=None):
    val = case.get("val")
    num = val if val is not None and val != "" else 1
    sleep(num)

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
    mainhandler.driver.find_element_by_xpath(selector).send_keys(input_val)

def swipeUp_handler(mainhandler, case=None):
    if case.get("val") != '':
        swipeUp(mainhandler.driver,int(case.get("val")))
    else:
        swipeUp(mainhandler.driver)

def drag_and_drop_handler(mainhandler, case=None):
    val = str(case.get("val"))
    selector = case.get("selector")
    driver = mainhandler.driver
    start = driver.find_element_by_xpath(selector)
    end = driver.find_element_by_xpath(val)
    driver.drag_and_drop(start, end)

def shell_handler(mainhandler,case=None):
    val = str(case.get("val"))
    subprocess.call( val, shell=True)