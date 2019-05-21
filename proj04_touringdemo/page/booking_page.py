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

    def get_bike_list_locale(self,locale):
        """
        Get Home page bike list
        :param locale:
        :return:
        """
        self.bike_list = self.find_elements(self.element.bike_list)
        return [li.get_attribute("data-code") for li in self.bike_list if li.get_attribute("data-code")]

    def get_bike_list(self):
        """
        Get Booking page bike list
        :param locale:
        :return:
        """
        self.bike_list = self.find_elements(self.element.bike_list)
        return self.bike_list

    def get_map_list(self):
        """
        Get Map list on booking page
        :return:
        """
        self.map_list = self.find_elements(self.element.chooseDealerList)
        return self.map_list