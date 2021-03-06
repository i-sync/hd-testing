"""
Spring Demo each locale landing page checking.
"""

import time
import unittest
import pytest
from driver.browser import *

from proj02_springdemo.data.locales import *
from proj02_springdemo.page.landing_page import LandingPage

@pytest.mark.live_checker
class TestSpringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_springdemo_check_landing_page(self):
        """
        02. Spring Demo Check locale landing page
        """
        #check online locale
        for locale in Online:
            #open landing page
            self.landingPage.open()
            #country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)
            #click_button
            self.landingPage.click_element(self.landingPage.element.landing_continue_button, refresh_page=True)
            self.assertIn(locale, self.driver.current_url)

        #check closing locale
        for locale in Closing:
            #open landing page
            self.landingPage.open()
            #country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)
            #click_button
            self.landingPage.click_element(self.landingPage.element.landing_continue_button, refresh_page=True)
            part_url = "harley-davidson\.com\/.*\/{}\/index\.html".format(locale[:2])
            self.assertRegex(self.driver.current_url, part_url)
if __name__ == "__main__":
    unittest.main()