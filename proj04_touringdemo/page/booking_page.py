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

    def get_message_list(self,loc):
        """
        Get booking page error message list
        :return:
        """
        self.error_message_list = self.find_elements(loc)
        return [li.get_attribute("value") for li in self.error_message_list if li.get_attribute("value")]

    def get_bike_list(self):
        """
        Get Booking page bike list
        :return:
        """
        bike_list = self.find_elements(self.element.bike_list)
        return bike_list
