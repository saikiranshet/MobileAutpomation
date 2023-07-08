import pytest
import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture(scope="module",autouse=True)
def setUp():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '13'
    desired_caps['deviceName'] = 'a52qnsxx'
    desired_caps['appPackage'] = 'com.code2lead.kwad'
    desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver

@pytest.fixture(scope="module",autouse=True)
def tearDown(setUp):
    yield
    setUp.driver.quit()

