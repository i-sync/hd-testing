"""
Check Spring Demo Social Link URL
"""
import unittest
import pytest

from driver.browser import *
from proj02_springdemo.data.locales import *
from proj02_springdemo.data.marketmatrix_utils import *
from proj02_springdemo.page.home_page import HomePage

class TestSpringDemoCheckHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
        self.homepage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.debug
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
            break

    def test_springdemo_check_bikelist(self):
        """
        Spring Demo Homepage check bike list
        :return:
        """

        #get bike list
        bike_list_matrix = get_bike_matrix()

        res = []
        for locale in Online:
            # open locale homepage
            self.homepage.url = "/{}".format(locale)
            self.homepage.open()

            #get bike list
            bike_list = self.homepage.get_bike_list(locale)
            if not sorted(bike_list) == sorted(bike_list_matrix[locale]):
                info = "locale: [{}] bike list is not equal.\r\npage bike list: {}\r\nmatrix bike list:{}".format(locale, sorted(bike_list), sorted(bike_list_matrix[locale]))
                self.homepage.logger.warning(info)
                res.append(info)

        if len(res):
            assert 0, "Some locales bike list are incorrect."