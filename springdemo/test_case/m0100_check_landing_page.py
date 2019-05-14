"""
Spring Demo each locale landing page checking.
"""

import unittest
from driver.browser import *
from springdemo.page.landing_page import LandingPage
from BeautifulReport import BeautifulReport
from springdemo.data.locales import *
import time,os

class TestCheckLandingPage(unittest.TestCase):
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

    @unittest.skipUnless(os.environ["env"] == "live", "only check live site")
    @BeautifulReport.add_test_img(time.strftime("%Y%m%d-%H%M%S")+'_springdemo_landing_error_img')
    def test_check_landing_page(self):
        """
        Spring Demo
        Check locale landing page
        """
        #check online locale
        for locale in Online:
            #open landing page
            self.landingPage.open();
            #country select
            self.landingPage.chose_locale(locale)
            #click_button
            self.landingPage.click_continue_button()
            self.assertIn(locale, self.driver.current_url)

        #check closing locale
        for locale in Closing:
            #open landing page
            self.landingPage.open()
            #country select
            self.landingPage.chose_locale(locale)
            #click_button
            self.landingPage.click_continue_button()
            part_url = "harley-davidson\.com\/.*\/{}\/index\.html".format(locale[:2])
            self.assertRegex(self.driver.current_url, part_url)
if __name__ == "__main__":
    unittest.main()