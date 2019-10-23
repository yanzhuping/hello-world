#登陆CRM
def Login(driver,base_url,username,password):
    # try:
    #     driver.set_page_load_timeout(10)
    #     driver.get(base_url)
    # except:
    #     driver.execute_script("window.stop()")
    # driver.find_element_by_css_selector("#username").send_keys(username)
    # driver.find_element_by_css_selector("#password").send_keys(password)
    # driver.find_element_by_css_selector(".btn-submit").click()
    try:
        driver.get(base_url)
        driver.find_element_by_css_selector("#username").send_keys(username)
        driver.find_element_by_css_selector("#password").send_keys(password)
        driver.find_element_by_css_selector(".btn-submit").click()
    except:
        pass






