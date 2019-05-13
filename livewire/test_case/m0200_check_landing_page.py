"""
Spring Demo each locale landing page checking.
"""

import unittest
from driver.browser import *
from BeautifulReport import BeautifulReport
from livewire.data.locales import *
from livewire.page.home_page import HomePage
import time,os

class TestCheckHomePage(unittest.TestCase):
    """
    LiveWire Home page
    """
    def setUp(self):
        self.driver = chrome_browser()
        self.homePage = HomePage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(BeautifulReport.img_path), img_name))

    #@unittest.skipUnless(os.environ["env"] == "live")
    @BeautifulReport.add_test_img(time.strftime("%Y%m%d-%H%M%S")+'_livewire_landing_error_img')
    def test_check_home_page(self):
        """
        LiveWire
        Check locale home page
        """
        #check all locale
        for locale in All_Locales:
            #open home page
            self.homePage.url = "/{}".format(locale)
            self.homePage.open();
            #check url
            self.assertIn(locale, self.driver.current_url)


if __name__ == "__main__":
    unittest.main()