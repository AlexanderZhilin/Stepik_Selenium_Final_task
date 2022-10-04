from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self) -> None:
        self.button_click(*ProductPageLocators.BTN_ADD_TO_BASKET)
        # if "?promo=newYear" in self.browser.current_url:
        self.solve_quiz_and_get_code()
        # print(self.browser.current_url)

    def should_be_product_in_basket_and_price_equal(self) -> None:
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
