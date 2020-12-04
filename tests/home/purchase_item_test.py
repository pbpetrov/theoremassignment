from pages.home import home_page
from pages.signin import signinpage
from pages.create_account import create_account_page
from pages.clothing_item import clothing_item_page
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PurchaseItemTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    #   Class Level Setup defining the lp object for the NavigationPage class
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = home_page.HomePage(self.driver)
        self.sip = signinpage.SignInPage(self.driver)
        self.cap = create_account_page.CreateAccountPage(self.driver)
        self.cip = clothing_item_page.ClothingItemPage(self.driver)

    # TEST CASES:
    @pytest.mark.run(order=12)
    def test_Add_Item_To_Cart(self):
        self.sip.clickSignInLink()
        self.sip.enterLoginEmail()
        self.sip.enterLoginPassword()
        self.sip.clickLoginButton()
        self.hp.searchForItem()
        self.cip.openItem()
        self.cip.addToCart()
        result = self.cip.verifyCartContent()
        assert result == True
        if result:
            self.log.info("The cart content is correct.")
        else:
            self.log.error("The cart content is not correct")

    @pytest.mark.run(order=13)
    def test_View_Cart_Summary(self):
        self.cip.proceedToCartSummary()
        result = self.cip.verifyCartSummary()
        assert result == True
        if result:
            self.log.info("The cart summary/total price is correct")
        else:
            self.log.error("The cart summary/total price is not correct")

    @pytest.mark.run(order=14)
    def test_GoToConfirmAddress(self):
        self.hp.driver.execute_script("window.scrollBy(0, 1000);")
        self.cip.pressButtonProceedInCartSummary()
        result = self.cip.verifyAddressesPageLoads()
        assert result == True
        if result:
            self.log.info("The address page is loaded.")
        else:
            self.log.error("The address page does not load!")

    @pytest.mark.run(order=15)
    def test_CompleteTheOrder(self):
        self.cip.pressButtonConfirmInAddress()
        self.cip.placeCheckForToS()
        self.cip.pressCheckoutButtonInShipping()
        self.cip.selectPaymentType()
        self.cip.confirmOrder()
        result = self.cip.verifyOrderIsComplete()
        assert result == True
        if result:
            self.log.info("The Order is placed successfully.")
        else:
            self.log.error("The Order is NOT places successfully!")