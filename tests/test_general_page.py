import allure
import pytest
from allure_commons.types import Severity
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.GeneralPage import GeneralPage

""" Тесты главной страницы """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на главной странице')
@allure.title('Проверка видимости элементов на главной странице')
def test_general_page(browser):
    page = GeneralPage(browser)
    page.open_page(browser)
    page.check_elements_on_general_page()


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на главной странице')
@allure.title('Переключение валют из верхнего меню опенкарта')
@pytest.mark.parametrize(
    "currency",
    ["EUR", "GBP", "USD"]
)
def test_currency_switching(browser, currency):
    page = GeneralPage(browser)
    page.open_page(browser)
    page.currency_switching(currency)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency strong")))
