import allure
from page_objects.AccountRegisterPage import AccountRegisterPage
from allure_commons.types import Severity

""" Тесты страницы регистрации нового пользователя """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Регистрация нового пользователя')
@allure.title('Проверка видимости элементов на странице регистрации нового пользователя')
def test_account_register_page(browser):
    page = AccountRegisterPage(browser)
    page.open_page(browser)
    page.check_elements_on_account_register_page()


@allure.severity(severity_level=Severity.BLOCKER)
@allure.feature('Регистрация нового пользователя')
@allure.title('Регистрация нового пользователя в магазине опенкарта')
def test_new_user_register(browser):
    page = AccountRegisterPage(browser)
    page.open_page(browser)
    page.firstname_fill("Ivan") \
        .lastname_fill("Petrov") \
        .email_fill("123@ya.ru") \
        .telephone_fill("12345678") \
        .password_fill("Qwe12345") \
        .password_confirm_fill("Qwe12345") \
        .checkbox_agree_click() \
        .continue_button_click()
    assert "Your Account Has Been Created!" in page.success_register_message
