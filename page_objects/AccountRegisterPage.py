from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AccountRegisterPage(BasePage):
    """ Класс страницы регистрации нового пользователя """
    page_url = "/index.php?route=account/register"

    PERSONAL_DETAILS = (By.ID, "account")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_TELEPHONE = (By.CSS_SELECTOR, "#input-telephone")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "input[type='radio'][value='1']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
    CHECKBOX_AGREE = (By.NAME, "agree")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content > h1")

    def check_elements_on_account_register_page(self):
        """
        Метод проверки видимости элементов на странице регистрации нового пользователя
        """
        self._find_element(AccountRegisterPage.PERSONAL_DETAILS)
        self._find_element(AccountRegisterPage.INPUT_FIRSTNAME)
        self._find_element(AccountRegisterPage.INPUT_PASSWORD)
        self._find_element(AccountRegisterPage.YES_RADIOBUTTON)
        self._find_element(AccountRegisterPage.CONTINUE_BUTTON)

    def firstname_fill(self, firstname):
        """
        Метод заполнения поля First Name
        """
        self._input(self.element(self.INPUT_FIRSTNAME), firstname)
        return self

    def lastname_fill(self, lastname):
        """
        Метод заполнения поля Last Name
        """
        self._input(self.element(self.INPUT_LASTNAME), lastname)
        return self

    def email_fill(self, email):
        """
        Метод заполнения поля E-Mail
        """
        self._input(self.element(self.INPUT_EMAIL), email)
        return self

    def telephone_fill(self, telephone):
        """
        Метод заполнения поля Telephone
        """
        self._input(self.element(self.INPUT_TELEPHONE), telephone)
        return self

    def password_fill(self, password):
        """
        Метод заполнения поля Password
        """
        self._input(self.element(self.INPUT_PASSWORD), password)
        return self

    def password_confirm_fill(self, password_confirm):
        """
        Метод заполнения поля Password Confirm
        """
        self._input(self.element(self.INPUT_PASSWORD_CONFIRM), password_confirm)
        return self

    def checkbox_agree_click(self):
        """
        Метод выбора чекбокса I have read and agree to the Privacy Policy
        """
        self.click(self.element(self.CHECKBOX_AGREE))
        return self

    def continue_button_click(self):
        """
        Метод нажатия кнопки Continue
        """
        self.click(self.element(self.CONTINUE_BUTTON))
        return self

    @property
    def success_register_message(self):
        """
        Метод проверки отображения сообщения об успешной регистрации
        """
        msg = self.element(self.SUCCESS_MESSAGE)
        return msg.text
