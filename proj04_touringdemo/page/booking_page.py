"""
Touring Demo(My19 Recommission) Home Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj04_touringdemo.data.urls import current_url
from proj04_touringdemo.element.elements_define import ElementsDefine
from proj04_touringdemo.data.form_data import FormContent

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
        return [li.get_attribute("data-code") for li in self.bike_list if li.get_attribute("data-code")]

    def get_map_list(self):
        """
        Get Map list on booking page
        :return:
        """
        self.map_list = self.find_elements(self.element.chooseDealerList)
        return [li.get_attribute("data-code") for li in self.map_list if li.get_attribute("data-code")]
    #
    # def choose_bookButton(self):
    #     """
    #     choose Book button on home page
    #     :return:
    #     """
    #     with self.wait_for_page_load(10):
    #         self.find_element(*self.element.choose_book_button).click()
    # def choose_firstBike(self):
    #     with self.wait_for_page_load(10):
    #          self.find_element(*self.element.firstBike).click()
    # def choose_DealerMap(self):
    #     """
    #     select a dealer Map on booking page
    #     :return:
    #     step:
    #     1. input a in dealer map
    #     2. choose first hint message
    #     3. choose first map by default(there is no code for this step because it will automation)
    #     """
    #     with self.wait_for_page_load(10):
    #         # 1. input a in dealer map
    #         self.find_element(*self.element.dealerMap).send_keys(FormContent["SearchTextField"])
    #     with self.wait_for_page_load(10):
    #         # 2. choose first hint message
    #         self.find_element(*self.element.chooseFirstDealer).click()
    #
    # def choose_RequestTestRideButton(self):
    #     """
    #       choose RequestTestRide button on Booking page
    #       :return:
    #     """
    #     with self.wait_for_page_load(10):
    #          self.find_element(*self.element.requestTestRideButton).click()
    #
    # def finish_form(self):
    #     """
    #     fill content on booking page
    #     :return:
    #     """
    #     with self.wait_for_page_load(10):
    #         self.choose_firstBike()
    #         self.choose_DealerMap()
    #         self.find_element(*self.element.chooseTitle).click()
    #         self.find_element(*self.element.chooseFirstTitle).click()