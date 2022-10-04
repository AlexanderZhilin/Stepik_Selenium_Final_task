from selenium.common.exceptions import NoSuchElementException  # Чтобы импортировать нужное нам исключение
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import math


class BasePage():

    def __init__(self, browser, url, timeout=20):  # Конструктор — метод, который вызывается, когда мы создаем объект
        self.browser = browser  # в конструктор передаем экземпляр драйвера и url адрес
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):  # Представлен. Метод в котором будем перехватывать исключения.
        try:
            self.browser.find_element(how, what)  # Как искать (css, id, xpath и тд) и что искать (строку-селектор)
        except (NoSuchElementException):
            return False
        return True

    def is_text_equal(self, equal):  # Локатор 1 - assert сообщение , локатор 2 - assert сообщение
        assert self.is_element_present(*equal[0]), equal[1]
        assert self.is_element_present(*equal[2]), equal[3]
        first_element = self.browser.find_element(*equal[0]).text
        second_element = self.browser.find_element(*equal[2]).text
        assert first_element == second_element, f'Text are not equal: "{first_element}" - "{second_element}"'

    def button_click(self, how, what, timeout=10):  # кнопка найдена, кликабельна, клик
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)),
                                                   "---!!! BUTTON NOT FOUND !!!---")
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((how, what)),
                                                   "---!!! BUTTON NOT CLICKABLE !!!---").click()

    def solve_quiz_and_get_code(self):  # метод в тесте для получения проверочного кода. Задание 4_3 шаг 2
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        WebDriverWait(self.browser, 20).until(EC.alert_is_present(), "---!!! ALERT NOT FOUND !!!---")
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
