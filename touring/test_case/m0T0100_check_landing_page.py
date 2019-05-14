"""
Touring each locale landing page checking.
"""

import unittest
from driver.browser import *
from touring.page.landing_page import LandingPage
from BeautifulReport import BeautifulReport
from touring.data.locales import *
import time,os

class TestCheckLandingPage(unittest.TestCase):
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

    # @unittest.skipUnless(os.environ["env"] == "live", "only check live site")
    @BeautifulReport.add_test_img(time.strftime("%Y%m%d-%H%M%S")+'_touring_landing_error_img')
    def test_check_landing_page(self):
        """
        Touring
        Check locale landing page
        """
        #check all of the locales
        for locale in All_Locales:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)
            self.assertIn(locale, self.driver.current_url)


if __name__ == "__main__":
    unittest.main()