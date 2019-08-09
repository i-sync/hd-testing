"""
MY20 RYI Home checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj12_ryi.data.locales import *
from proj12_ryi.data.marketmatrix_utils import *
from proj12_ryi.page.home_page import HomePage
import selenium.webdriver.support.expected_conditions as EC

@pytest.mark.ryi
class TestRYICheckHomePage(unittest.TestCase):
    """
    MY20 RYI Home page
    """
    def setUp(self):
        self.driver = chrome_browser()
        self.homePage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_ryi_check_social_link(self):
        """
        MY20 RYI Homepage check social link
        :return:
        """
        res = []
        # get social link matrix
        social_link_matrix = get_social_matrix()

        for locale in All_Locales:
            # open locale homePage
            self.homePage.url = "/{}/home".format(locale)
            self.homePage.open()

            # get social link
            social_links = self.homePage.get_social_links()
            if not sorted(social_links) == sorted(social_link_matrix[locale]):
                res.append(f"locale: [{locale}] social links is not equal. \rpage social links: {sorted(social_links)}\
                    \rmatrix social links:{sorted(social_link_matrix[locale])}")
                self.homePage.logger.warning(res[-1])

        if len(res):
            assert 0, "Some locales social links are incorrect."

    def test_ryi_check_ryi_button(self):
        """
        MY20 RYI Homepage check register you interest button
        :return:
        """
        for locale in All_Locales:
            # open locale homePage
            self.homePage.url = "/{}/home".format(locale)
            self.homePage.open()

            # waiting for the bottom ryi button
            self.homePage.wait_for_page_element(EC.visibility_of_element_located(self.homePage.element.homepage_ryi_button))

            # click the ryi button
            self.homePage.click_element(self.homePage.element.homepage_ryi_button, refresh_page=True)

            # check url if is the ryi-dealer
            self.assertIn("ryi-dealer", self.driver.current_url.lower(),
                          f"The current url is not correct :[{self.driver.current_url}], it should be the ryi-dealer.")

    def test_ryi_check_footer_link(self):
        """
        MY20 RYI homepage check footer links
        :return:
        """
        footer_links = ["privacy-policy", "terms-of-use", "we-care-about-you", "cookie-policy", "cookie-opt-out"]
        link_template = "https://www.harley-davidson.com/{}/{}/footer/utility/{}.html"


        res = []
        for locale in All_Locales:
            # open locale homePage
            self.homePage.url = "/{}/home".format(locale)
            self.homePage.open()

            page_footer_links = self.homePage.find_elements(self.homePage.element.homepage_footer_link)
            for index, link in enumerate(page_footer_links):
                href = link.get_attribute('href')
                target = link.get_attribute('target')
                if target != "_blank" or href != link_template.format(locale.split('_')[1], locale.split('_')[0], footer_links[index]).lower():
                    res.append(f"locale: {locale}, footer link:{href} is incorrect, target: {target} !")
                    self.homePage.logger.warning(res[-1])

        if len(res):
            assert 0, "some locale footer link is not correct, please see the log."

    def test_ryi_check_footer_country_list(self):
        """
        MY20 RYI homepage check footer country_list
        Only check en_GB locale
        :return:
        """
        # open locale homePage
        self.homePage.url = "/{}/home".format("en_GB")
        self.homePage.open()

        options = self.homePage.find_elements(self.homePage.element.homepage_footer_country_list)
        opts = [o.get_attribute('value') for o in options if o.get_attribute('value') and o.get_attribute('value') != "SWITCH LOCATION"]

        self.homePage.logger.warning(sorted(opts))
        self.homePage.logger.warning(sorted(get_all_locale()))
        self.assertListEqual(sorted(opts), sorted(get_all_locale()))

if __name__ == "__main__":
    unittest.main()
