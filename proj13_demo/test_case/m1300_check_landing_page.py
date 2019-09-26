"""
MY20 DEMO landing checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj13_demo.data.marketmatrix_utils import *
from proj13_demo.page.landing_page import LandingPage


@pytest.mark.live_checker
class TestMY20CheckLandingPage(unittest.TestCase):
    """
    MY20 DEMO Landing page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.landingPage = LandingPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_my20_check_landing_page(self):
        """
        13. my20 Check locale home page
        """
        # get all locales from matrix
        locales = get_all_locale()

        # check all locale
        for locale in locales:
            # open landing page
            self.landingPage.open()
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)

            # click submit button
            self.landingPage.click_element(self.landingPage.element.landing_go_button, refresh_page=True)

            # check home page title
            page_title = "Harley-Davidson® | Ride Free"
            self.assertEqual(page_title, self.driver.title,
                             "My20 Demo Home page title is incorrect: [{}]".format(self.driver.title))


if __name__ == "__main__":
    unittest.main()
