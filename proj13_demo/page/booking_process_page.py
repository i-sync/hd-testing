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
import datetime,io,time
from page.page import Page
from proj13_demo.data.urls import current_url
from proj13_demo.element.elements_define import ElementsDefine

from PIL import Image

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


    def take_screenshot(self, locale, page):
        path = "report/screenshot/proj13"
        filename = f"{path}/{locale}-{datetime.datetime.now():%Y%m%d%H%M%S}-{page}.png"
        self.driver.find_element_by_tag_name('html').screenshot(filename)

    def take_scroll_screenshot(self, locale, page):
        js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight,  document.documentElement.clientHeight,  document.documentElement.scrollHeight,  document.documentElement.offsetHeight);'
        scrollheight = self.driver.execute_script(js)

        slices = []
        offset = 0
        while offset < scrollheight:
            self.driver.execute_script("window.scrollTo(0, %s);" % offset)
            time.sleep(1.5)
            img = Image.open(io.BytesIO(self.driver.get_screenshot_as_png()))
            offset += img.size[1]
            slices.append(img)

        screenshot = Image.new('RGB', (slices[0].size[0], offset))
        offset = 0
        for img in slices:
            screenshot.paste(img, (0, offset))
            offset += img.size[1]

        path = "report/screenshot/proj13"
        filename = f"{path}/{locale}-{datetime.datetime.now():%Y%m%d%H%M%S}-{page}.png"
        screenshot.save(filename)
