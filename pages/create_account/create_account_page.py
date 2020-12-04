####################################################
# Objects on the SignIn page and Actions with them
####################################################

import logging
import time

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver
from utilities.generate_random_string import randomWord as random


class CreateAccountPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # TEST ACCOUNT
    email = random(5) + "@mail.com"
    password = 123321
    firstName = "Duffy"
    lastName = "Smith"
    address = "123 West Oak Rd"
    city = "Sunnyvale"
    zipCode = 77777
    mobilePhone = 8329999999
    addressAlias = "ShoppingAddress"

    # LOCATORS

    # CREATE AN ACCOUNT
    _email_create_account = "#email_create"  # CSS
    _create_account_button = "//button[@id='SubmitCreate']"  # XPATH
    _label_YourPersonalInformation = "//h3[contains(text(),'Your personal information')]"  # xpath

    # PERSONAL INFORMATION
    _first_name = "//input[@id='customer_firstname']"  # xpath
    _last_name = "//input[@id='customer_lastname']"  # xpath
    _password = "//input[@id='passwd']"  # xpath

    # YOUR ADDRESS -> All XPATH
    _address = "//input[@id='address1']"
    _city = "//input[@id='city']"
    _state_dropdown = "//select[@id='id_state']"
    _state_value = "//option[contains(text(),'California')]"
    _zip = "//input[@id='postcode']"
    _mobile_phone = "//input[@id='phone_mobile']"
    _address_alias = "//input[@id='alias']"

    _register_button = "//button[@id='submitAccount']"

    # ACCOUNT HOME PAGE
    _order_history_button = "//span[contains(text(),'Order history and details')]"

    # ACTIONS WITH PAGE OBJECTS

    #     def waitForHomePageToLoad(self):
    #         self.waitForElement()

    def enterCreateAccountEmail(self):
        self.getElement(self._email_create_account, "css")
        self.sendKeys(self.email, self._email_create_account, "css")
        time.sleep(5)

    def clickCreateAccount(self):
        self.elementClick(self._create_account_button, "xpath")
        time.sleep(5)

    # Verifies the account page is loaded
    def verifyCreateAccountPageLoads(self):
        self.waitForElement(self._label_YourPersonalInformation, "xpath")
        result = self.isElementPresent(self._label_YourPersonalInformation, "xpath")
        return result

    # Enters all account data
    def enterNewAccountInfo(self):
        self.sendKeys(self.firstName, self._first_name, "xpath")
        time.sleep(2)
        self.sendKeys(self.lastName, self._last_name, "xpath")
        time.sleep(2)
        self.sendKeys(self.password, self._password, "xpath")
        time.sleep(2)
        self.sendKeys(self.address, self._address, "xpath")
        time.sleep(2)
        self.sendKeys(self.city, self._city, "xpath")
        time.sleep(2)
        self.selectElementFromDropdown(self._state_dropdown, "xpath", "index", "5")
        time.sleep(2)
        self.sendKeys(self.zipCode, self._zip, "xpath")
        time.sleep(2)
        self.sendKeys(self.mobilePhone, self._mobile_phone, "xpath")
        time.sleep(2)
        self.clearTextBoxByXPATH(self._address_alias)
        time.sleep(2)
        self.sendKeys(self.addressAlias, self._address_alias, "xpath")

    # press the Register button to create new account
    def pressRegisterNewAccount(self):
        self.elementClick(self._register_button, "xpath")

    # Verifies if the account is created by checking for the order history object
    def verifyAccountIsCreated(self):
        result = self.isElementPresent(self._order_history_button, "xpath")
        return result
