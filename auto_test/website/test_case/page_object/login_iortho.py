from time import sleep

def login_iortho(driver,url,username,password):
    driver.implicitly_wait(10)
    driver.get(url)
    sleep(1)
    driver.maximize_window()
    driver.switch_to.frame("the-real-login-page")
    driver.find_element_by_id("_username").send_keys(username)
    driver.find_element_by_id("_password").send_keys(password)
    driver.find_element_by_id("_btn_login").click()
    sleep(3)



