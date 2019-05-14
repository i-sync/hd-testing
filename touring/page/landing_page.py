"""
Touring Demo Landing Page
"""
from page.page import Page
from touring.element.elements_define import ElementsDefine
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from touring.data.urls import current_url

class LandingPage(Page):
    """
    touring Landing Page
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

    def chose_locale(self, locale):
        """
        chose country select locale
        :param locale:
        :return:
        """
        self.country_select = self.find_element(*self.element.landing_country_select)
        Select(self.country_select).select_by_value(locale)