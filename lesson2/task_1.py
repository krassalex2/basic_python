# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.


my_list = [1, 1.1, True, [1, 2], (1, 2), {'name': 'Александр'}, None, {1, 2}, b'byte string', 1+2j]
for item in my_list:
    print(f'{item} имеет тип {type(item)}')
