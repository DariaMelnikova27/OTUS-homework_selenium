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
