##############################################
#
# This class will provide help methods based
# on the generic SeleniumWebDriver methods
#
##############################################

from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class SeleniumDriver():
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    #   Returns the type of locator for use with BY
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    # Finds the object by locator and locator type;
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locatorType)
        except:
            self.log.error("Element not found with locator: " + locator + " and locator type: " + locatorType)
        return element

    # Finds object by locator and locator type and clicks on it;
    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            # print_stack()

    # returns the title of the current page
    def getTitle(self):
        return self.driver.title

    # Select element from dropdown
    def selectElementFromDropdown(self, locator, locatorType, dropDownAttributeType, value):
        element = self.getElement(locator, locatorType)
        sel = Select(element)
        dropDownAttributeType.lower()
        if dropDownAttributeType == "value":
            sel.select_by_value(value)
            time.sleep(2)
        elif dropDownAttributeType == "index":
            sel.select_by_index(value)
            time.sleep(2)
        elif dropDownAttributeType == "text":
            sel.select_by_visible_text(value)
            time.sleep(2)
        elif dropDownAttributeType == "index":
            sel.select_by_index(value)
            time.sleep(2)

    # creates screenshot
    def getScreenshot(self):
        filename = str(round(time.time())) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFilename = screenshotDirectory + filename
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFilename)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationFile)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory: " + destinationFile)
        except:
            self.log.error("Exception Occurred")
            # print_stack()

    # Finds object by locator and locator type and types in it;
    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sending " + data + " to element with locator " + locator)
            # self.log.info("Sent data to element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data to the element with locator: " + locator + " locatorType: " + locatorType)
            # print_stack()

    # Finds object by locator and locator type and types in it;
    def sendEnterKey(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(Keys.ENTER)
            self.log.info("Pressed ENTER for " + " element with locator " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot press enter for element with locator: " + locator + " locatorType: " + locatorType)
            # print_stack()

    # Checks if the element is loaded
    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                return True
            else:
                return False
        except:
            return False

    # waits for an element to become available
    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element not appeared on the web page")
            # print_stack()
        return element

    # Hovers over an object and clicks on a child object
    def mouseHovering(self, hooverLocator, hooverLocatorType, itemToClickLocator, itemToClickLocatorType):
        element = self.driver.find_element(hooverLocator, hooverLocatorType)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Mouse Hovered on element with locator: \"" + hooverLocator + "\"")
            time.sleep(2)
            topLink = self.driver.find_element(itemToClickLocatorType, itemToClickLocator)
            actions.move_to_element(topLink).click().perform()
            self.log.info("Clicked on Item with locator: \"" + itemToClickLocator + "\"")
        except:
            self.log.error("Clicked failed on Item with locator: \"" + itemToClickLocator + "\"")
            self.log.error("Mouse Hover failed on element with locator: \"" + hooverLocator + "\"")

    # Clears a text box
    def clearTextBoxByXPATH(self, locator):
        self.driver.find_element(By.XPATH, locator).clear()
