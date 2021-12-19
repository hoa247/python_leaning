from selenium import webdriver
from os.path import dirname, abspath
import os
from time import sleep
from random import randint


def sleeprandom(a = 1, b = 3):
    sleep(randint(a, b))


driver_path = os.path.join(dirname(abspath(__file__)), 'driver', 'chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get('http://google.vn')
sleeprandom()
driver.find_element_by_name('q').send_keys('hehe')
sleeprandom()
driver.find_element_by_name('btnK').submit()
print('done')