"""
LiveWire Home Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj03_livewire.data.urls import current_url
from proj03_livewire.element.elements_define import ElementsDefine

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

