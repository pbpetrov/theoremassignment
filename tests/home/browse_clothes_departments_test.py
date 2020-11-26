from pages.home import home_page
from pages.signin import signinpage
from pages.create_account import create_account_page
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BrowseClothesDepartments(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    #Class Level Setup definig the lp object for the NavigationPage class
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = home_page.HomePage(self.driver)
        self.sip = signinpage.SignInPage(self.driver)
        self.cap = create_account_page.CreateAccountPage(self.driver)

# TEST CASES:
    @pytest.mark.run(order=8)
    def test_Browse_Women(self):
        self.sip.clickSignInLink()
        self.sip.enterLoginEmail()
        self.sip.enterLoginPassword()
        self.sip.clickLoginButton()
        self.hp.clickWomen()
        result = self.hp.verifyWomenPageLoadsSuccessfully()
        assert result == True
        if result == True:
            self.log.info("The \"Women\" section loads successfully!")
        else:
            self.log.error("The \"Women\" section fails to load!")

    @pytest.mark.run(order=9)
    def test_Browse_Dresses(self):
        self.hp.clickDresses()
        result = self.hp.verifyDressesPageLoadsSuccessfully()
        assert result == True
        if result == True:
            self.log.info("The \"Dresses\" section loads successfully!")
        else:
            self.log.error("The \"Dresses\" section fails to load!")

    @pytest.mark.run(order=10)
    def test_Browse_TShirts(self):
        self.hp.clickTshirts()
        result = self.hp.verifyTShirtsPageLoadsSuccessfully()
        assert result == True
        if result == True:
            self.log.info("The \"T-shirts\" section loads successfully!")
        else:
            self.log.error("The \"T-shirts\" section fails to load!")

    @pytest.mark.run(order=11)
    def test_searchItem(self):
        self.hp.searchForItem()
        time.sleep(10)
        result1 = self.hp.verifySearchResult_1()
        result2 = self.hp.verifySearchResult_2()
        assert (result1 == True and result2 == True)
        if (result1 == True and result2 == True):
            self.log.info("The search returns correct result!")
        else:
            self.log.error("The search result is incorrect!")