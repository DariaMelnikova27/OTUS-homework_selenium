from page_objects.AdminPage import AdminPage

""" Тесты страницы администратора """


def test_admin_page(browser):
    """
    Проверка видимости элементов на странице администратора
    """
    page = AdminPage(browser)
    page.open_page(browser)
    page.check_elements_on_admin_page()


def test_add_new_product(browser):
    """
    Добавление нового товара в разделе администратора
    """
    page = AdminPage(browser)
    page.open_page(browser)
    page.admin_page_login()
    page.open_add_product_section()
    page.add_new_product()


def test_delete_product(browser):
    """
    Удаление товара из списка в разделе администратора
    """
    page = AdminPage(browser)
    page.open_page(browser)
    page.admin_page_login()
    page.open_add_product_section()
    page.delete_product()
