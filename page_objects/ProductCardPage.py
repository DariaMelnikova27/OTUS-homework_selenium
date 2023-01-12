from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class ProductCardPage(BasePage):
    """ Класс страницы карточки товара """
    page_url = "/tablet/samsung-galaxy-tab-10-1"

    NAVBAR = (By.CLASS_NAME, "navbar")
    DESCRIPTION = (By.LINK_TEXT, "Description")
    ADD_TO_CART = (By.CSS_SELECTOR, "#product #button-cart")
    REVIEWS = (By.CSS_SELECTOR, "#tab-review")
    TWEET = (By.CLASS_NAME, "twitter-share-button")

    def check_elements_on_product_card_page(self):
        """ Метод проверки видимости элементов на странице карточки товара """
        self._find_element(ProductCardPage.NAVBAR)
        self._find_element(ProductCardPage.DESCRIPTION)
        self._find_element(ProductCardPage.ADD_TO_CART)
        self._find_element(ProductCardPage.REVIEWS)
        self._find_element(ProductCardPage.TWEET)
