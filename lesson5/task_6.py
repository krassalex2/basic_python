# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def getHours(n):
    result = "".join([char for char in n if char.isdigit()])
    return int(result) if len(result) > 0 else 0


result_dict = dict()
with open("task_6.txt", "r", encoding='utf-8') as f_obj:
    for item in f_obj:
        subject, n1, n2, n3 = item.split()
        result_dict[subject] = getHours(n1) + getHours(n2) + getHours(n3)
print(result_dict)
