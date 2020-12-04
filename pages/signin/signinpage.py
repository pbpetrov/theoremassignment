#############################
# Objects on the SignIn pages
#############################

import logging

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class SignInPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # TEST ACCOUNT
    email = "test_abc@mail.com"
    password = "123321"

    # LOCATORS
    _sign_in_link = "//a[contains(text(),'Sign in')]"  # xpath
    _login_email = "#email"  # css
    _login_pass = "#passwd"  # css
    _login_button = "//button[@id='SubmitLogin']"  # xpath
    _user_order_history = "//span[contains(text(),'Order history and details')]"  # xpath
    _sign_out_link = "Sign out"  # link

    # ACTIONS WITH PAGE OBJECTS

    def clickSignInLink(self):
        self.elementClick(self._sign_in_link, "xpath")

    def verifySignInPageIsLoaded(self):
        page_title = self.getTitle()
        if page_title == "Login - My Store":
            return True
        else:
            return False

    def enterLoginEmail(self):
        self.sendKeys(self.email, self._login_email, "css")

    def enterLoginPassword(self):
        self.sendKeys(self.password, self._login_pass, "css")

    def clickLoginButton(self):
        self.elementClick(self._login_button, "xpath")

    def verifySuccessfulLogin(self):
        result = self.isElementPresent(self._user_order_history, "xpath")
        return result

    def logOut(self):
        self.elementClick(self._sign_out_link, "link")

    def verifySuccessfulLogOut(self):
        result = self.isElementPresent(self._sign_in_link, "xpath")
        return result
