from .base_page import BasePage  # из файла base_page.py импортируем класс BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):  # MainPage является наследником класса BasePage
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        # time.sleep(5)
