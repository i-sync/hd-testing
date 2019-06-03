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
class TestTouringDemoCheckBookingFormPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser()
        cls.landingPage = LandingPage(cls.driver)
        cls.bookingPage = BookingPage(cls.driver)
        cls.log = Log(r"../../report/output.txt")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_touringdemo_check_booking_from_page(self):
        """
        Touring Demo(My19 Recommission)
        step:
        1.select one locale on landing page
        2.click book a ride test button
        3. choose first bike on home
        4. finished form
        5. submit form
        """
        # get all of locales
        locales = self.landingPage.get_all_locales()
        #check online locale
        for locale in locales:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale,refresh_page=True)
            # select book button on home page
            self.bookingPage.click_element(self.bookingPage.element.choose_book_button,refresh_page=True)
            # choose first bike on home
            time.sleep(3)
            bike_list = self.bookingPage.get_list(self.bookingPage.element.bike_value_list)
            bike_list[0].click()
            # input map
            self.bookingPage.click_element(self.bookingPage.element.dealerMap)
            self.bookingPage.input_element_value(self.bookingPage.element.dealerMap, "OP")
            # choose first map
            time.sleep(3)
            self.bookingPage.key_Action(Keys.DOWN)
            time.sleep(0.5)
            self.bookingPage.key_Action(Keys.ENTER)
            time.sleep(0.5)
            self.bookingPage.key_Action(Keys.ENTER)
            time.sleep(3)
            # submit form when all forms are empty
            self.bookingPage.click_element(self.bookingPage.element.requestTestRideButton)

        #check error message that is not --
        error_message_list = self.bookingPage.get_list_by_attribute(self.bookingPage.element.errorMessage,"value")
        errorLenght=len(error_message_list)
        #check error message lenght
        self.assertTrue(10,errorLenght)
        for error in error_message_list:
            self.assertNotIn(error, "--")
        error_message_div_list=self.bookingPage.get_list_by_attribute(self.bookingPage.element.errorMessage_checkbox,"value")
        errorDivLenght = len(error_message_div_list)
        self.assertTrue(2, errorDivLenght)
        for error in error_message_div_list:
            self.assertNotIn(error, "--")

if __name__ == "__main__":
    unittest.main()