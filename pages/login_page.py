from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):  # проверка, что есть страница логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):  # проверка на корректный url
        assert "login" in self.browser.current_url, "Current page is not a login page"

    def should_be_login_form(self):  # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):  # проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"  #
