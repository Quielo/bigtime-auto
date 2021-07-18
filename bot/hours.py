import bot.objects as o
import bot.setup as s

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ex

from time import sleep

import pyautogui as pai

# Objects
lists = o.selectLists
week = o.week
save = o.save
mon = "td:nth-of-type(4) > .hours-inner > .ng-binding.total-hours"
tue = "td:nth-of-type(5) > .hours-inner > .ng-binding.total-hours"
wed = "td:nth-of-type(6) > .hours-inner > .ng-binding.total-hours"
thu = "td:nth-of-type(7) > .hours-inner > .ng-binding.total-hours"
fri = "td:nth-of-type(8) > .hours-inner > .ng-binding.total-hours"

def weekwork():

    for day in week:
        driver.find_element_by_css_selector(day).click()
        pai.typewrite('8')

# setup
driver = s.driver

def hours():
    global monday
    global tuesday
    global wednesday
    global thursday
    global friday
    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, lists)))

    driver.find_element_by_css_selector(lists).click()
    sleep(1)
    weekwork()
    sleep(2)
    monday = driver.find_element_by_css_selector(mon).text
    tuesday = driver.find_element_by_css_selector(mon).text
    wednesday = driver.find_element_by_css_selector(mon).text
    thursday = driver.find_element_by_css_selector(mon).text
    friday = driver.find_element_by_css_selector(mon).text

    # driver.find_element_by_css_selector(save).click()

    #driver.close()
    #driver.quit()

global monday
global tuesday
global wednesday
global thursday
global friday
