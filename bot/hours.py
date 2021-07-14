import objects as o
import setup as s

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ex

from time import sleep

import pyautogui as pai

# Objects
lists = o.selectLists
week = o.week
save = o.save

def weekwork():

    for day in week:
        driver.find_element_by_css_selector(day).click()
        pai.typewrite('8')

# setup
driver = s.driver

def start():

    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, lists)))

    driver.find_element_by_css_selector(lists).click()
    sleep(1)
    weekwork()
    sleep(2)
    driver.find_element_by_css_selector(save).click()

