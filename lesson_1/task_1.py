# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.


number_var = 10
print(number_var)
print(type(number_var))

float_var = 10.1
print(float_var)
print(type(float_var))

str_var = 'Task 1'
print(str_var)
print(type(str_var))

list_var = [1, 2, 3]
print(list_var)
print(type(list_var))

tuple_var = (1, 2, 3)
print(tuple_var)
print(type(tuple_var))

dict_var = {1: 'task_1', 2: 'task_2'}
print(dict_var)
print(type(dict_var))

bool_var = True
print(bool_var)
print(type(bool_var))

user_name = input('Введите ваше имя: ')
user_surname = input('Введите вашу фамилию: ')
user_age = int(input('Введите ваш возраст: '))
user_height = int(input('Введите ваш рост: '))
print(f'Вас зовут {user_surname} {user_name}. Вам {user_age}. Рост {user_height}')
