# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
#
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

# выручка
revenue = float(input('Введите выручку фирмы: '))

# издержки
costs = float(input('Введите издержки фирмы: '))

# финансовый результат
result = revenue - costs

if result > 0:
    print(f'Прибыль фирмы составляет: {result:.2f}')
elif result < 0:
    print(f'Убыток фирмы составляет: {result:.2f}')
else:
    print('Вы сработали в себестоимость')

if result > 0:
    # Рентабельность
    profitability = result / revenue
    print(f'Рентабельность выручки составляет: {profitability:.2f}')

    employees_count = int(input('Введите кол-во сотрудников в фирме: '))
    # Прибыль фирмы в расчете на одного сотрудника
    result_by_employee = result / employees_count
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {result_by_employee:.2f}')