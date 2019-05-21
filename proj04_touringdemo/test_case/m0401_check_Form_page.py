"""
Touring Demo(My19 Recommission) landing page checking.
"""

import time,os
import unittest
import pytest

from driver.browser import *

from proj04_touringdemo.data.locales import *
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage

@pytest.mark.live_checker
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
            self.bookingPage.click_element(self.bookingPage.element.choose_book_button,refresh_page=True)
            # select text on bike top
            self.bookingPage.click_element(self.bookingPage.element.text_on_bike,refresh_page=True)
            # self.bookingPage.click_element(self.bookingPage.element.find_bikes,refresh_page=True)
            # choose first bike on home
        # with self.wait_for_page_load(30):
            bike_list = self.bookingPage.get_bike_list()
            bike_list = self.bookingPage.find_element_refresh_page(self.bookingPage.get_bike_list(),refresh_page=True)
            print(bike_list)
            self.bookingPage.click_element(self)

            bike_list[0].click()
            # choose first map
            map_list = self.bookingPage.get_map_list()
            map_list[0].click()
            # submit form when all forms are empty
            self.bookingPage.click_element(self.bookingPage.element.requestTestRideButton,refresh_page=True)









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