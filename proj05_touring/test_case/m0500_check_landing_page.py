"""
Touring each locale landing page checking.
"""

import time,os
import unittest
from driver.browser import *

from proj05_touring.data.locales import *
from proj05_touring.page.landing_page import LandingPage

class TestTouringCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = chrome_browser(headless=False)
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

    def test_touring_check_landing_page(self):
        """
        Touring
        Check locale landing page
        the locales are closing now on live
        """
        #check all of the locales()
        for locale in All_Locales:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)
        #     self.assertIn(locale, self.driver.current_url)
        # #check all of the closing locales
        # for locale in Closing:
        #     #open landing page
        #     self.landingPage.open();
        #     #coutry select
        #     self.landingPage.chose_locale(locale)
            part_url = "harley-davidson\.com\/.*\/{}\/index\.html".format(locale[:2])
            self.assertIn(self.driver.current_url,part_url)

if __name__ == "__main__":
    unittest.main()