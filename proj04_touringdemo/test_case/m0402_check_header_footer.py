"""
Touring Demo(My19 Recommission) landing page checking.
"""

import unittest
import pytest
from driver.browser import *

from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage
from proj04_touringdemo.data.marketmatrix_utils import *
@pytest.mark.my19R
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
        self.bookingPage = BookingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_links(self):
        """
        Touring Demo(My19 Recommission)
        check href links for footer&header
        :return:
        """
        get_footer_list = get_social_footer_matrix()
        get_menu_links_list = get_menu_links_matrix()
        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()
        # check online locale
        for locale in locales:
            # open landing page
            self.landingPage.open()
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale)
            # get footer link list
            get_footer_links_page = self.bookingPage.get_list_by_attribute(self.bookingPage.element.footerIconHrefs,"href")
            # assert footer icon links
            for footerHref in get_footer_links_page:
                self.assertTrue(footerHref in get_footer_list[locale])
            # get menu link list
            self.bookingPage.click_element(self.bookingPage.element.menuIcon)
            get_menu_links_page = self.bookingPage.get_list_by_attribute(self.bookingPage.element.headerHrefs,"href")
            #assert menu link
            assertValue=sorted(get_menu_links_page,key=str.lower)==sorted(get_menu_links_list[locale], key=str.lower)
            for menuHref in get_menu_links_page:
                self.assert_(menuHref in str(get_menu_links_list[locale]))
if __name__ == "__main__":
    unittest.main()