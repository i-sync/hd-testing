"""
Touring Demo Landing Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj05_touring.data.urls import current_url
from proj05_touring.element.elements_define import ElementsDefine

class LandingPage(Page):
    """
    Touring Landing Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/landing"
        super(LandingPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

    def get_all_locales(self):
        """
        Get all locales
        :return:
        """
        self.country_options = self.find_elements(self.element.landing_country_options)
        return [option.get_attribute("value") for option in self.country_options if option.get_attribute("value")]