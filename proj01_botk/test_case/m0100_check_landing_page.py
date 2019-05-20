"""
BOTK 2019 landing page checking.
"""

import time,os
import unittest
import pytest

from driver.browser import *
from proj01_botk.page.landing_page import LandingPage

@pytest.mark.live_checker
class TestBotkCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_botk_check_landing_page(self):
        """
        01. BOTK 2019 Check landing page
        """

        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()

        # check locale
        for locale in locales:
            #open landing page
            self.landingPage.open()
            #country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)
            #button click
            self.landingPage.click_element(self.landingPage.element.landing_continue_button, refresh_page=True)
            #check
            self.assertIn(locale, self.driver.current_url)

if __name__ == "__main__":
    unittest.main()