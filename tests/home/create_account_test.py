from pages.home import home_page
from pages.signin import signinpage
from pages.create_account import create_account_page
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CreateAccountTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    #Class Level Setup initializing the object for all test classes
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = home_page.HomePage(self.driver)
        self.sip = signinpage.SignInPage(self.driver)
        self.cap = create_account_page.CreateAccountPage(self.driver)

# TEST CASES:
    @pytest.mark.run(order=1)
    def test_Go_To_SignIn_Page(self):
        self.sip.clickSignInLink()
        result = self.sip.verifySignInPageIsLoaded()
        assert result == True
        if result == True:
            self.log.info("The \"" + self.hp.getTitle() + "\" page has loaded successfully!" )
        else:
            self.log.info("The \"" + self.hp.getTitle() + "\" page did not load successfully!")


    @pytest.mark.run(order=2)
    def test_Enter_New_Account_Email(self):
        self.cap.enterCreateAccountEmail()
        self.cap.clickCreateAccount()
        result = self.cap.verifyCreateAccountPageLoads()
        assert result == True
        if result == True:
            self.log.info("The \"" + self.hp.getTitle() + "\" page has loaded successfully!" )
        else:
            self.log.info("The \"" + self.hp.getTitle() + "\" page did not load successfully!")
        time.sleep(10)

    @pytest.mark.run(order=3)
    def test_Register_New_Account(self):
        self.cap.enterNewAccountInfo()
        time.sleep(2)
        self.cap.pressRegisterNewAccount()
        time.sleep(2)
        result = self.cap.verifyAccountIsCreated()
        assert result == True
        if result == True:
            self.log.info("The new account is created successfully!")
        else:
            self.log.error("Failed to create new account!")
        time.sleep(2)

    @pytest.mark.run(order=4)
    def test_Logout_From_Account(self):
        self.sip.logOut()
        result = self.sip.verifySuccessfulLogOut()
        assert result == True
        if result == True:
            self.log.info("The log out was successfull!")
        else:
            self.log.error("Log out failed!")
        time.sleep(2)
        self.driver.quit()
