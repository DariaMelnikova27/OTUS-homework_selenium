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
        """
        Метод проверки видимости элементов на странице администратора
        """
        self._find_element(AdminPage.FOOTER)
        self._find_element(AdminPage.FORGOTTEN_PASSWORD)
        self._find_element(AdminPage.INPUT_USERNAME)
        self._find_element(AdminPage.INPUT_PASSWORD)
        self._find_element(AdminPage.SUBMIT_BUTTON)

    def user_fill(self, username):
        """
        Метод заполнения поля Username
        """
        self._input(self.element(self.INPUT_USERNAME), username)
        return self

    def password_fill(self, password):
        """
        Метод заполнения поля Password
        """
        self._input(self.element(self.INPUT_PASSWORD), password)
        return self

    def login_button_click(self):
        """
        Метод нажатия кнопки Login
        """
        self.click(self.element(self.SUBMIT_BUTTON))
        return self

    def admin_page_login(self):
        """
        Метод авторизации на странице администратора
        """
        self.user_fill("user")
        self.password_fill("bitnami")
        self.login_button_click()

    def open_add_product_section(self):
        """
        Метод открытия раздела добавления нового товара
        """
        self.click(self.element(self.CATALOG))
        self.click(self.element(self.PRODUCT))
        return self

    def product_name_fill(self, product_name):
        """
        Метод заполнения поля Product Name
        """
        self._input(self.element(self.PRODUCT_NAME), product_name)
        return self

    def meta_tag_title_fill(self, meta_tag_title):
        """
        Метод заполнения поля Meta Tag Title
        """
        self._input(self.element(self.META_TAG_TITLE), meta_tag_title)
        return self

    def open_data_section(self):
        """
        Метод открытия вкладки Data
        """
        self.click(self.element(self.DATA))
        return self

    def model_fill(self, model):
        """
        Метод заполнения поля Model
        """
        self._input(self.element(self.MODEL), model)
        return self

    def check_alert(self):
        """
        Метод проверки отображения алерта после добавления/удаления товара
        """
        text = self.element(self.ALERT).text.strip().replace("\n×", "")
        assert text == "Success: You have modified products!"

    def add_new_product(self):
        """
        Метод добавления нового товара
        """
        self.click(self.element(self.ADD_NEW))
        self.product_name_fill("TestProduct")
        self.meta_tag_title_fill("123")
        self.open_data_section()
        self.model_fill("Q12GH")
        self.click(self.element(self.SAVE))
        self.check_alert()
        return self

    def delete_product(self):
        """
        Метод удаления товара
        """
        self.driver.find_elements(*self.CHECKBOX)[1].click()
        self.click(self.element(self.DELETE))
        self.driver.switch_to.alert.accept()
        self.check_alert()
        return self
