
from time import sleep
def serachIorthoPathient(driver,name):
    driver.find_element_by_class_name('app--0609e9').clear()
    driver.find_element_by_class_name('app--0609e9').send_keys(name)
    sleep(1)
    driver.find_element_by_class_name('searchResult--27e11a').click()
    sleep(2)
