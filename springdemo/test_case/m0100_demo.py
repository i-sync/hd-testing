"""
Please ignore this file
Just for demo.
"""

import unittest
from driver.browser import *
from springdemo.page.landing_page import LandingPage
from BeautifulReport import BeautifulReport
import time,os

class TestCaseDemo(unittest.TestCase):
    """
    Demo Test class
    """
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

    @unittest.skip("This is demo test case, ignore it.")
    @BeautifulReport.add_test_img(time.strftime("%Y%m%d-%H%M%S")+'_test_case1_error_img')
    def test_case1(self):
        """
        demo test case1
        :return:
        """
        #open landing page
        self.landingPage.open();
        #country select en_GB
        self.landingPage.chose_locale("en_GB")
        #click_button
        self.landingPage.click_continue_button()
        self.assertIn("en_GB", self.driver.current_url)
if __name__ == "__main__":
    unittest.main()