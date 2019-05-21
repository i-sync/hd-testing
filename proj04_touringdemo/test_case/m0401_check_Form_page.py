"""
Touring Demo(My19 Recommission) landing page checking.
"""

import time,os
import unittest
import pytest
from selenium.webdriver.common.keys import Keys
from driver.browser import *

from proj04_touringdemo.data.locales import *
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage

@pytest.mark.my19R
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
        self.bookingPage = BookingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_touringdemo_check_landing_page(self):
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
            self.bookingPage.click_element(self.bookingPage.element.choose_book_button)
            # choose first bike on home
            bike_list = self.bookingPage.get_bike_list()
            bike_list[0].click()
            # input map
            self.bookingPage.click_element(self.bookingPage.element.dealerMap)
            self.bookingPage.input_element_value(self.bookingPage.element.dealerMap, "OP")
            # choose first map
            self.bookingPage.key_Action(Keys.DOWN)
            self.bookingPage.key_Action(Keys.ENTER)
            self.bookingPage.key_Action(Keys.ENTER)
            # submit form when all forms are empty
            self.bookingPage.click_element(self.bookingPage.element.requestTestRideButton)
    def test_touringdemo_check_form_page(self):
         """
         Touring Demo(My19 Recommission)
         Auto submit booking form
         step:
         1. choose first bike on home
         2. submit form when form is empty
         3. assert the error message
         :return:
         """


if __name__ == "__main__":
    unittest.main()