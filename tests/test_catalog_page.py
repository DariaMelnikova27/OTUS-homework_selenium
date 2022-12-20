from page_objects.CatalogPage import CatalogPage

""" Тесты страницы каталога """


def test_catalog_page(browser):
    """
    Проверка видимости элементов на странице каталога
    """
    page = CatalogPage(browser)
    page.open_page(browser)
    page.check_elements_on_catalog_page()
