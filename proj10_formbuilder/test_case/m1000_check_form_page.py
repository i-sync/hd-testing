"""
FormBuilder Form page checking.
"""

import unittest
import pytest
from driver.browser import *
from proj10_formbuilder.page.form_page import FormPage


@pytest.mark.live_checker
class TestFormBuilderCheckFormPage(unittest.TestCase):
    def setUp(self):
        self.driver = firefox_browser()
        self.form_page = FormPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_formbuilder_check_form_page(self):
        """
        10. FormBuilder Form page
        """

        self.form_page.open()
        submit_button_text = self.form_page.get_element_text(self.form_page.element.form_submit_button)
        self.assertEqual("SUBMETER", submit_button_text.strip())


if __name__ == "__main__":
    unittest.main()
