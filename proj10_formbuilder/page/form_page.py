"""
FormBuilder Form Page
"""

from page.page import Page
from proj10_formbuilder.data.urls import current_url
from proj10_formbuilder.element.elements_define import ElementsDefine


class FormPage(Page):
    """
    FormBuilder Form Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        # testing url: https://form.harley-davidson.com/pt_BR/BR1835403
        self.url = "/pt_BR/BR1835403"
        super(FormPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()
