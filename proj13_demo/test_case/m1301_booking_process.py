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

    @parameterized.expand(['en_GB'])
    def test_demo_booking_process(self, locale):
        self.currentPage.logger.info(f"<#######[locale: {locale}]#######>")

        #homepage
        self.currentPage.logger.info(f"<=======[HOMEPAGE]=======>")

        self.open_homepage(locale)
        self.check_homepage_title()
        self.check_homepage_header()
        self.check_homepage_copy()
        self.check_homepage_cookie()
        self.check_homepage_social_link()
        self.check_homepage_footer_link()
        self.check_homepage_button()

        self.currentPage.logger.info(f"<=======[HOMEPAGE]=======>")

        #select-bike
        self.currentPage.logger.info(f"<=======[SELECT-BIKE]=======>")

        self.check_selectbike_title()
        self.check_selectbike_copy()
        self.check_selectbike_bikelist()
        self.check_selectbike_choose_bike()

        self.currentPage.logger.info(f"<=======[SELECT-BIKE]=======>")


        #select-dealer
        self.currentPage.logger.info(f"<=======[SELECT-DEALER]=======>")

        self.check_selectdealer_title()
        self.check_selectdealer_copy()
        self.check_selectdealer_googlemap()
        self.check_selectdealer_button()

        self.currentPage.logger.info(f"<=======[SELECT-DEALER]=======>")


        #booking
        self.currentPage.logger.info(f"<=======[BOOKING]=======>")

        self.check_booking_title()
        self.check_booking_copy()
        self.check_booking_privacy_popup()
        self.check_booking_button()

        self.currentPage.logger.info(f"<=======[BOOKING]=======>")

        #thankyou
        self.currentPage.logger.info(f"<=======[THANKYOU]=======>")

        self.check_thankyou_title()
        self.check_thankyou_copy()
        self.check_thankyou_share_link()

        self.currentPage.logger.info(f"<=======[THANKYOU]=======>")

        self.currentPage.logger.info(f"</#######[locale: {locale}]#######>>")

    # home page
    def open_homepage(self, locale):
        self.currentPage.logger.info(f"<-------[open home page]------>")
        self.currentPage.url = f"/{locale}/home"
        self.currentPage.open()
        self.assertIn("home", self.driver.current_url.lower(), f"Open homepage error, The url {self.driver.current_url} \
                        should be home.")
        self.currentPage.logger.info(f"</-------[open home page]------>")

    def check_homepage_title(self):
        self.currentPage.logger.info(f"<-------[check home page title]------>")
        page_title = self.currentPage.titles["home"]
        self.assertEqual(page_title, self.driver.title, f"home page title is incorrect: [{self.driver.title}]")
        self.currentPage.logger.info(f"</-------[check home page title]------>")

    def check_homepage_header(self):
        self.currentPage.logger.info(f"<-------[check home page header]------>")
        # logo icon
        home_link = self.currentPage.find_element(self.currentPage.element.hoempage_header_logo).get_attribute("href")
        self.assertIn("home", home_link, f"Home icon like incorrect: {home_link}")
        share_links = self.currentPage.find_elements(self.currentPage.element.homepage_header_share)
        self.assertIn(self.driver.current_url.split("@")[1].strip("/home"), share_links[0].get_attribute("href"), f"Feckbook share link incorrect")
        self.assertIn(self.driver.current_url.split("@")[1], share_links[1].get_attribute("href"), f"Twitter share link incorrect")
        self.currentPage.logger.info(f"</-------[check home page header]------>")

    def check_homepage_copy(self):
        self.currentPage.logger.info(f"<-------[check home page copy]------>")
        title_h1 = self.currentPage.get_element_text(self.currentPage.element.homepage_copy_title_h1)
        if title_h1.strip() == "--":
            self.currentPage.logger.warning("Homepage [title h1] copy is empty")

        section1_title = self.currentPage.get_element_text(self.currentPage.element.homepage_copy_section1_title)
        if section1_title.strip() == "--":
            self.currentPage.logger.warning("Homepage [section1 title] copy is empty")
        section1_desc = self.currentPage.get_element_text(self.currentPage.element.homepage_copy_section1_desc)
        if section1_desc.strip() == "--":
            self.currentPage.logger.warning("Homepage [section1 desc] copy is empty")
        section1_button = self.currentPage.get_element_text(self.currentPage.element.homepage_copy_section1_button)
        if section1_button.strip() == "--":
            self.currentPage.logger.warning("Homepage [section1 button] copy is empty")
        self.currentPage.logger.info(f"</-------[check home page copy]------>")

    def check_homepage_cookie(self):
        self.currentPage.logger.info(f"<-------[check home page cookie]------>")
        # wait for the cookie panel display
        self.currentPage.wait_for_page_element(
            EC.visibility_of_element_located(self.currentPage.element.homepage_cookiemodel))
        # get the cookie copy
        cookie = self.currentPage.get_element_text(self.currentPage.element.homepage_cookiemodel)
        if cookie in ["--", ""]:
            self.currentPage.logger.warning("Homepage cookie panel is empty.")

        # close the cookie panel
        self.currentPage.click_element(self.currentPage.element.homepage_cookiemodel_close)
        # wait for the cookie panel disappear
        self.currentPage.wait_for_page_element(
            EC.invisibility_of_element_located(self.currentPage.element.homepage_cookiemodel))
        # check the cookie model is not visible
        self.assertFalse(self.currentPage.find_element(self.currentPage.element.homepage_cookiemodel).is_displayed(),
                             "close cookie panel failed.")
        self.currentPage.logger.info(f"</-------[check home page cookie]------>")

    def check_homepage_social_link(self):
        self.currentPage.logger.info(f"<-------[check home page social link]------>")
        # 0. locale : [http://my20.proferochina.com/en_GB/home]
        locale = self.driver.current_url.split('/')[-2]

        # get social link matrix
        social_link_matrix = get_social_matrix()
        # get page social link
        social_links = self.currentPage.get_social_links()
        if not sorted(social_links) == sorted(social_link_matrix[locale]):
            self.currentPage.logger.warning(f"locale: [{locale}] social links is not equal. \rpage social links: {sorted(social_links)}\
                            \rmatrix social links:{sorted(social_link_matrix[locale])}")

        self.currentPage.logger.info(f"</-------[check home page social link]------>")

    def check_homepage_footer_link(self):
        self.currentPage.logger.info(f"<-------[check home page footer link]------>")
        # 0. locale : [http://my20.proferochina.com/en_GB/home]
        locale = self.driver.current_url.split('/')[-2]

        footer_links = ["privacy-policy", "terms-of-use", "we-care-about-you", "cookie-policy", "cookie-opt-out"]
        link_template = "https://www.harley-davidson.com/{}/{}/footer/utility/{}.html"

        page_footer_links = self.currentPage.find_elements(self.currentPage.element.homepage_footer_link)
        for index, link in enumerate(page_footer_links):
            href = link.get_attribute('href')
            target = link.get_attribute('target')
            if target != "_blank" or href != link_template.format(locale.split('_')[1], locale.split('_')[0],
                                                                  footer_links[index]).lower():
                self.currentPage.logger.warning(f"locale: {locale}, footer link:{href} is incorrect, target: {target} !")

        self.currentPage.logger.info(f"</-------[check home page footer link]------>")

    def check_homepage_button(self):
        self.currentPage.logger.info(f"<-------[check home page button]------>")
        # location_once_scrolled_into_view
        # height = self.currentPage.find_element(self.currentPage.element.homepage_booking_button).location_once_scrolled_into_view

        self.currentPage.script("window.scrollTo(0, document.body.scrollHeight);")

        # click book now button
        self.currentPage.click_element(self.currentPage.element.homepage_booking_button, refresh_page=True)

        # check the URL if correct
        self.assertIn("select-bike", self.driver.current_url, f"The current URL is incorrect: [{self.driver.current_url}]")
        self.currentPage.logger.info(f"</-------[check home page button]------>")

    # select bike page
    def check_selectbike_title(self):
        self.currentPage.logger.info(f"<-------[check select bike title]------>")

        page_title = self.currentPage.titles["select-bike"]
        self.assertEqual(page_title, self.driver.title, f"select-bike page title is incorrect: [{self.driver.title}]")

        self.currentPage.logger.info(f"</-------[check select bike title]------>")

    def check_selectbike_copy(self):
        self.currentPage.logger.info(f"<-------[check select bike copy]------>")

        self.currentPage.logger.info(f"</-------[check select bike copy]------>")

    def check_selectbike_bikelist(self):
        self.currentPage.logger.info(f"<-------[check select bike bikelist]------>")
        # 0. locale : [http://my20.proferochina.com/en_GB/home]
        locale = self.driver.current_url.split('/')[-2]

        # 1. Get bikelist matrix
        bikes = get_bike_matrix()[locale]
        self.currentPage.logger.warning(bikes)
        # 2. Get page bike list
        res = []
        categories = self.currentPage.find_elements(self.currentPage.element.selectbike_bikelist)
        cant_decide = self.currentPage.find_element(self.currentPage.element.selectbike_cant_decide)
        for index, c in enumerate(categories):
            title = c.find_element_by_css_selector(self.currentPage.element.selectbike_bikelist_title[1]).text.strip()
            bl = c.find_elements_by_css_selector(self.currentPage.element.selectbike_bikelist_list[1])
            bikeid = [a.get_attribute("href").split("=")[1] for a in bl if
                      a.get_attribute("href") and a.get_attribute("href").find("=") > -1]
            if index == 3:
                bikeid.append(cant_decide.get_attribute('href').split("=")[1])
            if not sorted(bikes[index]) == sorted(bikeid):
                self.currentPage.logger.warning(f"Locale: [{locale}], Category: [{title}], Matrix: [{sorted(bikes[index])}], Page: [{sorted(bikeid)}]")

        self.currentPage.logger.info(f"</-------[check select bike bikelist]------>")

    def check_selectbike_choose_bike(self):
        self.currentPage.logger.info(f"<-------[check select bike choose bike]------>")

        # choice one bike
        bikes = self.currentPage.find_elements(self.currentPage.element.selectbike_bikelist_list)
        bike = choice(bikes)
        bike.click()
        with self.currentPage.wait_for_page_load():
            bike.click()

        # check the URL if correct.
        self.assertIn("select-dealer", self.driver.current_url.lower(),
                      f"The current url is incorrent :[{self.driver.current_url}], it should be the booking.")

        self.currentPage.logger.info(f"</-------[check select bike choose bike]------>")

    # select dealer page
    def check_selectdealer_title(self):
        self.currentPage.logger.info(f"<-------[check select dealer title]------>")

        page_title = self.currentPage.titles["select-dealer"]
        self.assertEqual(page_title, self.driver.title, f"select-dealer page title is incorrect: [{self.driver.title}]")

        self.currentPage.logger.info(f"</-------[check select dealer title]------>")

    def check_selectdealer_copy(self):
        self.currentPage.logger.info(f"<-------[check select dealer copy]------>")

        self.currentPage.logger.info(f"</-------[check select dealer copy]------>")

    def check_selectdealer_googlemap(self):
        self.currentPage.logger.info(f"<-------[check select dealer googlemap]------>")

        time.sleep(2)
        # input letter a
        self.currentPage.input_element_value(self.currentPage.element.selectdealer_dealer_locate, 'a')
        # wait for first result item
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.selectdealer_googlemap_suggestfirst))
        self.currentPage.key_action(Keys.DOWN)
        self.currentPage.key_action(Keys.ENTER)
        # self.currentPage.click_element(self.currentPage.element.selectdealer_googlemap_suggestfirst)

        self.currentPage.logger.info(f"</-------[check select dealer googlemap]------>")

    def check_selectdealer_button(self):
        self.currentPage.logger.info(f"<-------[check select dealer button]------>")

        # wait for the button
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.selectdealer_button))
        # click button
        self.currentPage.click_element(self.currentPage.element.selectdealer_button, refresh_page=True)

        self.assertIn("booking", self.driver.current_url.lower(),
                      f"booking page error! : [{self.driver.current_url}], it should be the booking.")
        self.currentPage.logger.info(f"</-------[check select dealer button]------>")

    # booking page
    def check_booking_title(self):
        self.currentPage.logger.info(f"<-------[check booking title]------>")

        page_title = self.currentPage.titles["booking"]
        self.assertEqual(page_title, self.driver.title, f"select-dealer page title is incorrect: [{self.driver.title}]")

        self.currentPage.logger.info(f"</-------[check booking title]------>")

    def check_booking_copy(self):
        self.currentPage.logger.info(f"<-------[check booking copy]------>")


        self.currentPage.logger.info(f"</-------[check booking copy]------>")

    def check_booking_privacy_popup(self):
        """
        booking page privacy popup checking
        1. click page privacy notification link.
        2. check the first popup if showing.
        3. click the first popup close icon, check if the first popup if closing.
        """
        self.currentPage.logger.info(f"<-------[check booking privacy popup]------>")

        # click privacy notification link
        self.currentPage.click_element(self.currentPage.element.booking_privacy_page_link)

        # waiting for privacy popup showing
        self.currentPage.wait_for_page_element(
            EC.visibility_of_element_located(self.currentPage.element.booking_privacy_first_popup))

        # check the privacy popup is visible
        self.assertTrue(self.currentPage.find_element(
            self.currentPage.element.booking_privacy_first_popup).is_displayed(), "Privacy popup is not showing.")

        # click the first popup close icon
        self.currentPage.click_element(self.currentPage.element.booking_privacy_first_popup_close)

        # waiting for first popup closing
        self.currentPage.wait_for_page_element(
            EC.invisibility_of_element_located(self.currentPage.element.booking_privacy_first_popup))

        # check the first popup is not visible
        self.assertFalse(self.currentPage.find_element(
            self.currentPage.element.booking_privacy_first_popup).is_displayed(), "First popup is not closing.")

        self.currentPage.logger.info(f"</-------[check booking privacy popup]------>")

    def check_booking_button(self):
        """
        MY20 DEMO booking process: auto submit booking
        1. Title : select first one.
        2. First Name : Test_DEMO_FN
        3. Last Name: Test_DEMO_LN
        4. Email: My email
        5. Mobile: 123456789
        6. Date of birth: 29-07-1990
        7. License: Yes
        8. Motorcycle: choice one ["Aprilia", "BMW", "Ducati", "HarleyDavidson", "Honda", "Hyosung", "Indian", "Kawasaki", "KTM", "Moto Guzzi", "MVAgusta", "Other", "Suzuki", "Triumph", "Victory", "Yamaha"]
        9. Via email: Yes
        10.Via phone: Yes
        11.Submit the form.
        """
        self.currentPage.logger.info(f"<-------[check booking button]------>")

        form_data = {
            "firstname": "Test_DEMO_FN",
            "lastname": "Test_DEMO_LN",
            "email": "michael.tian@profero.com",
            "mobile": "123456789",
            "birthday": "29-07-1990",
            "motorcycle": choice(
                ["Aprilia", "BMW", "Ducati", "HarleyDavidson", "Honda", "Hyosung", "Indian", "Kawasaki", "KTM",
                 "Moto Guzzi", "MVAgusta", "Other", "Suzuki", "Triumph", "Victory", "Yamaha"])
        }
        # 1. Title
        self.currentPage.select_element_by_index(self.currentPage.element.booking_form_title, 1)

        # 2. First Name
        self.currentPage.input_element_value(self.currentPage.element.booking_form_firstname, form_data["firstname"])

        # 3. Last Name
        self.currentPage.input_element_value(self.currentPage.element.booking_form_lastname, form_data["lastname"])

        # 4. Email
        self.currentPage.input_element_value(self.currentPage.element.booking_form_email, form_data["email"])

        # 5. Mobile
        self.currentPage.input_element_value(self.currentPage.element.booking_form_mobile, form_data["mobile"])

        # 6. Birthday
        # self.currentPage.input_element_value(self.currentPage.element.booking_form_birthday, form_data["birthday"])
        self.currentPage.script('document.querySelector("#birthDay").value = "{}"'.format(form_data["birthday"]))

        # 8. Motorcycle
        self.currentPage.select_element_by_value(self.currentPage.element.booking_form_motocycle,
                                                 form_data["motorcycle"])

        # 9. Via Email
        self.currentPage.click_element(self.currentPage.element.booking_form_viaemail)

        # 10. Via Phone
        self.currentPage.click_element(self.currentPage.element.booking_form_viaphone)

        # 11. Close Via Post
        #self.currentPage.click_element(self.currentPage.element.booking_form_viapost)

        # 11. Submit Form, waiting for page refresh.
        self.currentPage.click_element(self.currentPage.element.booking_submit_button, refresh_page=True)

        # 12 check the URL if correct.
        self.assertIn("thankyou", self.driver.current_url.lower(),
                      f"The current url is incorrect :[{self.driver.current_url}], it should be the thankyou.")

        self.currentPage.logger.info(f"</-------[check booking button]------>")

    # thank you page
    def check_thankyou_title(self):
        self.currentPage.logger.info(f"<-------[check thankyou page title]------>")

        page_title = self.currentPage.titles["thankyou"]
        self.assertEqual(page_title, self.driver.title, f"thankyou page title is incorrect: [{self.driver.title}]")

        self.currentPage.logger.info(f"</-------[check thankyou page title]------>")

    def check_thankyou_copy(self):
        self.currentPage.logger.info(f"<-------[check thankyou page copy]------>")

        self.currentPage.logger.info(f"</-------[check thankyou page copy]------>")

    def check_thankyou_share_link(self):
        self.currentPage.logger.info(f"<-------[check thankyou page share link]------>")

        self.currentPage.logger.info(f"</-------[check thankyou page share link]------>")
