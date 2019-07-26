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

        #booking
        pass