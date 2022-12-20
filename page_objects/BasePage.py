from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """ Базовый класс с общими mетодами для всех страниц """
    url = "http://192.168.0.102:8081"
    page_url = None

    MY_ACCOUNT_MENU = (By.CSS_SELECTOR, 'a[title="My Account"]')
    REGISTER_LINK = (By.XPATH, '//ul[contains(@class, "dropdown-menu")]/li/a[.="Register"]')

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        """
        Метод клика по элементу
        """
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    def _input(self, element, value):
        """
        Метод ввода данных
        """
        self.click(element)
        element.clear()
        element.send_keys(value)

    def element(self, locator: tuple):
        """
        Метод ожидания элемента
        """
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    def _find_element(self, locator):
        """
        Метод поиска элементов
        """
        return self.driver.find_elements(*locator)

    def open_page(self, browser):
        """
        Метод открытия страницы
        """
        browser.get(browser.url + self.page_url)
