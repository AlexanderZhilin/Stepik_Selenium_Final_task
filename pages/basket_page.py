from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_form()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Current page is not a basket page"

    def should_be_basket_form(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FORM), "Basket form is not presented"

    def should_appeared_text_basket_is_empty(self) -> None:
        """ Должен появиться текст, что корзина пуста. Ждем появления <= 4 сек """

        assert self.is_element_present(*BasketPageLocators.BASKET_STATUS), "basket status is not present, but should be"
        my_text = 'Ваша корзина пуста'
        assert self.my_text_is_in_text(*BasketPageLocators.BASKET_STATUS, my_text), f'Basket status is not: "{my_text}"'

    def should_not_appeared_product_in_basket(self) -> None:
        """ Не должен появиться товар в корзине. Ждем == 4 сек"""

        assert self.is_not_element_present(
            *BasketPageLocators.FIRST_ITEM_IN_BASKET, ), "product in basket, but should not appear"
