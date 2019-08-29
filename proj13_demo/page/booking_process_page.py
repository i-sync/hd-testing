"""
MY20 RYI Booking Process Page
the steps:
    1. start from select dealer
    2. then goto ryi-booking
    3. goto ryi-thankyou
    4. check bike list
    5. goto booking
    6. goto final thankyou

"""

from page.page import Page
from proj13_demo.data.urls import current_url
from proj13_demo.element.elements_define import ElementsDefine


class BookingProcessPage(Page):
    """
    MY20 DEMO Booking Process Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        # self.url = "/{}/home"
        super(BookingProcessPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

