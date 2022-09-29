from .base_page import BasePage  # из файла base_page.py импортируем класс BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


# MainPage - это главная страница
class MainPage(BasePage):  # MainPage является наследником класса BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
         # time.sleep(5)

    def should_be_login_link(self):  # should_be_(название элемента) - метод проверки
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented" - удали.устар
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        # где *MainPageLocators.LOGIN_LINK это By.CSS_SELECTOR, "#login_link" из locators.py
