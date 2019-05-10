"""
The Browser Object
"""
from selenium import webdriver

def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def firefox_browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver
