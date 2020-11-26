from pages.home import home_page
from pages.signin import signinpage
from pages.create_account import create_account_page
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SigninTests(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    #Class Level Setup definig the lp object for the NavigationPage class
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = home_page.HomePage(self.driver)
        self.sip = signinpage.SignInPage(self.driver)
        self.cap = create_account_page.CreateAccountPage(self.driver)

# TEST CASES:
    @pytest.mark.run(order=5)
    def test_Go_To_SignIn_Page(self):
        self.sip.clickSignInLink()
        result = self.sip.verifySignInPageIsLoaded()
        assert result == True
        if result == True:
            self.log.info("The \"" + self.hp.getTitle() + "\" page has loaded successfully!" )
        else:
            self.log.error("The \"" + self.hp.getTitle() + "\" page did not load successfully!")

    @pytest.mark.run(order=6)
    def test_Login_To_Account(self):
        self.sip.enterLoginEmail()
        self.sip.enterLoginPassword()
        self.sip.clickLoginButton()
        result = self.sip.verifySuccessfulLogin()
        assert result == True
        if result == True:
            self.log.info("The login was successful!" )
        else:
            self.log.error("The login was not successful")


    @pytest.mark.run(order=7)
    def test_Logout_From_Account(self):
        self.sip.logOut()
        result = self.sip.verifySuccessfulLogOut()
        assert result == True
        if result == True:
            self.log.info("The login was successful!" )
        else:
            self.log.error("The login was not successful")

        #self.driver.quit()
