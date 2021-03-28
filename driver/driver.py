from selenium import webdriver
import os
from libs.test_utils import get_root_path
from time import ctime
import threading


def browser():

    # 无头模式
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1500,900')

    chrome_options.add_argument('--ignore-certificate-errors')
    # 无头模式打印日志级别 INFO = 0,WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3 default is 0
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('log-level=3')
    chrome_options.add_argument('--ignore-certificate-errors')

    # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
    # chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    experimentalFlags = [
        "same-site-by-default-cookies@2",
        "cookies-without-same-site-must-be-secure@2",
    ]
    chromeLocalStatePrefs = {
        "browser.enabled_labs_experiments": experimentalFlags
    }
    chrome_options.add_experimental_option("localState", chromeLocalStatePrefs)

    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver.set_network_conditions(offline=False, latency=5, throughput=200 * 1024)

    driver.implicitly_wait(20)
    driver.maximize_window()

    return driver


def select_browser(bro):
    print("start %s"%browser,ctime())
    try:
        if bro == 'Chrome':
            driver=webdriver.Chrome()
        elif bro == "Firefox":
            driver=webdriver.Firefox()
        elif bro == "Ie":
            driver = webdriver.Ie()
        else:
            print("Not found %s browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ "% browser)
        return driver
    except Exception as msg:
        print("启动浏览器出现异常：%s" % str(msg))

#封装一个threading多线程方法，参数必须传元组
def thread_browser(*args):
    if args:
        threads=[] #创建一个线程列表
        for browser in args:
            t=threading.Thread(target=fun,args=(browser,))   #创建线程
            threads.append(t)
        for t in threads:
            t.start()  #启动线程
        for t in threads:
            t.join()   #守护线程

        print("end all time %s"%ctime())
    else:
        print("please input at least one browser name")

