"""
Touring Demo(My19 Recommission) Home Page
"""

from page.page import Page
from proj04_touringdemo.data.urls import current_url
from proj04_touringdemo.element.elements_define import ElementsDefine

class BookingPage(Page):
    """
    Touring Demo(My19 Recommission) Home Page
    For Form page test
    """

    def __init__(self,driver):
        """
        :param driver:
        """
        # super这句是必须的，用于构造父类Page,且Page需要参数
        super(BookingPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

    def get_list_by_attribute(self,loc,attributeValue):
        """
        Get booking page error message list
        :return:
        """
        self.list = self.find_elements(loc)
        return [li.get_attribute(attributeValue) for li in self.list if li.get_attribute(attributeValue)]

    def get_list(self,loc):
        """
        Get Booking page bike list
        :return:
        """
        bike_list = self.find_elements(loc)
        return bike_list
