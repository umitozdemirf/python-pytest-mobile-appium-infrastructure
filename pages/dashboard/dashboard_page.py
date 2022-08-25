from appium.webdriver.common.mobileby import MobileBy

from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    LOGOUT_BUTTON = (MobileBy.ID, 'com.example.myloginapp:id/logout')

    def verify_logout_button(self):
        self.verify_element(self.LOGOUT_BUTTON)
        return self
