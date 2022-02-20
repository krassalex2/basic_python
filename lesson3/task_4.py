# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.


def power(positive_number, negative_number):
    """
    Выполняет возведение положительного числа x в отрицательную степень y
    :param positive_number: Действительное положительное число.
    :param negative_number: Целое отрицательное число.
    :return: Возвращает результат возведения positive_number в степень negative_number.
    """
    if positive_number <= 0:
        raise ValueError('positive_number должно быть положительным')
    if negative_number >= 0:
        raise ValueError('negative_number должно быть отрицательным')
    result = 1
    for index in range(abs(negative_number)):
        result *= 1 / positive_number
    return result


print(f'{power(10, -3)}')
