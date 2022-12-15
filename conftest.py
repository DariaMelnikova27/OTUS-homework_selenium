import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--driver_folder", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--url", action="store", default="http://192.168.0.102:8081")
    parser.addoption("--status_code", default="200", type=int)


@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    driver_folder = request.config.getoption("--driver_folder")
    driver = None
    url = request.config.getoption("--url")

    if _browser == "firefox" or _browser == "ff":
        options = FirefoxOptions()
        driver = webdriver.Firefox(
            executable_path=f"{driver_folder}{os.sep}geckodriver", options=options
        )
    elif _browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(
            options=options, executable_path=f"{driver_folder}{os.sep}chromedriver"
        )
    elif _browser == "edge":
        options = EdgeOptions()
        driver = webdriver.Edge(
            executable_path=f"{driver_folder}{os.sep}msedgedriver", options=options
        )
    elif _browser == "yandex":
        options = ChromeOptions()
        driver = webdriver.Chrome(
            executable_path=f"{driver_folder}{os.sep}yandexdriver", options=options
        )
    elif _browser == "safari":
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
