from selenium.webdriver.common.by import By


class ElementsDefine(object):
    """
    FormBuilder Element Define
    """

    def __init__(self):
        """
        init function
        """
        # form page
        self.form_submit_button = (By.CSS_SELECTOR, "form#hdForm li.submitBtn button span")
