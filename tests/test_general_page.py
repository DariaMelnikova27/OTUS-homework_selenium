import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.GeneralPage import GeneralPage

""" Тесты главной страницы """


def test_general_page(browser):
    """
    Проверка видимости элементов на главной странице
    """
    page = GeneralPage(browser)
    page.open_page(browser)
    page.check_elements_on_general_page()


@pytest.mark.parametrize(
    "currency",
    ["EUR", "GBP", "USD"]
)
def test_currency_switching(browser, currency):
    """
    Переключение валют из верхнего меню опенкарта
    """
    page = GeneralPage(browser)
    page.open_page(browser)
    page.currency_switching(currency)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency strong")))
