from selenium import webdriver


def browser():

    # 无头模式
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1500,900')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver=webdriver.Chrome()

    driver.implicitly_wait(10)
    # driver.maximize_window()
    # driver.set_window_size(1920,1080)

    return driver