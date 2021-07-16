from selenium import webdriver

# setup
prefs = {"profile.default_content_setting_values.notifications": 2}
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome("chromedriver.exe", options=options)

driver.maximize_window()

