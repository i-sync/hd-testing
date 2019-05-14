from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    TRBF Element Define
    """

    def __init__(self):
        """
        init function
        """
        #landing
        self.landing_country_select = (By.CSS_SELECTOR, "select#selectCountry") #country select
        self.landing_country_options = (By.CSS_SELECTOR, "select#selectCountry option") #country select option
        #self.landing_continue_button = (By.CSS_SELECTOR, "button.common-cta_btn") #start your votes
        #booking
