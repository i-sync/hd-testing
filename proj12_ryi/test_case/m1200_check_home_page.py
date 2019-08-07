"""
MY20 RYI Home checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj12_ryi.data.locales import *
from proj12_ryi.data.marketmatrix_utils import *
from proj12_ryi.page.home_page import HomePage

@pytest.mark.live_checker
class TestRYICheckHomePage(unittest.TestCase):
    """
    MY20 RYI Home page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.homePage = HomePage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_ryi_check_home_page(self):
        """
        12. MY20 RYI Home page
        """
        # check all locale
        for locale in All_Locales:
            # open home page
            self.homePage.url = "/{}".format(locale)
            self.homePage.open()
            # check url
            self.assertIn(locale, self.driver.current_url)

    def test_ryi_check_social_link(self):
        """
        MY20 RYI Homepage check social link
        :return:
        """
        res = []
        # get social link matrix
        social_link_matrix = get_social_matrix()

        for locale in All_Locales:
            # open locale homepage
            self.homepage.url = "/{}/home".format(locale)
            self.homepage.open()

            # get social link
            social_links = self.homepage.get_social_links()
            if not sorted(social_links) == sorted(social_link_matrix[locale]):
                res.append(f"locale: [{locale}] social links is not equal.\r\npage social links: {sorted(social_links)}\
                    \r\nmatrix social links:{sorted(social_link_matrix[locale])}")
                self.homepage.logger.warning(res[-1])

        if len(res):
            assert 0, "Some locales social links are incorrect."


if __name__ == "__main__":
    unittest.main()
