# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(dividend, divider):
    """
    Выполняет деление одного числа на другое.
    :param dividend: Делимое
    :param divider: Делитель
    :return: Возвращает частное
    """
    return dividend / divider


try:
    a = float(input('Введите делимое: '))
    b = float(input('Введите делитель: '))
    print('Частное:', division(a, b))
except ValueError:
    print('Введено не число!')
except ZeroDivisionError:
    print('Деление на ноль не допустимо!')
