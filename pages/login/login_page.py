from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    USERNAME_INPUT = (MobileBy.ID, 'com.example.myloginapp:id/username')
    PASSWORD_INPUT = (MobileBy.ID, 'com.example.myloginapp:id/password')
    LOGIN_BUTTON = (MobileBy.ID, 'com.example.myloginapp:id/loginbtn')
    MESSAGE_LABEL = (MobileBy.ID, 'com.example.myloginapp:id/warningMessage')
    LOGOUT_BUTTON = (MobileBy.ID, 'com.example.myloginapp:id/logout')

    def fill_username(self, email):
        self.fill_input(self.USERNAME_INPUT, email)
        return self

    def fill_password(self, password):
        self.fill_input(self.PASSWORD_INPUT, password)
        return self

    def click_login_button(self):
        self.click_element(self.LOGIN_BUTTON)
        return self

    def verify_error_message(self, message):
        self.verify_element_text(self.MESSAGE_LABEL, message)
        return self
