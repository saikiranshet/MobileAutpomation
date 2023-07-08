from ScreenObjects.locators import locators
from Tests import conftest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class Login(object):

    def setEmailId(self,setUp):
        self.EmailId = setUp.find_element(AppiumBy.ID,locators.email).send_keys("SAI")

    def setPassword(self,setUp):
        self.password = setUp.find_element(AppiumBy.ID, locators.password).send_keys("KIRAN")

    def clickLogin(self,setUp):
        self.loginButton.click()
    def MainScreenLoginClick(self,setUp):
        self.loginMainScreen = setUp.find_element(AppiumBy.ID,locators.LoginMainScreen).click()
