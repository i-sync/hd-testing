"""
Please ignore this file
Just for demo.
"""

import unittest
from driver.browser import *
from springdemo.page.LandingPage import LandingPage

class Test_m0001(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
        self.landingPage = LandingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_case1(self):
        #open landing page
        self.landingPage.open();
        #country select en_GB
        self.landingPage.chose_locale("en_CA")
        #click_button
        self.landingPage.click_continue_button()
        self.assertIn("en_CA", self.driver.current_url)
if __name__ == "__main__":
    unittest.main()