"""
MY20 RYI Landing page checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj12_ryi.page.landing_page import LandingPage

#@pytest.mark.live_checker
class TestRYICheckLandingPage(unittest.TestCase):
    """
    MY20 RYI Landing page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.landingPage = LandingPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_ryi_check_landing_page(self):
        """
        MY20 RYI Landing page check
        :return:
        """
        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()

        # check all locale
        for locale in locales:
            # open landing page
            self.landingPage.open()
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)

            # click submit button
            self.landingPage.click_element(self.landingPage.element.landing_go_button, refresh_page=True)

            # check home page title
            page_title = "Harley-Davidson® | Low Rider® S RYI - Register your interest"
            self.assertEqual(page_title, self.driver.title,
                             "RYI Home page title is incorrect: [{}]".format(self.driver.title))


if __name__ == "__main__":
    unittest.main()
