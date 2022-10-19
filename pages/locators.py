from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = "registration_submit"]')
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '#messages')

    LOGIN_USERNAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_MAIN_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_MAIN_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages > :nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages > :nth-child(3) strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasketPageLocators():
    FIRST_ITEM_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    BASKET_STATUS = (By.CSS_SELECTOR, '.content')
    BASKET_FORM = (By.CSS_SELECTOR, '#content_inner')
