"""
Touring Demo(My19 Recommission) landing page checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj04_touringdemo.data.locales import *
from proj04_touringdemo.page.landing_page import LandingPage

@pytest.mark.live_checker
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
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

    def test_touringdemo_check_landing_page(self):
        """
        Touring Demo(My19 Recommission)
        Check landing page
        """
        #check online locale
        for locale in All_Locales + Special:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)

            self.assertIn(locale, self.driver.current_url)

if __name__ == "__main__":
    unittest.main()