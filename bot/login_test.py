from selenium import webdriver
import pytest

import bot.objects as o

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as ex

from time import sleep

url = o.url
log1 = o.loginMain
user = o.username
passwd = o.password
log2 = o.loginSecond
userInput = o.userInput
passInput = o.passInput

@pytest.fixture()
def setup_driver():
    return webdriver.Chrome()


def test_url(setup_driver):
    driver = setup_driver
    expected_url = "https://www.bigtime.net/"
    driver.get(url)
    actual_url = driver.current_url

    assert expected_url == actual_url, "Url's are not the same"

def test_login_successful(setup_driver):
    driver = setup_driver
    driver.get(url)

    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, log1)))

    # login phase

    driver.find_element_by_css_selector(log1).click()

    # wait till change of page
    wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, user)))
    driver.find_element_by_css_selector(user).send_keys(userInput)
    sleep(1)
    driver.find_element_by_css_selector(passwd).send_keys(passInput)
    sleep(1)
    driver.find_element_by_css_selector(log2).click()

    expected = wait(driver, 5).until(ex.presence_of_element_located((By.CSS_SELECTOR, "#main-pane")))
    actual = driver.find_element_by_css_selector("#main-pane")

    assert expected == actual, "Login not successful"
