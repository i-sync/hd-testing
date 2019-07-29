"""
MY20 RYI Booking process .
"""

import time,os
import unittest
import pytest
from driver.browser import *
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC

from proj12_ryi.data.locales import *
from proj12_ryi.page.booking_process_page import BookingProcessPage

@pytest.mark.ryi
class TestRyiBookingProcess(unittest.TestCase):
    """
    MY20 RYI Booking process
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser()
        cls.currentPage = BookingProcessPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @pytest.mark.run(order=10)
    def test_ryi_dealer_page(self):
        """
        12. MY20 RYI Booking process :select dealer
        """
        #open dealer page
        self.currentPage.url = "/{}/location".format("en_GB")
        self.currentPage.open()

        # input letter a
        self.currentPage.input_element_value(self.currentPage.element.dealerpage_dealer_locate, 'a')

        # wait for first result item
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.dealerpage_googlemap_suggestfirst), 20)
        self.currentPage.key_action(Keys.DOWN)
        self.currentPage.key_action(Keys.ENTER)
        # self.currentPage.click_element(self.currentPage.element.dealerpage_googlemap_suggestfirst)

        # wait for the button
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.dealerpage_next_button), 20)
        # click next button
        self.currentPage.click_element(self.currentPage.element.dealerpage_next_button, refresh_page=True)

    @pytest.mark.run(order=20)
    def test_ryi_booking_error_validation(self):
        """
        12. MY20 RYI Booking process: booking error validation

        1. check the current page url should be ryi-booking
        :return:
        """

        self.assertIn("ryibooking", self.driver.current_url.lower(), "The current url is incorrent, it should be the ryi-booking.")

        # click the via post checkbox
        self.currentPage.click_element(self.currentPage.element.ryibooking_form_viapost)

        # click the submit button
        self.currentPage.click_element(self.currentPage.element.ryibooking_submit_button)

        # check the form errors
        form_errors = self.currentPage.find_elements(self.currentPage.element.ryibooking_form_errors)

        # the errors source
        errors_id = ["titleError", "firstNameError", "lastNameError", "emailError", "mobileError", "birthDayError", "myBikeNameError", "addressError1", "postcodeError"]

        # check the form_errors number
        self.assertEqual(len(form_errors), len(errors_id))

if __name__ == "__main__":
    unittest.main()