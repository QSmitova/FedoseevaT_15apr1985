Выведите все уникальные названия продуктов

SELECT DISTINCT product_name FROM products;

Выведите id, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов

SELECT P.product_id, P.product_name, P.price
FROM Products AS P
JOIN Nutritional_Information AS N ON P.product_id = N.product_id
WHERE N.fiber > 5;

Выведите название продукта с самым высоким содержанием белка (protein)

SELECT P.product_name
FROM Products AS P
JOIN Nutritional_Information AS N ON P.product_id = N.product_id
ORDER BY N.protein DESC
LIMIT 1;

Подсчитайте общую сумму калорий для продуктов каждой категории, 
но не учитывайте продукты с нулевым жиром (fat = 0). 
Выведите id категории, сумму калорий.

SELECT P.category_id, SUM(P.calories) AS total_calories
FROM Products AS P
JOIN Nutritional_Information AS N ON P.product_id = N.product_id
WHERE N.fat > 0
GROUP BY P.category_id;

Рассчитайте среднюю цену товаров каждой категории. Выведите название категории, среднюю цену.

SELECT C.category_name, AVG(P.price) AS avg_price
FROM Products AS P
JOIN Categories AS C ON P.category_id = C.category_id
GROUP BY C.category_id;