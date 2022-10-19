from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators


# Важно! EC.visibility_of_element_located(локатор-кортеж, не распаковываем), а is_not_element_present(*распаковываем)

class ProductPage(BasePage):
    def add_product_to_basket(self) -> None:
        self.button_click(*ProductPageLocators.BTN_ADD_TO_BASKET)
        if self.should_be_alert_appeared():
            self.solve_quiz_and_get_code()

    def should_be_product_in_basket_and_price_equal(self) -> None:
        """ Должен быть товар в корзине и цена соответствующая """

        WebDriverWait(self.browser, 30).until(
            EC.visibility_of_element_located(ProductPageLocators.MESSAGE_ADDED_TO_BASKET),
            'Message "added to basket" did not appear')
        # Список сравниваемых элементов. Локатор первого - assert сообщение , локатор втогого - assert сообщение
        equality = [(ProductPageLocators.NAME_MAIN_PRODUCT, "Product name is not present",
                     ProductPageLocators.MESSAGE_ADDED_TO_BASKET, 'Message: "product added to basket" not present'),
                    (ProductPageLocators.PRICE_MAIN_PRODUCT, "Product price is not present",
                     ProductPageLocators.BASKET_PRICE, 'Message: "product price in basket" not present')
                    ]
        for equal in equality:
            self.is_text_equal(equal)

    def should_disappeared_success_message(self):
        """ Должно исчезнуть сообщение об успехе """

        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message does not disappear, but should have disappeared"

    def should_not_be_success_message(self):
        """ Должно не быть успешное сообщение """

        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
