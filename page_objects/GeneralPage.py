from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class GeneralPage(BasePage):
    """ Класс главной страницы"""
    page_url = ""

    WISHLIST = (By.CSS_SELECTOR, "#wishlist-total")
    LOGO = (By.ID, "logo")
    MACBOOK = (By.LINK_TEXT, "MacBook")
    SWIPER = (By.CLASS_NAME, "swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")
    ABOUT_US = (By.LINK_TEXT, "About Us")
    CURRENCY_BTN = (By.CSS_SELECTOR, 'button.btn.btn-link.dropdown-toggle')
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "#top .btn-group .dropdown-menu")
    EURO = (By.NAME, "EUR")
    POUND = (By.NAME, "GBP")
    USD = (By.NAME, "USD")
    CURRENCY_VALUE = (By.CSS_SELECTOR, "#form-currency strong")

    def check_elements_on_general_page(self):
        """
        Метод проверки видимости элементов на главной странице
        """
        self._find_element(GeneralPage.WISHLIST)
        self._find_element(GeneralPage.LOGO)
        self._find_element(GeneralPage.MACBOOK)
        self._find_element(GeneralPage.SWIPER)
        self._find_element(GeneralPage.ABOUT_US)

    def get_currency(self):
        """
        Метод получения текущей выбранной валюты
        """
        return self.element(self.CURRENCY_VALUE)

    def currency_switching(self, name):
        """
        Метод переключения валют из верхнего меню опенкарта
        """
        self.click(self.element(self.CURRENCY_BTN))
        self.element(self.CURRENCY_DROPDOWN)
        if name == "EUR":
            self.click(self.element(self.EURO))
        elif name == "GBP":
            self.click(self.element(self.POUND))
        elif name == "USD":
            self.click(self.element(self.USD))
        else:
            raise AssertionError(f"Валюта {name} отсутствует")
