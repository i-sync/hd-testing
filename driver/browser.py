"""
The Browser Object
"""
import os
from selenium import webdriver

headless = eval(os.environ["headless"]) if "headless" in os.environ else None
def chrome_browser(headless = headless):
    option = webdriver.ChromeOptions()
    option.headless = headless
    driver = webdriver.Chrome(options=option)
    #driver.maximize_window()
    return driver

def firefox_browser(headless = headless):
    option = webdriver.FirefoxOptions()
    option.headless = headless
    driver = webdriver.Firefox(options=option)
    #driver.maximize_window()
    return driver
