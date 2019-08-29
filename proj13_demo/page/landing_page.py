"""
MY20 DEMO Landing Page
"""
from page.page import Page
from proj13_demo.data.urls import current_url
from proj13_demo.element.elements_define import ElementsDefine


class LandingPage(Page):
    """
    MY20 DEMO Landing Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/landing"
        super(LandingPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()
