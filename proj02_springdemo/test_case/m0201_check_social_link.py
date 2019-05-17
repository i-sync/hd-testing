"""
Check Spring Demo Social Link URL
"""

import unittest
import pytest

from driver.browser import *
from proj02_springdemo.data.locales import *
from proj02_springdemo.data.marketmatrix_utils import *
from proj02_springdemo.page.home_page import HomePage

class TestSpringDemoCheckSocialLink(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.homepage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_springdemo_check_social_link(self):
        """
        Spring Demo Homepage check social link
        :return:
        """

        #get social link matrix
        social_link_matrix = get_social_matrix()

        for locale in Online:
            # open locale homepage
            self.homepage.url = "/{}".format(locale)
            self.homepage.open()

            #get social link
            social_links = self.homepage.get_social_links(locale)
            for sl in social_links:
                self.assertTrue(sl in social_link_matrix[locale])