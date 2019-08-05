"""
Touring Demo(My19 Recommission) landing page checking.
"""

import unittest
import pytest

from driver.browser import *

from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.report.report import *

@pytest.mark.my19R
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
        self.landingPage = LandingPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_touringdemo_check_landing_page(self):
        """
        04. Touring Demo(My19 Recommission) Check landing page
        """
        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()
        #check online locale
        for locale in locales:
            time.sleep(3)
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale,refresh_page=True)
            # check url
            try:
                self.assertIn(locale, self.driver.current_url)
            except AssertionError as result:
                info = "Touring Demo(My19 Recommission) landing page checking. this locale is error\n"+locale+"\n please review error result%s"% result
                self.landingPage.logger.info(info)

            # open landing page
            self.landingPage.open()

if __name__ == "__main__":
    unittest.main()