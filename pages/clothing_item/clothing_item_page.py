################################
# Objects on the cloth item page
################################

import logging

import utilities.custom_logger as cl
from base.selenium_driver import SeleniumDriver


class ClothingItemPage(SeleniumDriver):
    # Create logger class instance
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # OBJECTS' LOCATORS
    _cart_empty_verification_object = "//span[contains(text(),'(empty)')]"  # xpath
    _add_to_cart_button = "//span[contains(text(),'Add to cart')]"  # xpath
    _blouse_item_link = "//a[@class='product-name' and @title='Blouse']"  # xpath
    _verify_cart_content = "//span[contains(text(),'There is 1 item in your cart.')]"  # xpath
    _proceed_button_in_cart = "//div[@class='button-container']//i[@class='icon-chevron-right right']"  # xpath
    _verify_cart_summary = "//span[@id='total_price' and contains(text(),'$29.00')]"  # xpath
    _proceed_button_cart_summary = "//a[@class='button btn btn-default standard-checkout button-medium']"  # xpath
    _verify_address_page_loads = "//h1[contains(text(),'Addresses')]"  # xpath
    _confirm_address = "//button[@name='processAddress']"  # xpath
    _terms_of_service = "//input[@id='cgv']"  # xpath
    _confirm_delivery_button = "//button[@name='processCarrier']"
    _payment_type = "//a[@class='bankwire']"  # xpath
    _confirm_payment_button = "//button[@class='button btn btn-default button-medium']"  # xpath
    _verify_order_is_complete = "//strong[contains(text(),'Your order on My Store is complete.')]"  # xpath

    # ACTIONS WITH PAGE OBJECTS

    def openItem(self):
        self.elementClick(self._blouse_item_link, "xpath")

    def addToCart(self):
        self.elementClick(self._add_to_cart_button, "xpath")

    def verifyCartContent(self):
        result = self.isElementPresent(self._verify_cart_content, "xpath")
        return result

    def proceedToCartSummary(self):
        self.elementClick(self._proceed_button_in_cart, "xpath")

    def verifyCartSummary(self):
        result = self.isElementPresent(self._verify_cart_summary, "xpath")
        return result

    def pressButtonProceedInCartSummary(self):
        self.elementClick(self._proceed_button_cart_summary, "xpath")

    def verifyAddressesPageLoads(self):
        result = self.isElementPresent(self._verify_address_page_loads, "xpath")
        return result

    def pressButtonConfirmInAddress(self):
        self.elementClick(self._confirm_address, "xpath")

    def placeCheckForToS(self):
        self.elementClick(self._terms_of_service, "xpath")

    def pressCheckoutButtonInShipping(self):
        self.elementClick(self._confirm_delivery_button, "xpath")

    def selectPaymentType(self):
        self.elementClick(self._payment_type, "xpath")

    def confirmOrder(self):
        self.elementClick(self._confirm_payment_button, "xpath")

    def verifyOrderIsComplete(self):
        result = self.isElementPresent(self._verify_order_is_complete, "xpath")
        return result
