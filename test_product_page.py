from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest
import time

# pip install pytest-rerunfailures # -плагин для перезапуска упавших тестов
# Для запуска тестов из командной строки:
# cd C:\Users\Александр\PyProject\Python Обучение\Stepik_Selenium\Stepik_Selenium_Final_task
# PyTest_env\Scripts\activate.bat
# pytest -v -s --tb=line -m need_review --reruns 3 --language=en --browser_name=chrome test_product_page.py

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


@pytest.mark.need_review
@pytest.mark.parametrize("product", links + links2)
def test_guest_can_add_product_to_basket(browser, product: str) -> None:
    link = product
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()
    page.add_product_to_basket()
    page.should_be_product_in_basket_and_price_equal()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser) -> None:
    """ Гость может перейти на страницу логина со страницы товара """

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser) -> None:
    """ Гость не видит товар в корзине, открытой со страницы товара """

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_appeared_product_in_basket()
    basket_page.should_appeared_text_basket_is_empty()


def test_guest_cant_see_success_message(browser) -> None:
    """ Гость не может видеть сообщение об успехе. Ждем появления <= 4 сек  """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser) -> None:
    """ Гость не может видеть сообщение об успехе после добавления товара в корзину. Ждем появления <= 4 сек  """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser) -> None:
    """ Гость должен видеть логин ссылку на странице товаров """

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser) -> None:
    """ Сообщение исчезает после добавления товара в корзину. Ждем исчезновения <= 4 сек  """

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()


@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'  # -ссылка на LoginPage
        page = LoginPage(browser, link)  # инициализируем Page Object, передаем экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        email = str(time.time()) + '@fakemail.org'
        password = str(time.time()) + 'Tpj-xhh-k4M-6ar'
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser) -> None:
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_product_in_basket_and_price_equal()

    def test_user_cant_see_success_message(self, browser) -> None:
        """ Пользователь не может видеть сообщение об успехе. Ждем появления <= 4 сек  """

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
