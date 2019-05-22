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
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
        self.bookingPage = BookingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_links(self):
        """
        Touring Demo(My19 Recommission)
        check href links for footer
        :return:
        """
        get_href_list=self.bookingPage.get_list_by_attribute(self.bookingPage.element.footerHrefs,"href")
        print(get_href_list)


if __name__ == "__main__":
    unittest.main()