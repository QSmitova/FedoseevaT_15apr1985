import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ui_pages import BasePage

"""
    Класс для страницы корзины
"""


class CartPage(BasePage):
    url = "https://altaivita.ru/cart/"

    @allure.step("Поиск карточки добавленного товара в корзине")
    def find_cart_items(self) -> list[WebElement]:
        return self.find_elements(By.CSS_SELECTOR, ".basket__list > .basket__item")

    @allure.step("Поиск кнопки удаления товара из корзины")
    def find_cart_delete(self) -> WebElement:
        return self.find_element(By.CSS_SELECTOR, "div[class='basket__delete js-item-delete'] i[class='fal fa-times']")

    @allure.step("Удаление товара из корзины")
    def cart_delete(self):
        delete_btn = self.find_cart_delete()
        with allure.step("Нажатие на кнопку удаление товара"):
            delete_btn.click()

    @allure.step("Поиск результата общей стоимости")
    def find_total_amount(self) -> WebElement:
        return self.find_element(
            By.CSS_SELECTOR,
            ".basket__result-top .js-cart_page_total_amount"
        )

    @allure.step("Получение текста результата общей стоимости")
    def get_total_amount_text(self) -> str:
        return self.find_total_amount().text
