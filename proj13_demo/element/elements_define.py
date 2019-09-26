from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    MY20 DEMO Element Define
    """

    def __init__(self):
        """
        init function
        """
        #landingPage
        self.landing_country_select = (By.CSS_SELECTOR, "select.common_form-select") #country select
        self.landing_country_options = (By.CSS_SELECTOR, "select.common_form-select option")  # country select option
        self.landing_go_button = (By.CSS_SELECTOR,"div.common-cta_btn") # Go button
        #homepage
        self.homepage_cookiemodel = (By.CSS_SELECTOR, "div.cookieModel p.cookieModel__title")
        self.homepage_cookiemodel_close = (By.CSS_SELECTOR, "div.cookieModel button.cookieModel__close")

        self.hoempage_header_logo = (By.CSS_SELECTOR, "header.navigation.home__header a")
        self.homepage_header_share = (By.CSS_SELECTOR, "header.navigation.home__header div.navigation-icon_box a[target='_blank']")

        self.homepage_social_link = (By.CSS_SELECTOR, "div.footer__share-container a[target='_blank']")
        self.homepage_footer_link = (By.CSS_SELECTOR, "footer div.footer div.footer_links-container a")
        self.homepage_booking_button = (By.CSS_SELECTOR, "div.home a.common-cta_btn.home__btn.active")
        self.homepage_footer_country_list = (By.CSS_SELECTOR, "footer div.footer div.common_form-ipt-container select.common_form-select option")
        # homepage copy
        self.homepage_copy_title_h1 = (By.CSS_SELECTOR, "div.home__section p.loadSection__title.paragraph__title-h1")
        self.homepage_copy_section1_title = (By.CSS_SELECTOR, "div.home__section div.loadSection__box p.loadSection__sub")
        self.homepage_copy_section1_desc = (By.CSS_SELECTOR, "div.home__section div.loadSection__box p.loadSection__paragraph")
        self.homepage_copy_section1_button = (By.CSS_SELECTOR, "div.home__section div.loadSection__box a.common-cta_btn")

        self.homepage_copy_section2_title = (By.CSS_SELECTOR, "div.home__section div.section2 div.section2__box p.section2__title")
        self.homepage_copy_section2_subtitle = (By.CSS_SELECTOR, "div.home__section div.section2 div.section2__box p.section2__subTitle")
        self.homepage_copy_section2_desc = (By.CSS_SELECTOR, "div.home__section div.section2 div.section2__box div.section2__text")
        self.homepage_copy_section2_1_title = (By.CSS_SELECTOR, "div.home__section div.section2__show-box.first p.paragraph__title-h5")
        self.homepage_copy_section2_1_desc = (By.CSS_SELECTOR, "div.home__section div.section2__show-box.first p.paragraph__body-mid")
        self.homepage_copy_section2_2_title = (By.CSS_SELECTOR, "div.home__section div.section2__show-box p.paragraph__title-h5")
        self.homepage_copy_section2_2_desc = (By.CSS_SELECTOR, "div.home__section div.section2__show-box p.paragraph__body-mid")

        self.homepage_copy_section3_title_mobile = (By.CSS_SELECTOR, "div.section3 div.section3__bg div.section3__only-mobile p")
        self.homepage_copy_section3_title_desktop = (By.CSS_SELECTOR, "div.section3 div.section3__gb div.section3__only-desktop p")

        self.homepage_copy_section4_top_title = (By.CSS_SELECTOR, "div.section4 div.section4__right-hero div.section4__right-topTitle")
        self.homepage_copy_section4_title = (By.CSS_SELECTOR, "div.section4 div.section4__right-box div.section4__right-title")
        self.homepage_copy_section4_desc = (By.CSS_SELECTOR, "div.section4 div.section4__right-box div.section4__right-par")

        self.homepage_copy_section5_title = (By.CSS_SELECTOR, "div.finalSection div.finalSection__left div.finalSection__left-title p")
        self.homepage_copy_section5_title1 = (By.CSS_SELECTOR, "div.finalSection div.finalSection__text-box div.finalSection__text-title")
        self.homepage_copy_section5_desc = (By.CSS_SELECTOR, "div.finalSection div.finalSection__text-box div.finalSection__text-par")

        # select bike page
        self.selectbike_bikelist = (By.CSS_SELECTOR, "div.selectBike div.selectBike__box div.bikeList")
        self.selectbike_bikelist_title = (By.CSS_SELECTOR, "div.bikeList__titleBox p.bikeList__title")
        self.selectbike_bikelist_list = (By.CSS_SELECTOR, "div.bikeList__out a.bikeList__box")
        self.selectbike_cant_decide = (By.CSS_SELECTOR, "div.selectBike div.selectBike__box div.selectBike__decide a")

        # select dealer page
        self.selectdealer_dealer_locate = (By.ID, "searchTextField")
        self.selectdealer_googlemap_suggestfirst = (By.CSS_SELECTOR, "div.pac-container div.pac-item")
        self.selectdealer_button = (By.CSS_SELECTOR, "#locationForm .googleMap__container button.common-cta_btn")

        # booking-privacy-popup
        self.booking_privacy_page_link = (By.CSS_SELECTOR, "div.formModel div.common_sections p.paragraph__body-mid a.org-colored")
        self.booking_privacy_first_popup = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.firstPop")
        self.booking_privacy_second_popup = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.secondPop")
        self.booking_privacy_first_popup_close = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.firstPop div.popup__close")
        self.booking_privacy_second_popup_close = (By.CSS_SELECTOR, "div.formModel div.common_sections div.popup.secondPop div.popup__close")

        # booking-form-field
        self.booking_form_title = (By.ID, "title")
        self.booking_form_firstname = (By.ID, "firstName")
        self.booking_form_lastname = (By.ID, "lastName")
        self.booking_form_email = (By.ID, "email")
        self.booking_form_mobile = (By.ID, "mobile")
        self.booking_form_birthday = (By.ID, "birthDay")
        # licence has default value, ignore.
        self.booking_form_motocycle = (By.ID, "myBikeName")
        self.booking_form_viaemail = (
        By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='useEmail']")
        self.booking_form_viaphone = (
        By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='usePhone']")
        self.booking_form_viapost = (
        By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='usePost']")


        self.booking_submit_button = (By.CSS_SELECTOR, "div.formModel div.common_sections button.common-cta_btn")

        # thankyou page
        self.thankyou_share_link = (By.CSS_SELECTOR, "div.shareBar div.shareBar__iconBox a[target='_blank']")