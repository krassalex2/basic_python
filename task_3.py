# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class NotNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg


number_list = []
while True:
    item = input("Введите число или 'stop' для выхода: ")
    if item == 'stop':
        break
    try:
        if item.replace('.', '', 1).isdigit():
            number_list.append(float(item))
        else:
            raise NotNumberError(f'{item} не число')
    except NotNumberError as ex:
        print(ex)

print('Список чисел: ')
print(number_list)
