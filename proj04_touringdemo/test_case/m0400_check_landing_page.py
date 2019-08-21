"""
Touring Demo(My19 Recommission) landing page checking.
"""

import unittest
import pytest

from driver.browser import *

from proj04_touringdemo.page.landing_page import LandingPage

@pytest.mark.live_checker
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser()
        self.landingPage = LandingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_touringdemo_check_landing_page(self):
        """
        04. Touring Demo(My19 Recommission) Check landing page
        """
        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()

        #check online locale
        for locale in locales:
            # open landing page
            self.landingPage.open()
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale, refresh_page=True)
            # check
            # self.assertIn(locale, self.driver.current_url)
            part_url = "harley-davidson\.com\/.*\/{}\/index\.html".format(locale[:2])
            self.assertRegex(self.driver.current_url, part_url)
if __name__ == "__main__":
    unittest.main()