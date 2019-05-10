"""
Spring Demo Landing Page
"""
from page.Page import Page
from springdemo.element.ElementsDefine import ElementsDefine
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from springdemo.data.urls import current_url

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
        self.driver = driver
        self.base_url = current_url()
        #super(Page,self).__init__(driver, self.base_url)
        self.elemnt = ElementsDefine()

    def chose_locale(self, locale):
        """
        chose country select locale
        :param locale:
        :return:
        """
        self.country_select = self.find_element(*self.elemnt.landing_country_select)
        Select(self.country_select).select_by_value(locale)

    def click_continue_button(self):
        """
        click landing page continue button
        :return:
        """
        self.find_element(*self.elemnt.landing_continue_button).click()