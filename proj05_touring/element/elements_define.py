from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    Touring Element Define
    """

    def __init__(self):
        """
        init function
        """
        #landing
        self.landing_country_select = (By.CSS_SELECTOR, "select.common_form-select") #country select

        #booking
