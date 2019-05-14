"""
Greatestrides Home Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj11_greatestrides.data.urls import current_url
from proj11_greatestrides.element.elements_define import ElementsDefine

class HomePage(Page):
    """
    Greatestrides Home Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/"
        #self.driver = driver
        #self.base_url = current_url()
        super(HomePage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

