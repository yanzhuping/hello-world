from time import sleep
from Auto_iortho.website.test_case.models.function import choice_photo
import random
from Auto_iortho.website.test_case.models.config import *

def uploadPhoto(driver):
    driver.find_element_by_id("pic-0").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-1").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-2").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-3").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-4").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-5").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-6").send_keys(random.choice(choice_photo()))
    sleep(0.5)
    driver.find_element_by_id("pic-7").send_keys(random.choice(choice_photo()))
    sleep(2)