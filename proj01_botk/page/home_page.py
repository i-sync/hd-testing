"""
BOTK 2019 Home Page
"""
from selenium.webdriver.support.select import Select

from page.page import Page
from proj01_botk.data.urls import current_url
from proj01_botk.element.elements_define import ElementsDefine

class HomePage(Page):
    """
    BOTK 2019 Home Page
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

    def get_social_links(self):
        """
        Get HomePage Social Link
        :return:
        """
        social_links = self.find_elements(self.element.homepage_social_link)
        return [a.get_attribute("href") for a in social_links if a.get_attribute("href")]