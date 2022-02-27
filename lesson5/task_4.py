# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


try:
    dict_map = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open("task_4.txt") as s_obj:
        with open("task_4_result.txt", "w") as r_obj:
            for row in s_obj:
                name, delimeter, digit = row.split()
                result_name = dict_map.get(name)
                print(f"{result_name} {delimeter} {digit}", file=r_obj)
except Exception:
    print("Что-то пошло не так...")
