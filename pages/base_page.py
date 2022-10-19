from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import math
from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=4):  # Конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser  # в конструктор передаем экземпляр драйвера и url адрес
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        # alert = self.browser.switch_to.alert # 1) перейти на всплывающее окно
        # alert.accept() #1) принять всплывающее окно
        # time.sleep(5)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        # где *BasePageLocators.LOGIN_LINK это By.CSS_SELECTOR, "#login_link" из locators.py

    def is_element_present(self, how, what):  # смотрм, что элемент присутствует - 0 сек
        try:
            self.browser.find_element(how, what)  # Как искать (css, id, xpath и тд) и что искать (строку-селектор)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):  # ждем не появления элемента - 4 сек
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_appeared(self, how, what, timeout=4):  # ждем появления элемента - 4 сек
        pass

    def is_disappeared(self, how, what, timeout=4):  # ждем исчезновения элемента - 4 сек
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_text_equal(self, equal):  # Локатор 1 - assert сообщение , локатор 2 - assert сообщение
        assert self.is_element_present(*equal[0]), equal[1]
        assert self.is_element_present(*equal[2]), equal[3]
        first_element = self.browser.find_element(*equal[0]).text
        second_element = self.browser.find_element(*equal[2]).text
        assert first_element == second_element, f'Text are not equal: "{first_element}" - "{second_element}"'

    def my_text_is_in_text(self, how, what, my_text):
        try:
            if my_text in self.browser.find_element(how, what).text:
                return True
            else:
                return False
        except NoSuchElementException:
            return False

    def button_click(self, how, what, timeout=10):  # кнопка найдена, кликабельна, клик
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)),
                                                   "---!!! BUTTON NOT FOUND !!!---")
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)),
                                                   "---!!! BUTTON NOT CLICKABLE !!!---").click()

    def should_be_alert_appeared(self, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(EC.alert_is_present(), "alert_not_appeared")
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):  # метод в тесте для получения проверочного кода. Задание 4_3 шаг 2
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        if self.should_be_alert_appeared():
            try:
                alert = self.browser.switch_to.alert
                alert_text = alert.text
                print(f"Your code: {alert_text}")
                alert.accept()
            except NoAlertPresentException:
                print("No second alert presented")
