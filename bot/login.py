import objects as o
import setup as s

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ex

from time import sleep

# Objects:
url = o.url
log1 = o.loginMain
user = o.username
passwd = o.password
log2 = o.loginSecond
userInput = "ezequiel.gonzalez@enroutesystems.com"
passInput = "-123quielo"

# setup
driver = s.driver

def login():


    driver.get(url)

    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, log1)))

    # login phase

    driver.find_element_by_css_selector(log1).click()

    #wait till change of page
    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, user)))
    driver.find_element_by_css_selector(user).send_keys(userInput)
    sleep(1)
    driver.find_element_by_css_selector(passwd).send_keys(passInput)
    sleep(1)
    driver.find_element_by_css_selector(log2).click()

    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, "#main-pane")))












