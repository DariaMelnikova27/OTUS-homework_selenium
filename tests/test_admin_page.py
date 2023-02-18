import allure
from allure_commons.types import Severity
from page_objects.AdminPage import AdminPage

""" Тесты страницы администратора """


@allure.severity(severity_level=Severity.CRITICAL)
@allure.feature('Действия на странице администратора')
@allure.title('Проверка видимости элементов на странице администратора')
def test_admin_page(browser):
    page = AdminPage(browser)
    page.open_page(browser)
    page.check_elements_on_admin_page()
