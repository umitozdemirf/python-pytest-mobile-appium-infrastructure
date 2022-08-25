"""Configuration for pytest runner."""

import pytest
import yaml

from appium import webdriver

from config.base_config import BaseConfig

pytest_plugins = 'pytester'

with open("/Users/umitozdemir/Proj/FireFly/firefly-mobil-aut/platform/app_android.yml", "r") as stream:
    try:
        desired_caps = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


@pytest.fixture(scope='function')
def init_driver(request):
    driver = webdriver.Remote(
        command_executor=desired_caps['appium_lib']['server_url'],
        desired_capabilities=desired_caps['caps']
    )
    request.cls.driver = driver
    yield driver
    driver.quit()
