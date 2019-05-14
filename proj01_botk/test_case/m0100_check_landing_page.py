"""
BOTK 2019 landing page checking.
"""

import time,os
import unittest
from driver.browser import *
from BeautifulReport import BeautifulReport
from proj01_botk.page.landing_page import LandingPage

class TestBotkCheckLandingPage(unittest.TestCase):
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

    @BeautifulReport.add_test_img(time.strftime("%Y%m%d-%H%M%S")+'_botk_landing_error_img')
    def test_botk_check_landing_page(self):
        """
        BOTK 2019
        Check landing page
        """

        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()

        # check locale
        for locale in locales:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)
            #button click
            self.landingPage.click_continue_button()
            #check
            self.assertIn(locale, self.driver.current_url)

if __name__ == "__main__":
    unittest.main()