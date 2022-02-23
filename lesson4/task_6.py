# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.


from itertools import count, cycle


print('Задание 6_1')
start_number = 3
for item in count(start_number):
    print(item)
    if item == 10:
        break


print('Задание 6_2')
source_list = list('abrakadabra')
max_iteration_count = 20
index = 0
for item in cycle(source_list):
    print(item)
    index += 1
    if index == max_iteration_count:
        break
