"""
Softail landing page checking.
"""

import time,os
import unittest
from driver.browser import *
from BeautifulReport import BeautifulReport

from proj06_softail.data.locales import *
from proj06_softail.page.landing_page import LandingPage

class TestSoftailCheckLandingPage(unittest.TestCase):
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

    @BeautifulReport.add_test_img(time.strftime("%Y%m%d-%H%M%S")+'_softail_landing_error_img')
    def test_softail_check_landing_page(self):
        """
        Softail
         the locales are closing now on live
        """
        #check all of the locales()
        for locale in All_Locales:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)
            part_url = "harley-davidson\.com\/.*\/{}\/index\.html".format(locale[:2])
            self.assertIn(self.driver.current_url,part_url)

if __name__ == "__main__":
    unittest.main()