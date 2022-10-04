from .pages.product_page import ProductPage
import time
import pytest

# pip install pytest-rerunfailures # -плагин для перезапуска упавших тестов

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
]


@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product: str) -> None:
    link = product
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.should_be_product_in_basket_and_price_equal()
    time.sleep(3)
