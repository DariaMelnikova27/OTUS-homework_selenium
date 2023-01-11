import allure
from allure_commons.types import Severity
from page_objects.ProductCardPage import ProductCardPage

""" Тесты страницы карточки товара """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на странице карточки товара')
@allure.title('Проверка видимости элементов на странице карточки товара')
def test_product_card_page(browser):
    page = ProductCardPage(browser)
    page.open_page(browser)
    page.check_elements_on_product_card_page()
