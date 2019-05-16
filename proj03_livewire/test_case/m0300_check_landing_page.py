"""
Spring Demo each locale landing page checking.
"""

import time,os
import unittest
from driver.browser import *

from proj03_livewire.data.locales import *
from proj03_livewire.page.home_page import HomePage

class TestLivewireCheckHomePage(unittest.TestCase):
    """
    LiveWire Home page
    """
    def setUp(self):
        self.driver = firefox_browser()
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

    def test_livewire_check_home_page(self):
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