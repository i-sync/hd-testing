"""
Touring Demo(My19 Recommission) booking page checking.
"""

import unittest
import pytest
from driver.browser import *
from proj04_touringdemo.data.marketmatrix_utils import *
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage
from proj04_touringdemo.report.report import *
from proj04_touringdemo.data.locales import *
@pytest.mark.my19R
class TestTouringDemoCheckBookingBikePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser()
        cls.landingPage = LandingPage(cls.driver)
        cls.bookingPage = BookingPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_touringdemo_check_bike_list(self):
         """
         Touring Demo(My19 Recommission)
         :return:
         """
         self.landingPage.open()
         # get all of locales
         # locales = self.landingPage.get_all_locales()
         # get bike list from excel
         bike_list_matrix = get_bike_matrix()
         res = []
         for locale in FromLocales:
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
                self.bookingPage.logger.info(infomation)
                res.append(infomation)
             if len(res):
                 assert 1,locale+"\n bike list are incorrect"
         for locale in Special:
             # open locale booking page for en_AU
             self.bookingPage.url = "/{}".format(locale)
             self.bookingPage.url = self.bookingPage.url + "/booking"
             self.bookingPage.open()
             time.sleep(3)
             self.bookingPage.logger.warning(self.bookingPage.driver.url)
if __name__ == "__main__":
    unittest.main()