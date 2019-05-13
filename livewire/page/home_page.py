"""
LiveWire Home Page
"""
from page.page import Page
from livewire.element.elements_define import ElementsDefine
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from livewire.data.urls import current_url

class HomePage(Page):
    """
    LiveWire Home Page
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

