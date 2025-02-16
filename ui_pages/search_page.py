import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ui_pages import BasePage

"""
    Класс для страницы поиска
"""


class SearchPage(BasePage):
    url = "https://altaivita.ru/search/"

    @allure.step("Поиск карточек товара")
    def find_result_cards(self) -> list[WebElement]:
        return self.find_elements(By.CSS_SELECTOR, ".category__list > .category__row > .category__col")

    @allure.step("Поиск карточек товара по названию")
    def get_card_title(self, card: WebElement) -> str:
        return card.find_element(By.CSS_SELECTOR, "div.product__info a > span").text

    @allure.step("Поиск карточек товара, в названии которых содержится поисковый запрос")
    def find_card_with_title(self, title: str) -> WebElement | None:
        for card in self.find_result_cards():
            if self.get_card_title(card) == title:
                return card

        return None

    @allure.step("Добавление товара в корзину")
    def add_card_to_cart(self, card: WebElement):
        card.find_element(By.CSS_SELECTOR, "div.product__add_2_0 > button").click()
