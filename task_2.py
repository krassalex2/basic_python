# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class CustomZeroDivisionError(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    dividend = float(input('Введите делимое: '))
    divider = float(input('Введите делитель: '))
    if divider == 0:
        raise CustomZeroDivisionError('Деление на ноль!!!')
    result = dividend / divider
    print('Результат:', result)
except CustomZeroDivisionError as ex:
    print(ex)
except ValueError:
    print('Неправильный формат ввода')
except:
    print('Какая-то другая ошибка')



