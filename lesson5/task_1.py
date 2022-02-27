# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.


with open("task_1.txt", "w", encoding='utf-8') as f_obj:
    while True:
        line = input("Input line: ")
        if not line:
            break
        f_obj.write(f"{line}\n")
