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


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на странице администратора')
@allure.title('Добавление нового товара в разделе администратора')
def test_add_new_product(browser):
    page = AdminPage(browser)
    page.open_page(browser)
    page.admin_page_login()
    page.open_add_product_section()
    page.add_new_product()


@allure.severity(severity_level=Severity.NORMAL)
@allure.feature('Действия на странице администратора')
@allure.title('Удаление товара из списка в разделе администратора')
def test_delete_product(browser):
    page = AdminPage(browser)
    page.open_page(browser)
    page.admin_page_login()
    page.open_add_product_section()
    page.delete_product()
