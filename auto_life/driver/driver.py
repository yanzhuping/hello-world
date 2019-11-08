from selenium import webdriver
import os
from libs.test_utils import get_root_path


def browser():

    # 无头模式
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--window-size=1500,900')
    # # 无头模式打印日志级别 INFO = 0,WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3 default is 0
    chrome_options.add_argument('log-level=3')
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    # prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
    # chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)
    driver.maximize_window()

    return driver
