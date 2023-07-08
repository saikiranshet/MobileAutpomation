import sys
import time
import pytest
from appium import webdriver
from conftest import setUp
sys.path.append("/")
from appium.webdriver.common.appiumby import AppiumBy
# from ScreenObjects.mainScreen import MainScreen
# from appium.webdriver.appium_service import AppiumService
# from selenium.webdriver.common import keys
from ScreenObjects.login import Login

# appium_service = AppiumService()
# appium_service.start()
class Test_Appium:

    def test_s1(self,setUp):
        # eld_id = setUp.find_element(AppiumBy.ID,"LoginMainScreen").click()
        # time.sleep(5)
        # eld_id2 = setUp.find_element(AppiumBy.ID,"com.code2lead.kwad:id/Et1").send_keys("SAI")
        # eld_id3 = setUp.find_element(AppiumBy.ID,"com.code2lead.kwad:id/Btn1").click()
        Login.MainScreenLoginClick(self,setUp)
        time.sleep(5)
        Login.setEmailId(self,setUp)
        Login.setPassword(self,setUp)
        # Login.clickLogin(self,setUp)
