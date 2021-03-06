from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    Spring Demo Element Define
    """

    def __init__(self):
        """
        init function
        """
        #landing
        self.landing_country_select = (By.CSS_SELECTOR, "select.common_form-select") #country select
        self.landing_continue_button = (By.CSS_SELECTOR, "div.common-cta_btn") #continue button

        #homepage
        self.homepage_social_link = (By.CSS_SELECTOR, "div.footer .common_sections .footer_icon-container a") #footer social link
        self.homepage_bike_list = (By.CSS_SELECTOR, "div.bike .bike__list-items") #bike list