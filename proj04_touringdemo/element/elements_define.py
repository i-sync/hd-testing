from selenium.webdriver.common.by import By

class ElementsDefine(object):
    """
    Touring Demo(My19 Recommission) Element Define
    """

    def __init__(self):
        """
        init function
        """
        #landing page
        self.landing_country_select = (By.CSS_SELECTOR, "select.common_form-select") #country select
        self.landing_country_options = (By.CSS_SELECTOR, "select.common_form-select option")  # country select option

        #Home page
        #book a ride test button
        self.choose_book_button = (By.XPATH,"//div[@class='main_page-black-box padding_up-container padding_down-container']/div/div[@class='common_sections']//a")

        # Booking page
        # text on bike
        self.text_on_bike=(By.CSS_SELECTOR,"p.confirmation_bikes-name.upper-case-texts")
        self.find_bikes=(By.CSS_SELECTOR,"div.my19-container div.confirmation_bikes-container")
        #first bike
        self.bike_value_list = (By.CSS_SELECTOR,"div.confirmation_bikes div.confirmation_bikes-box")
        self.firstBike = (By.XPATH,"//div[@class='my19-container bigger']//img[1]")
        # Locale dealer
        self.dealerMap =(By.ID,"searchTextField")
        # map
        self.mapDetailMessage=(By.CSS_SELECTOR,"div.map_info-container")
        # first dealer
        self.chooseDealerList = (By.CSS_SELECTOR,".pac-container.pac-logo .pac-item")
        # title
        self.chooseTitle = (By.XPATH,"//*[@name='Title']")
        # firstTitle
        self.chooseFirstTitle = (By.XPATH,"//*[@name='Title']/option[2]")
        # first name
        self.firstName = (By.XPATH,"//*[@name='FirstName']")
        # last name
        self.lastName = (By.XPATH,"//*[@name='LastName']")
        # Email
        self.email = (By.XPATH, "//*[@name='Email']")
        # MOBILE
        self.phone = (By.XPATH, "//*[@name='Phone']")
        # POSTCODE
        self.postCode = (By.XPATH, "//*[@name='Postcode']")
        #Date
        self.dateDD = (By.CSS_SELECTOR,".small:nth-child(1)")
        self.dateYYYY = (By.CSS_SELECTOR,".small:nth-child(3)")
        self.dateYear = (By.CSS_SELECTOR,".middle")
        # own a motorcycle->Yes
        self.motorcycleYes = (By.CSS_SELECTOR,".common_sections:nth-child(11) .common_form-label:nth-child(1) .common_form-inner-box")
        # brandSelect
        self.brandSelect = (By.CSS_SELECTOR,"select[name=VehicleOwned]")
        # full motorcycle licence->Yes
        self.fullMatorcycle = (By.CSS_SELECTOR,".common_sections:nth-child(12) .common_form-radio-container .common_form-label:nth-child(1) .common_form-inner-box")
        # via Email
        self.viaEmail = (By.CSS_SELECTOR,".horilized > .common_form-label:nth-child(1) .common_form-inner-box")
        # via phone
        self.viaPhone = (By.CSS_SELECTOR,".horilized > .common_form-label:nth-child(2) .common_form-inner-box")
        # via POST
        self.viaPost = (By.CSS_SELECTOR,".common_form-label:nth-child(3) .common_form-inner-box")
        # error message when form is empty
        self.errorMessage = (By.CSS_SELECTOR,"p.error")
        self.errorMessage_checkbox=(By.CSS_SELECTOR,"div.error")
        # Request Test Ride button
        self.requestTestRideButton = (By.CSS_SELECTOR,".common_confirm-btn")

        #menu&footer
        #footer <a>
        self.footerIconHrefs=(By.CSS_SELECTOR,"div.footer_icon-container a[target='_blank']")