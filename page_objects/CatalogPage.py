from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    """ Класс страницы каталога """
    page_url = "/index.php?route=product/category&path=20"

    GRID_VIEW_BUTTON = (By.ID, "grid-view")
    LIST_VIEW_BUTTON = (By.ID, "list-view")
    MENU = (By.CSS_SELECTOR, ".list-group")
    SORT_FIELD = (By.CSS_SELECTOR, "#input-sort")
    BANNER = (By.CSS_SELECTOR, ".swiper-wrapper")

    def check_elements_on_catalog_page(self):
        """
        Метод проверки видимости элементов на странице каталога
        """
        self._find_element(CatalogPage.GRID_VIEW_BUTTON)
        self._find_element(CatalogPage.LIST_VIEW_BUTTON)
        self._find_element(CatalogPage.MENU)
        self._find_element(CatalogPage.SORT_FIELD)
        self._find_element(CatalogPage.BANNER)
