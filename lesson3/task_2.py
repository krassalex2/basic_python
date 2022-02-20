# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def print_user_info(name, surname, year_of_birthday, city, email, phone):
    """
    Выводит данные о пользователя одной строкой.
    :param name: Имя
    :param surname: Фамилия
    :param year_of_birthday: Год рождения
    :param city: Город проживания
    :param email: Адрес электронной почты
    :param phone: Телефон
    """
    print(f'{name} {surname} {year_of_birthday} {city}, {email}, {phone}')


print_user_info(name='Ivan', surname='Ivanov', year_of_birthday=1990, city='Ivanteevka',
                email='ivanivanov@ivanov.ru', phone='88005553535')
