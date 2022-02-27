# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


try:
    with open("task_2.txt", "r", encoding='utf-8') as f_obj:
        count_rows = 0
        for row in f_obj:
            print(f"В строке '{row.rstrip()}' {len(row.split())} слов(а)")
            count_rows += 1
        print(f"Всего: {count_rows} строк(и)")
except IOError:
    print("Ошибка ввода-вывода")
