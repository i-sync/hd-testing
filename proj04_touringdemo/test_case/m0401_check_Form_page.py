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

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(BeautifulReport.img_path), img_name))

    def test_touringdemo_check_landing_page(self):
        """
        Touring Demo(My19 Recommission)
        step:
        1.select one locale on landing page
        2.click book a ride test button
        """
        #check online locale
        for locale in FromLocale:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)
            #assert landing page URL
            self.assertIn(locale, self.driver.current_url)
            # select book button on home page
            self.bookingPage.choose_bookButton()
            # submit form when form is empty
            self.bookingPage.choose_RequestTestRideButton()
    def test_touringdemo_check_form_page(self):
         """
         Touring Demo(My19 Recommission)
         Auto submit booking form
         step:
         1. choose first bike on home
         2. finished form
         3. submit form
         :return:
         """


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