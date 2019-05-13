"""
The Browser Object
"""
from selenium import webdriver

def chrome_browser(headless = None):
    option = webdriver.ChromeOptions()
    option.headless = headless
    driver = webdriver.Chrome(options=option)
    #driver.maximize_window()
    return driver

def firefox_browser(headless = None):
    option = webdriver.FirefoxOptions()
    option.headless = headless
    driver = webdriver.Firefox(options=option)
    #driver.maximize_window()
    return driver
