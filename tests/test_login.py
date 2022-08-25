import pytest
from config.account.account_config import AccountConfig as account
from pages.login.login_page import LoginPage

from pages.login.login_page import LoginPage


@pytest.mark.usefixtures('init_driver')
class TestProducts:
    """Products tests - """

    @pytest.mark.smoke
    def test_login(self):
        login_page = LoginPage(self.driver)

        login_page.fill_username(account.USERNAME) \
            .fill_password(account.PASSWORD) \
            .click_login_button() \
            .verify_logout_button()

