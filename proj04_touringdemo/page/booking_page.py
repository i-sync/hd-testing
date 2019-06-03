"""
Touring Demo(My19 Recommission) Home Page
"""
import re
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
        self.url="/{}"
        # super这句是必须的，用于构造父类Page,且Page需要参数(python3 不需要参数，但是python 2.7需要，这里加入的目的是为了兼容)
        super(BookingPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()
        self.logger

    def get_list_by_attribute(self,loc,attributeValue):
        """
        Get booking page error message list
        :return:
        """
        self.list = self.find_elements(loc)
        return [li.get_attribute(attributeValue) for li in self.list if li.get_attribute(attributeValue)]

    def get_list(self,loc):
        """
        Get Booking page list
        eg:bike list
        :return:
        """
        get_list = self.find_elements(loc)
        return get_list

    def get_text_list(self,loc):
        """
        Get Booking page text list
        eg:bike name list
        :return:
        """
        L=[]
        get_list = self.find_elements(loc)
        for text_element in get_list:
            value = text_element.text
            #remove 特殊符号
            string = re.sub('[./~!@#$%^&*()-+®]+','', value)
            L.append(string)
        return L