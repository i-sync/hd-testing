"""
Touring Demo(My19 Recommission) landing page checking.
"""

import time,os
import unittest
import pytest
import time
from driver.browser import *
from proj04_touringdemo.report.demo1 import logger
from selenium.webdriver.common.keys import Keys
from proj04_touringdemo.data.locales import *
from proj04_touringdemo.data.marketmatrix_utils import *
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage
from proj04_touringdemo.report.report import *
@pytest.mark.my19R
class TestTouringDemoCheckBookingBikePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser(headless=False)
        cls.landingPage = LandingPage(cls.driver)
        cls.bookingPage = BookingPage(cls.driver)
        cls.log = Log(r"../../report/output.txt")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_touringdemo_check_bike_list(self):
         """
         Touring Demo(My19 Recommission)
         :return:
         """
         # get all of locales
         locales = self.landingPage.get_all_locales()
         # get bike list from excel
         bike_list_matrix = get_bike_matrix()
         res = []
         for locale in locales:
             # open locale booking page
             self.bookingPage.url = "/{}".format(locale)
             self.bookingPage.url = self.bookingPage.url +"/booking"
             self.bookingPage.open()
             time.sleep(3)
             #get bike list on this locale
             get_bike_list=self.bookingPage.get_text_list(self.bookingPage.element.bike_value_list)
             #assert bike list value
             if not sorted(get_bike_list)==sorted(bike_list_matrix[locale]):
                infomation="locale: [{}] bike list is not equal.\r\npage bike list: {}\r\nmatrix bike list:{}".format(locale,sorted(get_bike_list),sorted(bike_list_matrix[locale]))
                self.bookingPage.logger.warning(infomation)
                res.append(infomation)
             if len(res):
                 assert 1,locale+"\n bike list are incorrect"

if __name__ == "__main__":
    unittest.main()