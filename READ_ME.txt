Required tools to run the test suite:

1. Download Chrome WebDriver based on you browser version:
https://chromedriver.chromium.org/downloads 
2. Save the driver to a location of your choice and add its path to the SYSTEM environment variables PATH. 

2. Install latest Python realease(I've used 3.8.2).

3. Install latest selenium package. 

4. Install the pytest package. 

5. Install the pytest-html package


To run the test suite, be at the roo project level and run:  

py.test -s -v tests/test_sanity_suite.py --html=report.html

The testrun will produce: 
automation_log
report.html