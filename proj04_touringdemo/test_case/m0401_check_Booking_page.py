"""
Touring Demo(My19 Recommission) landing page checking.
"""

import time,os
import unittest
import pytest
import time
from selenium.webdriver.common.keys import Keys
from driver.browser import *

from proj04_touringdemo.data.locales import *
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage

@pytest.mark.my19R
class TestTouringDemoCheckBookingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
        self.bookingPage = BookingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_touringdemo_check_booking_page(self):
        """
        Touring Demo(My19 Recommission)
        step:
        1.select one locale on landing page
        2.click book a ride test button
        3. choose first bike on home
        4. finished form
        5. submit form
        """
        #check online locale
        for locale in FromLocale:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)
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
        self.assert_(10,errorLenght)
        for error in error_message_list:
            self.assertNotIn(error, "--")
        error_message_div_list=self.bookingPage.get_list_by_attribute(self.bookingPage.element.errorMessage_checkbox,"value")
        errorDivLenght = len(error_message_div_list)
        self.assert_(2, errorDivLenght)
        for error in error_message_div_list:
            self.assertNotIn(error, "--")
    def test_touringdemo_check_bike_list(self):
         """
         Touring Demo(My19 Recommission)
         :return:
         """
         self.get_list_by_attribute=self.bookingPage.get_list_by_attribute(self.bookingPage.element.bike_value_list,"value")
         # assert bike list value



if __name__ == "__main__":
    unittest.main()