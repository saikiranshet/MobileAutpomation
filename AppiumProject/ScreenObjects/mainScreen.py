from ScreenObjects import locators
from appium.webdriver.common.appiumby import AppiumBy

class MainScreen(object):
    def __init__(self,setUp):
        self.value = setUp.find_element(AppiumBy.ID,locators.EnterSomeValue)

    def openthatSomevalue(self):
        self.value.click()