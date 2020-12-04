############################################################
# @package base
# WebDriver Generator class implementation
# It creates a WebDriver instance based on browser choice
# Note: Currently only Chrome is supported!!!
############################################################
from selenium import webdriver
from configfiles.environmentSettings import WebSiteUnderTest as wut


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        #       Get WebDriver Instance based on the browser configuration
        baseURL = wut.baseURL
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            raise Exception("Configure your browser in base/web_driver_generator.py")

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
