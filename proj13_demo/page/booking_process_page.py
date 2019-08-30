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
        #self.url = "/{}/home"
        super(BookingProcessPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

        # titles
        self.titles = {"home": "Harley-Davidson® | Ride Free",
                       "select-bike": "Harley-Davidson® | Ride Free - Choose your ride",
                       "select-dealer": "Harley-Davidson® | Ride Free - Select a dealer",
                       "booking": "Harley-Davidson® | Ride Free - Enter your details",
                       "thankyou": "Harley-Davidson® | Ride Free - Thanks"}

    def get_social_links(self):
        """
        Get HomePage Social Link
        :return:
        """
        social_links = self.find_elements(self.element.homepage_social_link)
        return [a.get_attribute("href") for a in social_links if a.get_attribute("href")]