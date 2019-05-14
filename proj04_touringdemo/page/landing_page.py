"""
Touring Demo(My19 Recommission) Landing Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj04_touringdemo.data.urls import current_url
from proj04_touringdemo.element.elements_define import ElementsDefine

class LandingPage(Page):
    """
    Touring Demo(My19 Recommission) Landing Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/landing"
        super(LandingPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

    def chose_locale(self, locale):
        """
        chose country select locale
        :param locale:
        :return:
        """
        self.country_select = self.find_element(*self.element.landing_country_select)
        with self.wait_for_page_load(10):
            Select(self.country_select).select_by_value(locale)
