"""
MY20 RYI Dealer checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from proj12_ryi.data.locales import *
from proj12_ryi.page.dealer_page import DealerPage

@pytest.mark.ryi
@pytest.mark.live_checker
class TestRYICheckDealerPage(unittest.TestCase):
    """
    MY20 RYI Dealer page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.dealerPage = DealerPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_ryi_check_dealer_page(self):
        """
        12. MY20 RYI Dealer page
        steps:
            1. Input letter 'a' into google map
            2. Select first result item
            3. Click the next button goto ryi-booking page
        """
        # check all locale
        for locale in Testing:
            # open dealer page
            self.dealerPage.url = self.dealerPage.url.format(locale)
            self.dealerPage.open()

            # input letter a
            self.dealerPage.input_element_value(self.dealerPage.element.dealerpage_dealer_locate, 'a')

            # wait for first result item
            self.dealerPage.wait_for_page_element(EC.element_to_be_clickable(self.dealerPage.element.dealerpage_googlemap_suggestfirst), 20)
            self.dealerPage.key_action(Keys.DOWN)
            self.dealerPage.key_action(Keys.ENTER)
            # self.dealerPage.click_element(self.dealerPage.element.dealerpage_googlemap_suggestfirst)

            # wait for the button
            self.dealerPage.wait_for_page_element(EC.element_to_be_clickable(self.dealerPage.element.dealerpage_next_button), 20)
            # click next button
            self.dealerPage.click_element(self.dealerPage.element.dealerpage_next_button, refresh_page=True)

if __name__ == "__main__":
    unittest.main()
