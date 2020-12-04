import pytest
from base.web_driver_generator import WebDriverFactory


@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser='chrome'):
    global driver
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("Running one time tearDown")
    driver.quit()


def addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
