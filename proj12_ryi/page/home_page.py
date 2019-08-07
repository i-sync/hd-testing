"""
MY20 RYI Home Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj12_ryi.data.urls import current_url
from proj12_ryi.element.elements_define import ElementsDefine

class HomePage(Page):
    """
    MY20 RYI Home Page
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

    def get_social_links(self):
        """
        Get HomePage Social Link
        :return:
        """
        social_links = self.find_elements(self.element.hoempage_social_link)
        return [a.get_attribute("href") for a in social_links if a.get_attribute("href")]