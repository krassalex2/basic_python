# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


import random


try:
    with open("task_5.txt", "w", encoding="utf-8") as f_obj:
        for number in [random.random() * 100 for item in range(10)]:
            f_obj.write(f"{number} ")
except Exception:
    print("При записи файла что-то пошло не так...")

try:
    with open("task_5.txt", "r", encoding="utf-8") as f_obj:
        print(f_obj.read())
except Exception:
    print("При показе файла что-то пошло не так...")

try:
    with open("task_5.txt", "r", encoding="utf-8") as f_obj:
        numbers = [float(number) for number in f_obj.read().split()]
        result = sum(numbers)
        print(f"Сумма: {result}")
except Exception:
    print("Что-то при чтении файла пошло не так...")
