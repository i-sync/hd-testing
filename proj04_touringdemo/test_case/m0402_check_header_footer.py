"""
Touring Demo(My19 Recommission) landing page checking.
"""

import unittest
import pytest
from driver.browser import *
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage
from proj04_touringdemo.data.marketmatrix_utils import *
from proj04_touringdemo.report.report import *

@pytest.mark.my19R
class TestTouringDemoCheckHeaderFooterPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
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
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale,refresh_page=True)
            # get footer link list
            get_footer_links_page = self.bookingPage.get_list_by_attribute(self.bookingPage.element.footerIconHrefs,"href")
            if locale in["de_AT","de_CH"]:
                time.sleep(3)
                self.bookingPage.logger.info(get_footer_list[locale])
            # assert footer icon links
            try:
                for footerHref in get_footer_links_page:
                    self.assertTrue(footerHref in get_footer_list[locale])

            except AssertionError as result:
                self.bookingPage.logger.info(
                    "Touring Demo(My19 Recommission) footerHref check issue locale is \n"+locale+" ,\n please review error result%s" % result)

            #sleep
            time.sleep(3)
             # click menu icon
            self.bookingPage.click_element(self.bookingPage.element.menuIcon)
            # get menu link list
            get_menu_links_page = self.bookingPage.get_list_by_attribute(self.bookingPage.element.headerHrefs,"href")
            #assert menu link
            try:
                for menuHref in get_menu_links_page:

                        if "twitter" in menuHref:
                            twitter = "https:\/\/twitter\.com\/intent\/tweet\?hashtags=(.*)&text=+(.*)url=https:\/\/ridefree\.harley-davidson\.com\/" + locale
                            self.assertRegex(menuHref,twitter)
                        else:
                            self.assertTrue(menuHref in get_menu_links_list[locale])
            except AssertionError as result:
                self.bookingPage.logger.info(
                    "Touring Demo(My19 Recommission) header&footer link checking.this locale has some issue ,\n please review error result%s" % result)


if __name__ == "__main__":
    unittest.main()