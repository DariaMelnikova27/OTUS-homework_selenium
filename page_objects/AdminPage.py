import allure
from selenium.webdriver.common.by import By

from page_objects.BasePage import BasePage


class AdminPage(BasePage):
    """ Класс страницы администратора """
    page_url = "/admin"

    FOOTER = (By.ID, "footer")
    FORGOTTEN_PASSWORD = (By.PARTIAL_LINK_TEXT, "Forgotten")
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CATALOG = (By.XPATH, '//ul[@id="menu"]/li/a[contains(text(), "Catalog")]')
    PRODUCT = (By.XPATH, '//ul[@id="collapse1"]/li/a[contains(text(), "Products")]')
    ADD_NEW = (By.CSS_SELECTOR, "i.fa.fa-plus")
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    DATA = (By.XPATH, '//li/a[@data-toggle="tab"][.="Data"]')
    MODEL = (By.ID, "input-model")
    SAVE = (By.CSS_SELECTOR, "i.fa.fa-save")
    CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    DELETE = (By.CSS_SELECTOR, "button.btn.btn-danger")
    ALERT = (By.CSS_SELECTOR, "div.alert.alert-dismissible")

    def check_elements_on_admin_page(self):
        """ Метод проверки видимости элементов на странице администратора """
        self._find_element(AdminPage.FOOTER)
        self._find_element(AdminPage.FORGOTTEN_PASSWORD)
        self._find_element(AdminPage.INPUT_USERNAME)
        self._find_element(AdminPage.INPUT_PASSWORD)
        self._find_element(AdminPage.SUBMIT_BUTTON)

    @allure.step("Заполняю поле Username значением {username}")
    def user_fill(self, username):
        self._input(self.element(self.INPUT_USERNAME), username)
        return self

    @allure.step("Заполняю поле Password значением {password}")
    def password_fill(self, password):
        self._input(self.element(self.INPUT_PASSWORD), password)
        return self

    @allure.step("Нажимаю кнопку Login")
    def login_button_click(self):
        self.click(self.element(self.SUBMIT_BUTTON))
        return self

    @allure.step("Авторизуюсь на странице администратора")
    def admin_page_login(self):
        self.user_fill("user")
        self.password_fill("bitnami")
        self.login_button_click()

    @allure.step("Открываю раздел добавления нового товара")
    def open_add_product_section(self):
        self.click(self.element(self.CATALOG))
        self.click(self.element(self.PRODUCT))
        return self

    @allure.step("Заполняю поле Product Name значением {product_name}")
    def product_name_fill(self, product_name):
        self._input(self.element(self.PRODUCT_NAME), product_name)
        return self

    @allure.step("Заполняю поле Meta Tag Title значением {meta_tag_title}")
    def meta_tag_title_fill(self, meta_tag_title):
        self._input(self.element(self.META_TAG_TITLE), meta_tag_title)
        return self

    @allure.step("Открываю вкладку Data")
    def open_data_section(self):
        self.click(self.element(self.DATA))
        return self

    @allure.step("Заполняю поле Model значением {model}")
    def model_fill(self, model):
        self._input(self.element(self.MODEL), model)
        return self

    @allure.step("Проверяю отображения алерта после добавления/удаления товара")
    def check_alert(self):
        text = self.element(self.ALERT).text.strip().replace("\n×", "")
        assert text == "Success: You have modified products!"

    @allure.step("Добавляю новый товар")
    def add_new_product(self):
        self.click(self.element(self.ADD_NEW))
        self.product_name_fill("TestProduct")
        self.meta_tag_title_fill("123")
        self.open_data_section()
        self.model_fill("Q12GH")
        self.click(self.element(self.SAVE))
        self.check_alert()
        return self

    @allure.step("Удаляю товар")
    def delete_product(self):
        self.driver.find_elements(*self.CHECKBOX)[1].click()
        self.click(self.element(self.DELETE))
        self.driver.switch_to.alert.accept()
        self.check_alert()
        return self
