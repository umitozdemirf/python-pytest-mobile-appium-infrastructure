from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

desired_caps = {
    "deviceName": "Galaxy S20",
    "deviceId": "emulator-5554",
    "platformName": "Android",
    "app": "/Users/umitozdemir/Desktop/app-debug.apk",  # Enter app_url here
    "build": "Python Vanilla Android",
    "name": "Sample Test - Python",
    "network": True,
    "visual": True,
    "video": True
}


def startingTest():
    driver = webdriver.Remote(
        command_executor="http://localhost:4723/wd/hub",
        desired_capabilities=desired_caps
    )
    yield driver
    colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
    colorElement.click()

    textElement = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))
    textElement.click()

    toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
    toastElement.click()

    notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
    notification.click()

    geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
    geolocation.click()
    time.sleep(5)

    driver.back()

    home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
    home.click()

    speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
    speedTest.click()
    time.sleep(5)

    driver.back()

    browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/webview")))
    browser.click()

    url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/url")))
    url.send_keys("https://www.lambdatest.com")

    find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (MobileBy.ID, "com.lambdatest.proverbial:id/find")))
    find.click()
    driver.quit()


startingTest()
