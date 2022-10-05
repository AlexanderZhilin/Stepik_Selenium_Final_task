from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_MAIN_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_MAIN_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
