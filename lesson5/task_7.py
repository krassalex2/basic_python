# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


from json import dump


result_dict = dict()
average_dict = dict()
with open("task_7.txt") as f_obj:
    for row in f_obj:
        name, forma, revenue, costs = row.split()
        revenue = float(revenue)
        costs = float(costs)
        result_dict[name] = revenue - costs

profits = [r for r in result_dict.values() if r > 0]
average_dict["average_profit"] = sum(profits) / len(profits)

final_list = [result_dict, average_dict]
with open("task_7.json", "w", encoding="utf-8") as f_obj:
    dump(final_list, f_obj, ensure_ascii=False)
