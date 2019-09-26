"""
MY20 DEMO landing checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj13_demo.data.locales import *
from proj13_demo.page.home_page import HomePage


@pytest.mark.live_checker
class TestMY20CheckLandingPage(unittest.TestCase):
    """
    MY20 DEMO Landing page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.homePage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_my20_check_landing_page(self):
        """
        13. my20 Check locale home page
        """
        pass


if __name__ == "__main__":
    unittest.main()
