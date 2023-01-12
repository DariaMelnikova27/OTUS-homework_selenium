import allure
from allure_commons.types import Severity
from page_objects.CatalogPage import CatalogPage

""" Тесты страницы каталога """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на странице каталога')
@allure.title('Проверка видимости элементов на странице каталога')
def test_catalog_page(browser):
    page = CatalogPage(browser)
    page.open_page(browser)
    page.check_elements_on_catalog_page()
