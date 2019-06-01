"""
TRBF landing page checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj07_trbf.page.landing_page import LandingPage

@pytest.mark.live_checker
class TestTrbfCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
        self.landingPage = LandingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(BeautifulReport.img_path), img_name))

    def test_trbf_check_landing_page(self):
        """
        07. TRBF Check landing page
        """

        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()

        # check locale
        for locale in locales:
            #open landing page
            self.landingPage.open()
            #country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale, refresh_page=True)
            #check
            self.assertIn(locale, self.driver.current_url)

if __name__ == "__main__":
    unittest.main()