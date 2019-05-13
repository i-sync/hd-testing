"""
The Browser Object
"""
from selenium import webdriver

def chrome_browser(headless = None):
    option = webdriver.ChromeOptions()
    option.headless = headless
    driver = webdriver.Chrome(chrome_options=option)
    #driver.maximize_window()
    return driver

def firefox_browser(headless = None):
    option = webdriver.FirefoxOptions()
    option.headless = headless
    driver = webdriver.Firefox(firefox_options=option)
    #driver.maximize_window()
    return driver
