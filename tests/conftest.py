import pytest
from selenium import webdriver
from base.web_driver_generator import WebDriverFactory
import logging
import utilities.custom_logger as cl

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser='chrome'):
    global driver
    log = cl.customLogger(logging.DEBUG)
    #log.info("***********************STARTING TEST RUN*****************************")
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("Running one time tearDown")
    driver.quit()
    #log.info("*********************** TEST RUN END *****************************")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")