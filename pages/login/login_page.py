from appium.webdriver.common.mobileby import MobileBy

import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    USERNAME_INPUT = (MobileBy.ID, 'com.example.myloginapp:id/username')
    PASSWORD_INPUT = (MobileBy.ID, 'com.example.myloginapp:id/password')
    LOGIN_BUTTON = (MobileBy.ID, 'com.example.myloginapp:id/loginbtn')
    LOGOUT_BUTTON = (MobileBy.ID, 'com.example.myloginapp:id/logout')

    def fill_username(self, email):
        self.fill_input(self.USERNAME_INPUT, email)
        time.sleep(2)
        return self

    def fill_password(self, password):
        self.fill_input(self.PASSWORD_INPUT, password)
        time.sleep(2)
        return self

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(2)
        return self

    def verify_logout_button(self):
        self.verify_element(self.LOGOUT_BUTTON)
        time.sleep(2)
        return self
