# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

source_number = int(input('Введите целое положительное число: '))

max_digit = 0
divider = 10
next_number = source_number
while next_number > 0:
    digit = next_number % divider
    print('Проверяемый разряд: ', digit)
    if digit > max_digit:
        max_digit = digit
    next_number = next_number // divider

print('Максимальная цифра в числе: ', max_digit)
