from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    MY20 RYI Element Define
    """

    def __init__(self):
        """
        init function
        """
        #homepage
        self.homepage_cookiemodel = (By.CSS_SELECTOR, "div.cookieModel p.cookieModel__title")
        self.homepage_cookiemodel_close = (By.CSS_SELECTOR, "div.cookieModel button.cookieModel__close")

        #dealer page
        self.dealerpage_dealer_locate = (By.ID, "searchTextField")
        self.dealerpage_googlemap_suggestfirst = (By.CSS_SELECTOR, "div.pac-container div.pac-item")
        self.dealerpage_next_button = (By.CSS_SELECTOR, "#locationForm .googleMap__container button.common-cta_btn")

        #ryi-booking
        self.ryibooking_submit_button = (By.CSS_SELECTOR, "div.formModel div.common_sections button.common-cta_btn")
        self.ryibooking_form_errors = (By.CSS_SELECTOR, "div.formModel div.common_sections.form_error")

        # ryi-form-field
        self.ryibooking_form_title = (By.ID, "title")
        self.ryibooking_form_firstname = (By.ID, "firstName")
        self.ryibooking_form_lastname = (By.ID, "lastName")
        self.ryibooking_form_email = (By.ID, "email")
        self.ryibooking_form_mobile = (By.ID, "mobile")
        self.ryibooking_form_birthday = (By.ID, "birthDay")
        # licence has default value, ignore.
        self.ryibooking_form_motocycle = (By.ID, "myBikeName")
        self.ryibooking_form_viaemail = (By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='useEmail']")
        self.ryibooking_form_viaphone = (By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='usePhone']")
        self.ryibooking_form_viapost = (By.CSS_SELECTOR, "div.formModel__inner div.common_form-radio-container label.common_form-label[for='usePost']")

        # ryi-thankyou
        self.ryithankyou_bikelist = (By.CSS_SELECTOR, "div.thanksPage div.thanksPage__main div.bikeList")
        self.ryithankyou_bikelist_title = (By.CSS_SELECTOR, "div.bikeList__titleBox p.bikeList__title")
        self.ryithankyou_bikelist_list = (By.CSS_SELECTOR, "div.bikeList__out .slick-list a.bikeList__box")