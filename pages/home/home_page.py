############################
# Objects on the home page
############################

from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging

class HomePage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# SEARCH STRING
    _search_string = "Blouse"

# LOCATORS
    _cart_link = "//b[contains(text(),'Cart')]" # xpath
    _women_link = "Women" # link
    _dresses_link = "Dresses" # link
    _t_shirts_link = "//div[@id='block_top_menu']//li[3]/a[@title='T-shirts']" # link
    _search_txt_box = "//input[@id='search_query_top']" # xpath
    _search_button = "//span[contains(text(),'Search')]" # xpath
    _search_result1 = "//div[@class='top-pagination-content clearfix']//div[contains(text(),'Showing 1 - 1 of 1 item')]" # xpath
    _search_result2 = "//a[@title='Blouse' and contains(text(),'Blouse')]" #xpath

# ACTIONS WITH PAGE OBJECTS

    def clickWomen(self):
        self.elementClick(self._women_link, locatorType="link")
        time.sleep(2)

    def verifyWomenPageLoadsSuccessfully(self):
        title = self.getTitle()
        if title == "Women - My Store":
            return True
        else:
            return False

    def clickDresses(self):
        self.elementClick(self._dresses_link, locatorType="link")
        time.sleep(2)

    def verifyDressesPageLoadsSuccessfully(self):
        title = self.getTitle()
        if title == "Dresses - My Store":
            return True
        else:
            return False

    def clickTshirts(self):
        self.elementClick(self._t_shirts_link, locatorType="xpath")
        time.sleep(2)

    def verifyTShirtsPageLoadsSuccessfully(self):
        title = self.getTitle()
        if title == "T-shirts - My Store":
            return True
        else:
            return False

    def clickCartLink(self):
        self.elementClick(self._cart_link, locatorType="xpath")

    # def enterDressSearchString(self):
    #     self.sendKeys(self._search_string_dress, self._search_txt_box, "xpath")
    #
    # def enterWomenSearchString(self):
    #     self.sendKeys(self._search_string_women, self._search_txt_box, "xpath")
    #
    # def enterTshirtsSearchString(self):
    #     self.sendKeys(self._search_string_tshirt, self._search_txt_box, "xpath")

    def searchForItem(self):
        self.sendKeys(self._search_string, self._search_txt_box, "xpath")
        self.sendEnterKey(self._search_txt_box, "xpath")

    def verifySearchResult_1(self):
        result1 = self.isElementPresent(self._search_result1, "xpath")
        return result1

    def verifySearchResult_2(self):
        result2 = self.isElementPresent(self._search_result2, "xpath")
        return result2