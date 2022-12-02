from selenium.webdriver.common.by import By


class GeneralPage:
    WISHLIST = (By.CSS_SELECTOR, "#wishlist-total")
    LOGO = (By.ID, "logo")
    MACBOOK = (By.LINK_TEXT, "MacBook")
    SWIPER = (By.CLASS_NAME, "swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")
    ABOUT_US = (By.LINK_TEXT, "About Us")


class CatalogPage:
    GRID_VIEW_BUTTON = (By.ID, "grid-view")
    LIST_VIEW_BUTTON = (By.ID, "list-view")
    MENU = (By.CSS_SELECTOR, ".list-group")
    SORT_FIELD = (By.CSS_SELECTOR, "#input-sort")
    BANNER = (By.CSS_SELECTOR, ".swiper-wrapper")


class ProductCardPage:
    NAVBAR = (By.CLASS_NAME, "navbar")
    DESCRIPTION = (By.LINK_TEXT, "Description")
    ADD_TO_CART = (By.CSS_SELECTOR, "#product #button-cart")
    REVIEWS = (By.CSS_SELECTOR, "#tab-review")
    TWEET = (By.CLASS_NAME, "twitter-share-button")


class AdminPage:
    FOOTER = (By.ID, "footer")
    FORGOTTEN_PASSWORD = (By.PARTIAL_LINK_TEXT, "Forgotten")
    INPUT_USERNAME = (By.NAME, "username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class AccountRegisterPage:
    PERSONAL_DETAILS = (By.ID, "account")
    INPUT_FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    YES_RADIOBUTTON = (By.CSS_SELECTOR, "input[type='radio'][value='1']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "input[type='submit'][value='Continue']")
