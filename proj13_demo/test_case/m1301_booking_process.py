"""
MY20 Demo Booking process .
"""

import time,os
import unittest
import pytest
from random import choice
from driver.browser import *
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from parameterized import parameterized, parameterized_class

from proj13_demo.data.marketmatrix_utils import *
from proj13_demo.page.booking_process_page import BookingProcessPage


@pytest.mark.demo
class TestDemoBookingProcess(unittest.TestCase):
    """
    MY20 DEMO Booking process
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = firefox_browser()
        cls.currentPage = BookingProcessPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_demo_booking_process(self):
        pass

    # home page
    def check_homepage_title(self):
        pass

    def check_homepage_header_icon(self):
        pass

    def check_homepage_copy(self):
        pass

    def check_homepage_cookie(self):
        pass

    def check_homepage_social_link(self):
        pass

    def check_homepage_footer_link(self):
        pass

    def check_homepage_button(self):
        pass

    # select bike page
    def check_selectbike_title(self):
        pass

    def check_selectbike_copy(self):
        pass

    def check_selectbike_bikelist(self):
        pass

    def check_selectbike_choose_bike(self):
        pass

    # select dealer page
    def check_selectdealer_title(self):
        pass

    def check_selectdealer_copy(self):
        pass

    def check_selectdealer_googlemap(self):
        pass

    def check_selectdealer_button(self):
        pass

    # booking page
    def check_booking_title(self):
        pass

    def check_booking_copy(self):
        pass

    def check_booking_privacy_popup(self):
        pass

    def check_booking_button(self):
        pass

    # thank you page
    def check_thankyou_title(self):
        pass

    def check_thankyou_copy(self):
        pass

    def check_thankyou_share_link(self):
        pass
