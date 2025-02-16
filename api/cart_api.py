from typing import Any
import pytest
import allure
import requests


class CartApi:
    """ Класс для взаимодействия с API Altaivita """
    def __init__(self):
        self.base_url = "https://altaivita.ru/engine/cart/"
        self.headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }

        self.constant_params = {
            "S_wh": 1,
            "S_CID": "9cf9d4da38c6a18b80d5a338d0ec98c9"
        }

    @allure.step("Создание запроса")
    def make_request(self, method: str, params: dict[str, str]) -> tuple[int, Any]:
        params.update(self.constant_params)
        response = requests.post(f"{self.base_url}{method}", data=params, headers=self.headers)
        return response.status_code, response.json()

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self, product_id: int, quantity: int) -> float:
        status_code, resp = self.make_request(
            "add_products_to_cart_from_preview.php",
            {
                "product_id": product_id,
                "quantity": quantity
            }
        )

        return resp["products_amount"]

    @allure.step("Удаление товара из корзины")
    def delete_from_cart(self, product_id: int):
        status_code, resp = self.make_request(
            "delete_products_from_cart_preview.php",
            {
                "product_id": product_id
            }
        )

        return resp["sum_quantity"]
