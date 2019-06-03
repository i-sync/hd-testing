"""
Touring Demo(My19 Recommission) landing page checking.
"""

import unittest
import pytest

from driver.browser import *

from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.report.report import *
case_name = os.path.basename(__file__).split('.')[0]

@pytest.mark.my19R
class TestTouringDemoCheckLandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser(headless=False)
        self.landingPage = LandingPage(self.driver)
        self.log = Log(r"../../report/output.txt")
    def tearDown(self):
        self.driver.quit()

    def test_touringdemo_check_landing_page(self):
        """
        04. Touring Demo(My19 Recommission) Check landing page
        """
        self.landingPage.open()
        # get all locales from landing page
        locales = self.landingPage.get_all_locales()
        self.log.info(locales)
        #check online locale
        for locale in locales:
            # time.sleep(3)
            self.log.info(locale)
            # open landing page6
            self.landingPage.open()
            # country select
            self.landingPage.select_element_by_value(self.landingPage.element.landing_country_select, locale,refresh_page=True)
            # check
            try:
                self.assertIn(locale, self.driver.current_url)
            except AssertionError as result:
                self.log.info("Touring Demo(My19 Recommission) landing page checking. this locale is error\n"+locale+"\n please review error result%s"% result)
if __name__ == "__main__":
    unittest.main()