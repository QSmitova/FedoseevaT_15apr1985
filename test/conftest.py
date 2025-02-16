import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from api.cart_api import CartApi
from ui_pages import MainPage
from ui_pages.cart_page import CartPage
from ui_pages.search_page import SearchPage


@pytest.fixture(scope="session")
def browser() -> WebDriver:
    """Фикстура для получения объекта WebDriver"""

    with allure.step("Открыть и настроить браузер"):
        browser = webdriver.Chrome()
        browser.implicity_wait(4)
        browser.maximize_window()
        yield browser

    with allure.step("Закрыть браузер"):
        browser.quit()


"""Фикстура для получения главной страницы"""


@pytest.fixture(scope="module")
def main_ui_page(browser: WebDriver) -> MainPage:
    return MainPage(browser)


"""Фикстура для получения страницы поиска"""


@pytest.fixture(scope="module")
def search_ui_page(browser: WebDriver) -> SearchPage:
    return SearchPage(browser)


"""Фикстура для получения страницы корзины"""


@pytest.fixture(scope="module")
def cart_ui_page(browser: WebDriver) -> CartPage:
    return CartPage(browser)


"""Фикстура для получения класса для взаимодействия с API"""


@pytest.fixture(scope="module")
def cart_api() -> CartApi:
    return CartApi()
