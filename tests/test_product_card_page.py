from page_objects.ProductCardPage import ProductCardPage

""" Тесты страницы карточки товара """


def test_product_card_page(browser):
    """
    Проверка видимости элементов на странице карточки товара
    """
    page = ProductCardPage(browser)
    page.open_page(browser)
    page.check_elements_on_product_card_page()
