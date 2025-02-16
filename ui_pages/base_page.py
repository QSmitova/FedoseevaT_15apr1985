import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" Базовый класс для браузера """


class BasePage:
    url = None

    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def open(self):
        with allure.step(f"Открытие страницы: {self.url}"):
            self._driver.get(self.url)

    @allure.step("Обновление страницы")
    def refresh(self):
        self._driver.refresh()

    @allure.step("Поиск элемента на странице")
    def find_element(self, by: str, value: str, *, timeout: int = 10) -> WebElement:
        WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_element_located((by, value))
        )

        return self._driver.find_element(by, value)

    @allure.step("Проверка существования элемента на странице")
    def element_exists(self, by: str, value: str, *, timeout: int = 10) -> bool:
        try:
            self.find_element(by, value, timeout=timeout)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    @allure.step("Поиск элементов на странице")
    def find_elements(self, by: str, value: str, *, timeout: int = 10) -> list[WebElement]:
        WebDriverWait(self._driver, timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )
        return self._driver.find_elements(by, value)
