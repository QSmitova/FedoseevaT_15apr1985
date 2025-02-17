import allure


@allure.title("Поиск")
@allure.description("Тест на поиск товара по названию")
@allure.feature("Search")
@allure.severity("critical")
def test_search_product(main_ui_page, search_ui_page):
    main_ui_page.open()
    main_ui_page.find_product("грибы")

    with allure.step("Проверка, что карточка, в названии которой содержится поисковый запрос, существует"):
        assert search_ui_page.find_card_with_title("Белые грибы, сушеные, резаные, 40 г") is not None


@allure.title("Корзина")
@allure.description("Тест на добавление товара в корзину")
@allure.feature("Cart")
@allure.severity("critical")
def test_add_to_cart(main_ui_page, search_ui_page, cart_ui_page):
    main_ui_page.open()
    main_ui_page.find_product("грибы")

    card = search_ui_page.find_card_with_title("Белые грибы, сушеные, резаные, 40 г")
    search_ui_page.add_card_to_cart(card)

    cart_ui_page.open()
    with allure.step("Проверка, что в корзину добавлен товар"):
        assert len(cart_ui_page.find_cart_items()) > 0

    cart_ui_page.cart_delete()



@allure.title("Корзина")
@allure.description("Тест на удаление товара из корзины")
@allure.feature("Cart")
@allure.severity("critical")
def test_delete_from_cart(main_ui_page, search_ui_page, cart_ui_page):
    main_ui_page.open()
    main_ui_page.find_product("грибы")

    card = search_ui_page.find_card_with_title("Белые грибы, сушеные, резаные, 40 г")
    search_ui_page.add_card_to_cart(card)

    cart_ui_page.open()
    cart_ui_page.cart_delete()
    with allure.step("Проверка, что из корзины удален товар"):
        assert cart_ui_page.get_total_amount_text() == "0 ₽"
