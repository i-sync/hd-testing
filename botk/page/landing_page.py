"""
Touring Demo(My19 Recommission) Landing Page
"""
from page.page import Page
from botk.element.elements_define import ElementsDefine
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from botk.data.urls import current_url

class LandingPage(Page):
    """
    BOTK 2019 Landing Page
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
        self.country_options = self.find_elements(*self.element.landing_country_options)
        return [option.get_attribute("value") for option in self.country_options if option.get_attribute("value")]

    def chose_locale(self, locale):
        """
        chose country select locale
        :param locale:
        :return:
        """
        self.country_select = self.find_element(*self.element.landing_country_select)
        Select(self.country_select).select_by_value(locale)

    def click_continue_button(self):
        """
        click landing page continue button
        :return:
        """
        with self.wait_for_page_load(10):
            self.find_element(*self.element.landing_continue_button).click()