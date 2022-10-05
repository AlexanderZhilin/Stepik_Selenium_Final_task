from .pages.product_page import ProductPage
import pytest

# pip install pytest-rerunfailures # -плагин для перезапуска упавших тестов

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
]

# Т.к все страницы отличаются лишь последней цифрой, то для удобства создадим генератор страниц и
# xf - кортеж из старниц, которые падают, сюда можно дописывать номера страниц.
# Полезно, если например подобных страниц тысячи :)
xf = (7,)  # список страниц с падающими тестами
lin = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links2 = [pytest.param(lin + str(i), marks=pytest.mark.xfail) if i in xf else lin + str(i) for i in range(10)]


@pytest.mark.parametrize("product", links + links2)
def test_guest_can_add_product_to_basket(browser, product: str) -> None:
    link = product
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.should_be_product_in_basket_and_price_equal()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()