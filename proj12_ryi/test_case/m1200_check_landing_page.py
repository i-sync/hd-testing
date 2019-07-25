"""
MY20 RYI Landing checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj12_ryi.data.locales import *
from proj12_ryi.page.home_page import HomePage

@pytest.mark.live_checker
class TestRYICheckHomePage(unittest.TestCase):
    """
    MY20 RYI Landing page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.homePage = HomePage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_ryi_check_home_page(self):
        """
        12. MY20 RYI Landing page
        """
        #check all locale
        for locale in All_Locales:
            #open home page
            self.homePage.url = "/{}".format(locale)
            self.homePage.open()
            #check url
            self.assertIn(locale, self.driver.current_url)


if __name__ == "__main__":
    unittest.main()