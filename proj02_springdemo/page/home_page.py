"""
Spring Demo Home Page
"""
from selenium.webdriver.support.select import Select

from page.page import Page
from proj02_springdemo.data.urls import current_url
from proj02_springdemo.element.elements_define import ElementsDefine

class HomePage(Page):
    """
    Spring Demo Landing Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/{}"
        #self.driver = driver
        #self.base_url = current_url()
        super(HomePage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

    def get_social_links(self, locale):
        """
        Get HomePage Social Link
        :param locale:
        :return:
        """
        self.social_links = self.find_elements(*self.element.homepage_social_link)
        return [a.get_attribute("href") for a in self.social_links if a.get_attribute("href")]

    def get_bike_list(self, locale):
        """
        Get HomePage Bike List
        :param locale:
        :return:
        """
        self.bike_list = self.find_elements(*self.element.homepage_bike_list)
        return [li.get_attribute("data-code") for li in self.bike_list if li.get_attribute("data-code")]