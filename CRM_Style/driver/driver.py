from selenium import webdriver

def browser():

    #无头模式
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--window-size=1920,1080')
    # driver = webdriver.Chrome(chrome_options=chrome_options)

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver