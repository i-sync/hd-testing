"""
Touring Demo(My19 Recommission) landing page checking.
"""

import time,os
import unittest
import pytest
import time
from driver.browser import *
from selenium.webdriver.common.keys import Keys
from proj04_touringdemo.page.landing_page import LandingPage
from proj04_touringdemo.page.booking_page import BookingPage
from proj04_touringdemo.report.report import *
@pytest.mark.my19RForm
class TestTouringDemoCheckBookingFormPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = chrome_browser()
        cls.landingPage = LandingPage(cls.driver)
        cls.bookingPage = BookingPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_touringdemo_booking_from_page(self):
        """
        Touring Demo(My19 Recommission)
        step:
        1.select one locale on landing page
        2.click book a ride test button
        3. choose first bike on home
        4. finished form(a.doesn't finish form and submit;b.finished form and submit)
        5. submit form
        """
        # get all of locales
        self.landingPage.open()
        locales = self.landingPage.get_all_locales()
        for locale in locales:
            # open locale booking page
            self.bookingPage.url = "/{}".format(locale)
            self.bookingPage.url = self.bookingPage.url + "/booking"
            self.bookingPage.open()
            # choose first bike on home
            time.sleep(3)
            bike_list = self.bookingPage.get_list(self.bookingPage.element.bike_value_list)
            bike_list[0].click()
            # input map
            self.bookingPage.click_element(self.bookingPage.element.dealerMap)
            self.bookingPage.input_element_value(self.bookingPage.element.dealerMap, "OP")
            # choose first map
            time.sleep(3)
            self.bookingPage.key_action(Keys.DOWN)
            time.sleep(0.5)
            self.bookingPage.key_action(Keys.ENTER)
            time.sleep(0.5)
            self.bookingPage.key_action(Keys.ENTER)
            time.sleep(3)
            # submit form when all forms are empty
            self.bookingPage.click_element(self.bookingPage.element.requestTestRideButton)

            #check error message that is not --
            error_message_list = self.bookingPage.get_list_by_attribute(self.bookingPage.element.errorMessage,"text")
            errorLenght=len(error_message_list)
            #check error message lenght
            self.assertTrue(10,errorLenght)
            try:
                for error in error_message_list:
                    self.assertNotIn(error, "--")
                error_message_div_list=self.bookingPage.get_list_by_attribute(self.bookingPage.element.errorMessage_checkbox,"text")
                errorDivLenght = len(error_message_div_list)
                self.assertTrue(2, errorDivLenght)
                for error in error_message_div_list:
                    self.assertNotIn(error, "--")
            except AssertionError as result:
                info="Touring Demo(My19 Recommission) booking form check:\n error locale is %s"%locale+"error message is %s"% result
                self.bookingPage.logger.info(info)
        # '''check finished form'''
        # self.bookingPage.click_element(self.bookingPage.element.chooseTitle) # click title
        # self.bookingPage.click_element(self.bookingPage.element.chooseFirstTitle) # select first title
        # self.bookingPage.input_element_value(self.bookingPage.element.firstName,FormContent["FirstName"]) #input first name
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["LastName"]) #input last name
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["Email"]) #input email
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["Moble"]) #input Moble
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["PostCode"]) #input PostCode
        # # input Date
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["DateDD"])
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["DateMM"])
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["DateYYYY"])
        # #select motorcycle
        # #select own a motorcycle->Yes
        # self.bookingPage.click_element(self.bookingPage.element.motorcycleYes)
        # self.landingPage.select_element_by_value(self.bookingPage.element.brandSelect,FormContent["ownBrand"]) #select ownBrand
        # #select full motorcycle licence->Yes
        # self.bookingPage.click_element(self.bookingPage.element.fullMatorcycleYes)
        # #select Via email
        # self.bookingPage.click_element(self.bookingPage.element.viaEmail)
        # #select Via phone
        # self.bookingPage.click_element(self.bookingPage.element.viaPhone)
        # #select Via post
        # self.bookingPage.click_element(self.bookingPage.element.viaPost)
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["PostAddress1"]) #input PostAddress1
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["PostAddress2"]) #input PostAddress2
        # self.bookingPage.input_element_value(self.bookingPage.element.lastName,FormContent["City"]) #input City
        # #select Submit
        # self.bookingPage.click_element(self.bookingPage.element.requestTestRideButton)

if __name__ == "__main__":
    unittest.main()