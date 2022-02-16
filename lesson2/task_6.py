# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
#
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
# }

from pprint import pprint


products = []
product_id = 1

while True:
    item = input('Введите q для выхода или нажмите Enter: ')
    if item == 'q':
        break
    product_name = input('Введите наименование товара: ')
    product_cost = int(input('Введите стоимость товара: '))
    product_count = int(input('Введите кол-во товара: '))
    product_measure = input('Введите название единицы измерения: ')
    products.append((product_id,
                     {'Название': product_name, 'Стоимость': product_cost, 'Кол-во': product_count, 'Ед.': product_measure}))
    product_id += 1

print('Исходная структура данных')
pprint(products)

properties_list = ['Название', 'Стоимость', 'Кол-во', 'Ед.']
properties_dict = dict()
for prop in properties_list:
    values_list = []
    for product in products:
        values_list.append(product[1].get(prop))
    properties_dict[prop] = list(set(values_list))

print('Аналитика')
pprint(properties_dict)
