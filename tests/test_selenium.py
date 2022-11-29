from page_objects import GeneralPage, CatalogPage, ProductCardPage, AdminPage, AccountRegisterPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_general_page(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(GeneralPage.WISHLIST))
    browser.find_element(*GeneralPage.WISHLIST)
    browser.find_element(*GeneralPage.LOGO)
    browser.find_element(*GeneralPage.MACBOOK)
    browser.find_element(*GeneralPage.SWIPER)
    browser.find_element(*GeneralPage.ABOUT_US)


def test_catalog_page(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    browser.find_element(*CatalogPage.GRID_VIEW_BUTTON)
    browser.find_element(*CatalogPage.LIST_VIEW_BUTTON)
    wait = WebDriverWait(browser, 2)
    wait.until(EC.visibility_of_element_located(CatalogPage.MENU))
    browser.find_element(*CatalogPage.MENU)
    browser.find_element(*CatalogPage.SORT_FIELD)
    browser.find_element(*CatalogPage.BANNER)


def test_product_card_page(browser):
    browser.get(browser.url + "/tablet/samsung-galaxy-tab-10-1")
    browser.find_element(*ProductCardPage.NAVBAR)
    browser.find_element(*ProductCardPage.DESCRIPTION)
    browser.find_element(*ProductCardPage.ADD_TO_CART)
    browser.find_element(*ProductCardPage.REVIEWS)
    browser.find_element(*ProductCardPage.TWEET)


def test_admin_page(browser):
    browser.get(browser.url + "/admin")
    browser.find_element(*AdminPage.FOOTER)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located(AdminPage.FOOTER))
    browser.find_element(*AdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*AdminPage.INPUT_USERNAME)
    browser.find_element(*AdminPage.INPUT_PASSWORD)
    browser.find_element(*AdminPage.SUBMIT_BUTTON)


def test_account_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(*AccountRegisterPage.PERSONAL_DETAILS)
    browser.find_element(*AccountRegisterPage.INPUT_FIRSTNAME)
    wait = WebDriverWait(browser, 1)
    wait.until(EC.visibility_of_element_located(AccountRegisterPage.INPUT_PASSWORD))
    browser.find_element(*AccountRegisterPage.INPUT_PASSWORD)
    browser.find_element(*AccountRegisterPage.YES_RADIOBUTTON)
    browser.find_element(*AccountRegisterPage.CONTINUE_BUTTON)
