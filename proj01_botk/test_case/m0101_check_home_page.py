"""
Check BOTK 2019 Homepage
"""
import unittest
import pytest

from driver.browser import *
from proj01_botk.data.locales import *
from proj01_botk.data.marketmatrix_utils import *
from proj01_botk.page.home_page import HomePage

class TestBOTK2019CheckHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
        self.homepage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.apac
    def test_botk2019_check_social_link(self):
        """
        Botk 2019 Homepage check social link
        :return:
        """
        res = []
        #get social link matrix
        social_link_matrix = get_social_matrix()
        #self.homepage.logger.warning(social_link_matrix)

        for locale in APAC:
            # open locale homepage
            self.homepage.url = "/{}".format(locale)
            self.homepage.open()

            #get social link
            social_links = self.homepage.get_social_links(locale)
            if not sorted(social_links) == sorted(social_link_matrix[locale]):
                info = "locale: [{}] soical links is not equal.\r\npage social links: {}\r\nmatrix social links:{}".format(
                    locale, sorted(social_links), sorted(social_link_matrix[locale]))
                self.homepage.logger.warning(info)
                res.append(info)

        if len(res):
            assert 0, "Some locales social links are incorrect."
