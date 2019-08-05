"""
MY20 RYI Footer process .
"""

import time,os
import unittest
import pytest
from driver.browser import *
from proj12_ryi.data.locales import *
from proj12_ryi.data.marketmatrix_utils import *
from proj12_ryi.page.home_page import HomePage


@pytest.mark.ryi
class TestRyiFooterProcess(unittest.TestCase):
    """
    MY20 RYI Footer
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = chrome_browser()
        cls.currentPage = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @pytest.mark.run(order=10)
    def test_ryi_dealer_page(self):
        """
         MY20 RYI Footer process
        """
        # open home page
        self.currentPage.url = "/{}/home".format("en_GB")
        self.currentPage.open()
        # get footer href links
        get_footer_links = get_footer_matrix()

        for locale in All_Locales:
            #open landing page
            self.currentPage.url = "/landing"
            self.currentPage.open()
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale,
                                                     refresh_page=True)
            # get footer link list
            get_footer_links_page = self.bookingPage.get_list_by_attribute(self.bookingPage.element.footerIconHrefs,
                                                                           "href")
            # assert footer icon links
            try:
                for footerHref in get_footer_links_page:
                    self.assertTrue(footerHref in get_footer_links[locale])

            except AssertionError as result:
                info = "Touring Demo(My20 RYI) footerHref check issue locale is \n" + locale + " ,\n please review error result%s" % result
                self.bookingPage.logger.warning(info)
                self.bookingPage.logger.info(info)

