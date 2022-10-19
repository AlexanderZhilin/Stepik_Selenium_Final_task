from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        assert self.is_appeared(*LoginPageLocators.REGISTRATION_EMAIL), '"registration email" is not presented'
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        assert self.is_appeared(*LoginPageLocators.REGISTRATION_PASSWORD1), '"registration password1" is not presented'
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(password)
        assert self.is_appeared(*LoginPageLocators.REGISTRATION_PASSWORD2), '"registration password2" is not presented'
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(password)
        self.button_click(*LoginPageLocators.REGISTRATION_SUBMIT)
        assert self.is_appeared(*LoginPageLocators.REGISTRATION_MESSAGE,
                                timeout=10), '"registration message" is not presented'
        my_text = ('Thanks for registering!', 'Спасибо за регистрацию!')
        assert self.my_text_is_in_text(*LoginPageLocators.REGISTRATION_MESSAGE,
                                       my_text), f'Registration status is not: "{my_text}"'

    def should_be_login_page(self):  # проверка, что есть страница логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # проверка на корректный url
        assert "login" in self.browser.current_url, "Current page is not a login page"

    def should_be_login_form(self):  # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):  # проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
