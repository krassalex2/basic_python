# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


items = []
while True:
    item = input('Введите элемент. Для прекращения ввода элементов нажмите q: ')
    if item == 'q':
        break
    items.append(item)

print('Исходный список')
print(items)

for index in range(1, len(items), 2):
    items[index - 1], items[index] = items[index], items[index - 1]

print('Преобразованный список')
print(items)