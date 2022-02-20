# Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
# Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_numbers_to_asteriks(input_str):
    """
    Суммирует строку чисел вида 'a b c...' до знака *
    :param input_str: Входная строка вида 'a b c...'
    :return: Возвращает сумму чисел до знака *
    """
    nums = input_str.split()
    result = 0
    for n in nums:
        if n == '*':
            break
        else:
            result += float(n)
    return result


def has_asterisk(input_str):
    """
    Проверяет наличие символа * в строке
    :param input_str: Входная строка
    :return: Возвращает True, если в строке есть *
    """
    return True if '*' in input_str else False


result_sum = 0
while True:
    source_str = input('Введите строку чисел, разделенных пробелом. '
                       'Добавьте при вводе специальный символ * вместо одного из чисел, '
                       'чтобы завершить работу программы: ')
    result_sum += sum_numbers_to_asteriks(source_str)
    print(f'Текущая сумма: {result_sum}')
    if has_asterisk(source_str):
        break
