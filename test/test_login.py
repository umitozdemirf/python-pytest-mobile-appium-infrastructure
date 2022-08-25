import pytest

from config.account.account_config import AccountConfig as account
from resources.validation import Validation as validation

from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage

from utils.data.data_generator import DataGenerator as generator


@pytest.mark.usefixtures('init_driver')
class TestProducts:
    """Products test - """

    @pytest.mark.regression
    def test_login_case1(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        login_page.fill_username(account.USERNAME) \
            .fill_password(account.PASSWORD) \
            .click_login_button()
        dashboard_page.verify_logout_button()

    @pytest.mark.regression
    def test_login_case2(self):
        login_page = LoginPage(self.driver)

        login_page.click_login_button() \
            .verify_error_message(validation.BLANK_VALUE_MESSAGE)

    @pytest.mark.regression
    def test_login_case3(self):
        login_page = LoginPage(self.driver)

        login_page.fill_username(generator.generate_random_string()) \
            .fill_password(generator.generate_random_string()) \
            .click_login_button() \
            .verify_error_message(validation.EMAIL_FORMAT_MESSAGE)

    @pytest.mark.regression
    def test_login_case4(self):
        login_page = LoginPage(self.driver)

        login_page.fill_username(generator.generate_email()) \
            .fill_password(generator.generate_random_integer(1, 1000)) \
            .click_login_button() \
            .verify_error_message(validation.INCORRECT_PASSWORD_MESSAGE)

    @pytest.mark.regression
    def test_login_case5(self):
        login_page = LoginPage(self.driver)

        login_page.fill_username(generator.generate_email()) \
            .fill_password(generator.generate_random_string()) \
            .click_login_button() \
            .verify_error_message(validation.INCORRECT_LOGIN_MESSAGE)

    @pytest.mark.regression
    def test_login_case6(self):
        login_page = LoginPage(self.driver)

        login_page.fill_username(generator.generate_special_character_email()) \
            .fill_password(generator.generate_random_string()) \
            .click_login_button() \
            .verify_error_message(validation.INCORRECT_LOGIN_MESSAGE)
