# Есть возможность прогонять тесты через Chrome или Firefox указав их в командной строке терминала
# pytest -s -v --browser_name=chrome  --language=ru test_parser.py    - для Chrome (по умолчанию)
# pytest -s -v --browser_name=firefox --language=ru test_parser.py    - для Firefox

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):  # добавляет опции в командную строку, чтоб мы могли к ним обращаться
    # добавляем возможность в командной строке вводить: --browser_name=firefox
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    # добавляем возможность в командной строке вводить: --language=(любой язык, например en)
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, de, fr")


@pytest.fixture(scope="function")
def browser(request):
    # возьмем из командной строки значение от --browser_name=
    browser_name = request.config.getoption("browser_name")
    # возьмем из командной строки значение от --language=
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with {user_language}..")
        options = Options()
        # options.add_argument("window-size=1920,1040")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        # options.add_argument("--headless") # 1) отключить окна
        browser = webdriver.Chrome(options=options)  # 2) включить просмотр окон
    elif browser_name == "firefox":
        print(f"\nstart firefox browser for test with {user_language}..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
