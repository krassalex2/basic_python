# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.


result_list = [item for item in range(20, 241) if item % 20 == 0 or item % 21 == 0]
print(result_list)
