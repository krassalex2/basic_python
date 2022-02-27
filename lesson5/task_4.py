# —оздать (не программно) текстовый файл со следующим содержимым:
# One Ч 1
# Two Ч 2
# Three Ч 3
# Four Ч 4
# Ќапишите программу, открывающую файл на чтение и считывающую построчно данные.
# ѕри этом английские числительные должны замен¤тьс¤ на русские.
# Ќовый блок строк должен записыватьс¤ в новый текстовый файл.


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
