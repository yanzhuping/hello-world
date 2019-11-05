#登陆CRM
def loginCrm(driver,base_url,username,password):
    try:
        driver.get(base_url)
        driver.find_element_by_css_selector("#username").send_keys(username)
        driver.find_element_by_css_selector("#password").send_keys(password)
        driver.find_element_by_css_selector(".btn-submit").click()
    except:
        pass





