import allure
import pytest


@allure.title("Корзина")
@allure.description("Тест на добавление товара в корзину")
@allure.feature("Add")
@allure.severity("critical")
def test_add_to_cart(cart_api):
    cart_api.delete_from_cart(2858)

    assert cart_api.add_to_cart(2858, 1) == 4.92


@allure.title("Корзина")
@allure.description("Тест на удаление товара из корзины")
@allure.feature("Delete")
@allure.severity("critical")
def test_delete_from_cart(cart_api):
    cart_api.add_to_cart(2858, 2)

    assert cart_api.delete_from_cart(2858) == "0"
