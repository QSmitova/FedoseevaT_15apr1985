import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ui_pages import BasePage

"""
    Класс для главной страницы интернет-магазина Алтайвита
"""


class MainPage(BasePage):
    url = "https://altaivita.ru/"

    @allure.step("Поиск поля поиска")
    def find_search_input(self) -> WebElement:
        return self.find_element(By.CSS_SELECTOR, '[placeholder="Поиск товаров"]')

    @allure.step("Поиск товара в строке поиска")
    def find_product(self, product_name: str):
        search_input = self.find_search_input()
        with allure.step("Нажатие на поле поиска"):
            search_input.click()
        with allure.step(f"Ввод значения: {product_name} в поле поиска"):
            search_input.send_keys(product_name)
        with allure.step("Подтверждение ввода в поле поиска (Keys.RETURN)"):
            search_input.send_keys(Keys.RETURN)
