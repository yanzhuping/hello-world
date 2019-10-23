from time import sleep

def select_product(driver,product_num):   #product_num:1是冠军版，2是标准版，3是儿童版，4是儿童+冠军版

    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/div/span[2]').click()
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/div[3]/span[1]').click()
    driver.find_element_by_xpath(
        '//*[@id="root-route"]/ui-view/page-case/div/ui-view/page-case-list/div/div/div[3]/div[2]/div/dl/dd[%d]'%product_num).click()