import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser) -> None:
        """ Гость должен видеть ссылку на логин на главной странице """

        link = "http://selenium1py.pythonanywhere.com/"  # -ссылка на главную страницу т.е. MainPage
        page = MainPage(browser, link)  # инициализируем Page Object, передаем экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser) -> None:
        """ Гость должен видеть ссылку на логин на главной странице """

        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser) -> None:
    """ Гость не видит товар в корзине, открытой с главной страницы """

    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_appeared_product_in_basket()
    basket_page.should_appeared_text_basket_is_empty()
