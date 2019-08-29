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
        self.landing_Go_button = (By.CSS_SELECTOR,"div.common-cta_btn") # Go button
        #homepage
        self.homepage_cookiemodel = (By.CSS_SELECTOR, "div.cookieModel p.cookieModel__title")
        self.homepage_cookiemodel_close = (By.CSS_SELECTOR, "div.cookieModel button.cookieModel__close")
        self.homepage_social_link = (By.CSS_SELECTOR, "div.footer__share-container a[target='_blank']")
        self.homepage_footer_link = (By.CSS_SELECTOR, "footer div.footer div.footer_links-container a")
        self.homepage_ryi_button = (By.CSS_SELECTOR, "div.home a.common-cta_btn.home__btn.active")
        self.homepage_footer_country_list = (By.CSS_SELECTOR, "footer div.footer div.common_form-ipt-container select.common_form-select option")

