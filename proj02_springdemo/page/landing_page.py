"""
Spring Demo Landing Page
"""
from selenium.webdriver.support.select import Select

from page.page import Page
from proj02_springdemo.data.urls import current_url
from proj02_springdemo.element.elements_define import ElementsDefine

class LandingPage(Page):
    """
    Spring Demo Landing Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/landing"
        #self.driver = driver
        #self.base_url = current_url()
        super(LandingPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()